"""Module for a reservoir model."""
import filecmp
import logging
import math
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional, Union, get_args

import numpy as np

import rtctools_simulation.reservoir.setq_help_functions as setq_functions
from rtctools_simulation.interpolate import fill_nans_with_interpolation
from rtctools_simulation.model import Model, ModelConfig
from rtctools_simulation.reservoir._input import (
    Input,
    OutflowType,
    input_to_dict,
)
from rtctools_simulation.reservoir._variables import (
    FixedInputVar,
    InputVar,
    OutputVar,
    QOutControlVar,
)
from rtctools_simulation.reservoir.rule_curve import rule_curve_discharge
from rtctools_simulation.reservoir.rule_curve_deviation import (
    rule_curve_deviation,
)

DEFAULT_MODEL_DIR = Path(__file__).parent.parent / "modelica" / "reservoir"

logger = logging.getLogger("rtctools")


class ReservoirModel(Model):
    """Class for a reservoir model."""

    def __init__(self, config: ModelConfig, use_default_model=True, **kwargs):
        """
        Initialize the model.

        :param use_default_model BOOL: (default=True)
            If true, the default single reservoir model will be used.
        """
        if use_default_model:
            self._create_model(config)
        super().__init__(config, **kwargs)
        # Stored parameters
        self.max_reservoir_area = 0  # Set during pre().
        # Model inputs and input controls.
        self._input = Input()
        self._allow_set_var = True

    def _get_lookup_table_equations(self, allow_missing_lookup_tables=True):
        return super()._get_lookup_table_equations(allow_missing_lookup_tables)

    def _create_model(self, config: ModelConfig):
        """Create a model folder based on the default model."""
        base_dir = config.base_dir()
        if base_dir is None:
            raise ValueError("A base directory should be set when using the default model.")
        model_dir = base_dir / "generated_model"
        if not model_dir.is_dir():
            model_dir.mkdir()
        config.set_dir("model", model_dir)
        config.set_model("Reservoir")
        for filename in ["reservoir.mo", "lookup_table_equations.csv"]:
            default_file = DEFAULT_MODEL_DIR / filename
            file = model_dir / filename
            if file.is_file() and filecmp.cmp(default_file, file, shallow=False):
                continue
            shutil.copy2(default_file, file)

    # Methods for preprocsesing.
    def pre(self, *args, **kwargs):
        """
        This method can be overwritten to perform any pre-processing before the simulation begins.

        .. note:: Be careful if you choose to overwrite this method as default values have been
            carefully chosen to select the correct default schemes.
        """
        super().pre(*args, **kwargs)
        timeseries_names = self.io.get_timeseries_names()
        input_vars = get_args(QOutControlVar) + get_args(FixedInputVar)
        default_values = {var: 0 for var in input_vars}
        # To avoid infeasibilities,
        # the default value for the elevation needs to be within the range of the lookup table.
        # We use the intial volume or elevation to ensure this.
        if "H_observed" in timeseries_names:
            initial_h = float(self.get_timeseries("H_observed")[0])
        elif "H" in timeseries_names:
            initial_h = float(self.get_timeseries("H")[0])
        elif "V" in timeseries_names:
            initial_h = float(self._lookup_tables["h_from_v"](self.get_timeseries("V")[0]))
        else:
            raise Exception(
                'No initial condition is provided for reservoir elevation, "H", '
                'reservoir volume, "V", or observed elevation "H_observed". '
                "One of these must be provided."
            )
        default_values[InputVar.H_OBSERVED.value] = initial_h
        for var in input_vars:
            default_value = default_values[var]
            if var not in timeseries_names:
                self.set_timeseries(var, [default_value] * len(self.times()))
                logger.info(f"{var} not found in the input file. Setting it to {default_value}.")
                continue
            timeseries = self.get_timeseries(var)
            if var == InputVar.H_OBSERVED.value and np.isnan(timeseries[0]):
                timeseries[0] = initial_h
            if np.all(np.isnan(timeseries)):
                timeseries = [default_value] * len(self.times())
                logger.info(
                    f"{var} contains only NaNs in the input file. "
                    f"Setting these values to {default_value}."
                )
                continue
            logger.info(
                f"{var} contains NaNs in the input file. "
                f"Setting these values using linear interpolation."
            )
            timeseries = fill_nans_with_interpolation(self.times(), timeseries)
            self.set_timeseries(var, timeseries)
        # Set parameters.
        self.max_reservoir_area = self.parameters().get("max_reservoir_area", 0)

    # Helper functions for getting/setting the time/date/variables.
    def get_var(self, name: str) -> float:
        """
        Get the value of a given variable at the current time.

        :param var: name of the variable.
        :returns: value of the given variable.
        """
        try:
            value = super().get_var(name)
        except KeyError:
            expected_vars = list(InputVar) + list(OutputVar)
            message = f"Variable {name} not found." f" Expected var to be one of {expected_vars}."
            return KeyError(message)
        return value

    def set_var(self, name: str, value):
        """
        Set the value of a given variable at the current time.

        :param name: variable name.
        :param value: value to set the variable with.
        :returns: value of the given variable.

        :meta private:
        """
        if not self._allow_set_var:
            raise ValueError("Do not set variables directly. Use schemes instead.")
        return super().set_var(name, value)

    def get_current_time(self) -> int:
        """
        Get the current time (in seconds).

        :returns: the current time (in seconds).
        """
        return super().get_current_time()

    def get_current_datetime(self) -> datetime:
        """
        Get the current datetime.

        :returns: the current time in datetime format.
        """
        current_time = self.get_current_time()
        return self.io.sec_to_datetime(current_time, self.io.reference_datetime)

    def set_time_step(self, dt):
        """
        Set the time step size.

        :meta private:
        """
        # TODO: remove once set_q allows variable dt.
        current_dt = self.get_time_step()
        if current_dt is not None and not math.isclose(dt, current_dt):
            raise ValueError("Timestep size cannot change during simulation.")
        super().set_time_step(dt)

    # Schemes
    def apply_spillway(self):
        """Scheme to enable water to spill from the reservoir.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        This scheme ensures that the spill "Q_spill" is computed from the elevation "H" using a
        lookuptable "qspill_from_h".
        """
        self._input.outflow.outflow_type = OutflowType.COMPOSITE
        self._input.outflow.components.do_spill = True

    def apply_adjust(self):
        """Scheme to adjust simulated volume to observed volume.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        Observed pool elevations (H_observed) can be provided to the model, internally these are
        converted to observed volumes (V_observed) via the lookup table ``h_from_v``.
        When applying this scheme, V is set to V_observed and a corrected version of the outflow,
        Q_out_corrected, is calculated in order to preserve the mass balance.
        """
        # Disable compute_v so V will equal v_observed
        self._input.volume.compute_v = False

    def apply_passflow(self):
        """Scheme to let the outflow be the same as the inflow.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.

        .. note:: This scheme cannot be used in combination with
            :py:meth:`.ReservoirModel.apply_poolq`, or :py:meth:`.ReservoirModel.set_q` when the
            target variable is Q_out.
        """
        self._input.outflow.outflow_type = OutflowType.PASS

    def apply_poolq(self):
        """Scheme to let the outflow be determined by a lookup table with name "qout_from_v".

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.

        It is possible to impose a dependence on days using the “qout_from_v” lookup table
        If this is not needed then the “day” column should be constant (e.g. = 1)
        Otherwise a 2D lookup table is created by linear interpolation between days, Q_out and V.

        .. note:: This scheme cannot be used in combination with
            :py:meth:`.ReservoirModel.apply_passflow`, or :py:meth:`.ReservoirModel.set_q` when the
            target variable is Q_out.
        """
        self._input.outflow.outflow_type = OutflowType.LOOKUP_TABLE

    def include_rain(self):
        """Scheme to  include the effect of rainfall on the reservoir volume.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        This scheme computes

             Q_rain = max_reservoir_area * mm_rain_per_hour / 3600 / 1000 * include_rain.

        This is then treated in the mass balance of the reservoir

            der(V) = Q_in - Q_out + Q_rain - Q_evap.

        .. note:: To include rainfall, make sure to set the max_reservoir_area parameter.
        """
        assert (
            self.max_reservoir_area > 0
        ), "To include rainfall, make sure to set the max_reservoir_area parameter."
        self._input.rain_evap.include_rain = True

    def include_evaporation(self):
        """Scheme to include the effect of evaporation on the reservoir volume.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        This scheme computes

            Q_evap = Area * mm_evaporation_per_hour / 3600 / 1000 * include_evaporation.

        This is then treated in the mass balance of the reservoir

            der(V) = Q_in - Q_out + Q_rain - Q_evap.
        """
        self._input.rain_evap.include_evaporation = True

    def include_rainevap(self):
        """Scheme to include the effect of both rainfall and evaporation on the reservoir volume.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        This scheme implements both :py:meth:`.ReservoirModel.include_rain`
        and :py:meth:`.ReservoirModel.include_evaporation`.
        """
        self._input.rain_evap.include_rain = True
        self._input.rain_evap.include_evaporation = True

    def apply_rulecurve(self, outflow: QOutControlVar = InputVar.Q_TURBINE):
        """Scheme to set the outflow of the reservoir in order to reach a rulecurve.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.
        This scheme uses the lookup table ``v_from_h`` and requires the following parameters
        from the ``rtcParameterConfig.xml`` file.

            - ``rule_curve_q_max``: Upper limiting discharge while blending pool elevation
              (m^3/timestep)
            - ``rule_curve_blend``:  Number of timesteps over which to bring the pool back to the
              scheduled elevation.

        The user must also provide a timeseries with the name ``rule_curve``. This contains the
        water level target for each timestep.

        :param outflow: :py:type:`~rtctools_simulation.reservoir._variables.QOutControlVar`
            (default: :py:type:`~rtctools_simulation.reservoir._variables.InputVar.Q_TURBINE`)
            outflow variable that is modified to reach the rulecurve.

        .. note:: This scheme does not correct for the inflows to the reservoir. As a result,
            the resulting height may differ from the rule curve target.
        """
        outflow = InputVar(outflow)
        current_step = int(self.get_current_time() / self.get_time_step())
        q_max = self.parameters().get("rule_curve_q_max")
        if q_max is None:
            raise ValueError(
                "The parameter rule_curve_q_max is not set, "
                + "which is required for the rule curve scheme"
            )
        blend = self.parameters().get("rule_curve_blend")
        if blend is None:
            raise ValueError(
                "The parameter rule_curve_blend is not set, "
                "which is required for the rule curve scheme"
            )
        try:
            rule_curve = self.io.get_timeseries("rule_curve")[1]
        except KeyError as exc:
            raise KeyError("The rule curve timeseries is not found in the input file.") from exc
        v_from_h_lookup_table = self.lookup_tables().get("v_from_h")
        if v_from_h_lookup_table is None:
            raise ValueError(
                "The lookup table v_from_h is not found"
                " It is required for the rule curve scheme."
            )
        volume_target = v_from_h_lookup_table(rule_curve[current_step])
        current_volume = self.get_var("V")
        discharge = rule_curve_discharge(
            volume_target,
            current_volume,
            q_max,
            blend,
        )
        discharge_per_second = discharge / self.get_time_step()
        self._set_q(outflow, discharge_per_second)
        logger.debug(f"Rule curve function has set the outflow to {discharge_per_second} m^3/s.")

    def calculate_rule_curve_deviation(
        self,
        periods: int,
        inflows: Optional[np.ndarray] = None,
        q_max: float = np.inf,
        maximum_difference: float = np.inf,
    ):
        """Calculate the moving average between the rule curve and the simulated elevations.

        This method can be applied inside :py:meth:`.ReservoirModel.calculate_output_variables`.

        This method calculates the moving average between the rule curve and the simulated
        elevations over a specified number of periods. It takes the following parameters:

        :param periods: The number of periods over which to calculate the moving average.
        :param inflows: Optional. The inflows to the reservoir. If provided, the moving average
                        will be calculated only for the periods with non-zero inflows.
        :param q_max: Optional. The maximum discharge allowed while calculating the moving average.
                      Default is infinity, required if q_max is set.
        :param maximum_difference: Optional. The maximum allowable difference between the rule curve
                                   and the simulated elevations.

        .. note:: The rule curve timeseries must be present in the timeseries import. The results
            are stored in the timeseries "rule_curve_deviation".
        """
        observed_elevations = self.extract_results().get("H")
        try:
            rule_curve = self.io.get_timeseries("rule_curve")[1]
        except KeyError as exc:
            raise KeyError("The rule curve timeseries is not found in the input file.") from exc
        deviations = rule_curve_deviation(
            observed_elevations,
            rule_curve,
            periods,
            inflows=inflows,
            q_max=q_max,
            maximimum_difference=maximum_difference,
        )
        self.set_timeseries("rule_curve_deviation", deviations)
        self.extract_results().update({"rule_curve_deviation": deviations})

    def _set_q(self, q_var: QOutControlVar, value: float):
        """Set an outflow control variable."""
        if q_var == InputVar.Q_OUT:
            self._input.outflow.outflow_type = OutflowType.FROM_INPUT
            self._input.outflow.from_input = value
        elif q_var == InputVar.Q_TURBINE:
            self._input.outflow.outflow_type = OutflowType.COMPOSITE
            self._input.outflow.components.turbine = value
        elif q_var == InputVar.Q_SLUICE:
            self._input.outflow.outflow_type = OutflowType.COMPOSITE
            self._input.outflow.components.sluice = value
        else:
            raise ValueError(f"Outflow shoud be one of {get_args(QOutControlVar)}.")

    # Methods for applying schemes / setting input.
    def set_default_input(self):
        """Set default input values.

        This method sets default values for internal variables at each timestep.
        This is important to ensure that the schemes behave as expected.

        :meta private:
        """
        self._input = Input()
        self._input.volume.h_observed = self.get_var(InputVar.H_OBSERVED.value)
        self._input.inflow = self.get_var(InputVar.Q_IN.value)
        self._input.rain_evap.mm_evaporation_per_hour = self.get_var("mm_evaporation_per_hour")
        self._input.rain_evap.mm_rain_per_hour = self.get_var("mm_rain_per_hour")
        self._input.outflow.components.turbine = self.get_var("Q_turbine")
        self._input.outflow.components.sluice = self.get_var("Q_sluice")
        self._input.outflow.from_input = self.get_var("Q_out_from_input")
        self._input.day = self.get_current_datetime().day

    def apply_schemes(self):
        """
        Apply schemes.

        This method is called at each timestep and should be implemented by the user.
        This method should contain the logic for which scheme is applied under which conditions.

        :meta private:
        """
        pass

    def calculate_output_variables(self):
        """
        Calculate output variables.

        This method is called after the simulation has finished.
        The user can implement this method to calculate additional output variables.
        """
        pass

    def set_input_variables(self):
        """Set input variables.

        This method calls :py:meth:`.ReservoirModel.set_default_input` and
        :py:meth:`.ReservoirModel.apply_schemes`.
        This method can be overwritten to set input at each timestep.

        .. note:: Be careful if you choose to overwrite this method as default values have been
            carefully chosen to select the correct default schemes.

        :meta private:
        """
        self._allow_set_var = False
        self.set_default_input()
        self.apply_schemes()
        self._allow_set_var = True
        self._set_modelica_input()

    def _set_modelica_input(self):
        """Set the Modelica input variables."""
        # Validate model input.
        self._input = Input(**self._input.model_dump())
        # Set Modelica inputs.
        modelica_vars = input_to_dict(self._input)
        for var, value in modelica_vars.items():
            self.set_var(var.value, value)

    # Plotting
    def get_output_variables(self):
        """Method to get, and extend output variables

        This method gets all output variables of the reservoir model, and extends the
        output to also include input variables like "Q_in" and "Q_turbine" such that they appear in
        the timeseries_export.xml.
        """
        variables = super().get_output_variables().copy()
        variables.extend(["Q_in"])
        variables.extend(["Q_turbine"])
        variables.extend(["Q_sluice"])
        return variables

    def set_q(
        self,
        target_variable: QOutControlVar = InputVar.Q_TURBINE,
        input_type: str = "timeseries",
        input_data: Union[str, float, list[float]] = None,
        apply_func: str = "MEAN",
        timestep: int = None,
        nan_option: str = None,
    ):
        """
        Scheme to set one of the input or output discharges to a given value,
        or a value determined from an input list.

        This scheme can be applied inside :py:meth:`.ReservoirModel.apply_schemes`.

        .. note:: This scheme cannot be used
            in combination with :py:meth:`.ReservoirModel.apply_poolq`, or
            :py:meth:`.ReservoirModel.apply_passflow` if the target variable is Q_out.

        :param target_variable: :py:type:`~rtctools_simulation.reservoir._variables.QOutControlVar`
            (default: :py:const:`~rtctools_simulation.reservoir._variables.InputVar.Q_TURBINE`)
            The variable that is to be set. Needs to be an internal variable, limited to discharges.
        :param input_type: str (default: 'timeseries')
            The type of target data. Either 'timeseries' or 'parameter'. If it is a timeseries,
            the timeseries is assumed to have a regular time interval.
        :param input_data: str | float | list[float] (default: None)
            Single value or a list of values for each time step to set the target.
            It can also be a name of a parameter or input variable.
        :param apply_func: str (default: 'MEAN')
            Function that is used to find the fixed_value if input_type = 'timeseries'.

                - 'MEAN' (default): Finds the average value, excluding nan-values.
                - 'MIN': Finds the minimum value, excluding nan-values.
                - 'MAX': Finds the maximum value, excluding nan-values.
                - 'INST': Finds the value marked by the corresponding timestep 't'. If the
                  selected value is NaN, nan_option determines the procedure to find a valid
                  value.

        :param timestep: int (default: None)
            The timestep at which the input data should be read at if input_type = 'timeseries',
            the default is the current timestep of the simulation run.
        :param nan_option: str (default: None)
            the user can indicate the action to be take if missing values are found.
            Usable in combination with input_type = 'timeseries' and apply_func = 'INST'.

                - 'MEAN': It will take the mean of the timeseries excluding nans.
                - 'PREV': It attempts to find the closest previous valid data point.
                - 'NEXT': It attempts to find the closest next valid data point.
                - 'CLOSEST': It attempts to find the closest valid data point, either backwards or
                  forward. If same distance, take average.
                - 'INTERP': Interpolates linearly between the closest forward and backward data
                  points.
        """
        # TODO: enable set_q to handle variable timestep sizes.
        target_variable = InputVar(target_variable)
        target_value = setq_functions.getq(
            self,
            target_variable,
            input_type,
            apply_func,
            input_data,
            timestep,
            nan_option,
        )
        self._set_q(target_variable.value, target_value)
