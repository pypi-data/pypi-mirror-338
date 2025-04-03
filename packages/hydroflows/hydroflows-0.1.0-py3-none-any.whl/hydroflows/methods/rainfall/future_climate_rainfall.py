"""Method to deriving future climate rainfall by scaling an historical event using Clausius-Clapeyron (CC)."""

from logging import getLogger
from pathlib import Path
from typing import List, Optional

from hydroflows._typing import (
    ClimateScenariosDict,
    FileDirPath,
    ListOfStr,
    OutputDirPath,
)
from hydroflows.events import Event, EventSet
from hydroflows.workflow.method import ExpandMethod
from hydroflows.workflow.method_parameters import Parameters

logger = getLogger(__name__)

__all__ = ["FutureClimateRainfall", "Input", "Output", "Params"]


class Input(Parameters):
    """Input parameters for the :py:class:`FutureClimateRainfall` method."""

    event_set_yaml: FileDirPath
    """The file path to the event set YAML file, which includes the events to be scaled
    for future climate projections, see also :py:class:`hydroflows.events.EventSet`."""


class Output(Parameters):
    """Output parameters for the :py:class:`FutureClimateRainfall` method."""

    future_event_yaml: FileDirPath
    """The path to the scaled event description file,
    see also :py:class:`hydroflows.events.Event`."""

    future_event_csv: Path
    """The path to the scaled event csv timeseries file."""

    future_event_set_yaml: FileDirPath
    """The path to the scaled event set yml file,
    see also :py:class:`hydroflows.events.EventSet`.
    """


class Params(Parameters):
    """Parameters for :py:class:`FutureClimateRainfall` method."""

    scenarios: ClimateScenariosDict
    """Future scenario name, e.g. "rcp45_2050", and delta temperature for Clausius-Clapeyron scaling.

    The delta temperature represents the projected temperature increase, with an emphasis on
    hot days, rather than a simple average temperature change. To accurately capture extreme
    temperature shifts, it is recommended that users consider high quantiles
    (e.g., the 95th percentile) in their analyses.

    Temperature changes for different periods and emission scenarios
    for CMIP5 and CMIP6 models can be taken via:
    `Future Climate Data Platform <https://dap.climateinformation.org/dap/>`_"""

    event_root: OutputDirPath
    """Root folder to save the derived scaled events."""

    event_names: ListOfStr
    """List of event names (subset of event_set_yaml events)."""

    alpha: float = 0.07
    """The rate of change of precipitation with respect to temperature (per degree)
    used in Clausius-Clapeyron (CC) scaling"""

    event_wildcard: str = "future_event"
    """The wildcard key for expansion over the scaled events."""

    scenario_wildcard: str = "scenario"
    """The wildcard key for expansion over the scenarios."""


class FutureClimateRainfall(ExpandMethod):
    """Method to derive future climate rainfall by scaling an historical event using Clausius-Clapeyron (CC).

    Parameters
    ----------
    scenarios: Dict[str, float]
        Future scenario name, e.g. "rcp45_2050", and delta temperature for CC scaling.
    event_set_yaml : Path
        The file path to the event set YAML file, which includes the events to be scaled
        for a future climate projection.
    event_names: Optional[List[str]]
        List of event names in event_set_yaml
        If not provided, event_set_yaml must exist to get the event names.
    event_root: Path, optional
        Root folder to save the derived scaled events, by default "data/events/future_rainfall".
    wildcard: str
        The wildcard key for expansion over the scaled events, default is "future_event".
    **params
        Additional parameters to pass to the FutureClimateRainfall Params instance.

    See Also
    --------
    :py:class:`FutureClimateRainfall Input <hydroflows.methods.rainfall.future_climate_rainfall.Input>`
    :py:class:`FutureClimateRainfall Output <hydroflows.methods.rainfall.future_climate_rainfall.Output>`
    :py:class:`FutureClimateRainfall Params <hydroflows.methods.rainfall.future_climate_rainfall.Params>`
    """

    name: str = "future_climate_rainfall"

    _test_kwargs = {
        "scenarios": {"rcp45_2050": 1.0},
        "event_set_yaml": Path("event_set.yaml"),
        "event_names": ["p_event1", "p_event2"],
    }

    def __init__(
        self,
        scenarios: dict[str, float],
        event_set_yaml: Path,
        event_names: Optional[List[str]] = None,
        event_root: Path = Path("data/events"),
        event_wildcard: str = "future_event",
        scenario_wildcard: str = "scenario",
        **params,
    ) -> None:
        self.input: Input = Input(event_set_yaml=event_set_yaml)

        event_set_names = None
        if self.input.event_set_yaml.exists():
            event_set = EventSet.from_yaml(self.input.event_set_yaml)
            event_set_names = [event["name"] for event in event_set.events]

        if event_names is None and event_set_names is not None:
            event_names = event_set_names
        elif event_names is None:
            raise ValueError(
                "event_names must be provided if event_set_yaml does not exist"
            )

        self.params: Params = Params(
            scenarios=scenarios,
            event_root=event_root,
            event_wildcard=event_wildcard,
            scenario_wildcard=scenario_wildcard,
            event_names=event_names,
            **params,
        )
        if event_set_names is not None:
            # make sure all event names are in the event set
            if not set(self.params.event_names).issubset(event_set_names):
                raise ValueError(
                    "event_names must be subset of event names in event_set_yaml"
                )

        ewc = "{" + self.params.event_wildcard + "}"
        swc = "{" + self.params.scenario_wildcard + "}"

        self.output: Output = Output(
            future_event_yaml=self.params.event_root / swc / f"{ewc}.yml",
            future_event_csv=self.params.event_root / swc / f"{ewc}.csv",
            future_event_set_yaml=self.params.event_root
            / swc
            / f"{self.input.event_set_yaml.stem}_{swc}.yml",
        )

        self.set_expand_wildcard(self.params.event_wildcard, self.params.event_names)
        self.set_expand_wildcard(
            self.params.scenario_wildcard, list(self.params.scenarios.keys())
        )

    def _run(self):
        """Run the FutureClimateRainfall method."""
        event_set = EventSet.from_yaml(self.input.event_set_yaml)

        # scenario in outer loop because of event set
        for scenario, dT in self.params.scenarios.items():
            # List to save the scaled events
            future_events_list = []

            for name in self.params.event_names:
                output = self.get_output_for_wildcards(
                    {
                        self.params.event_wildcard: name,
                        self.params.scenario_wildcard: scenario,
                    }
                )

                # Load the original event
                event: Event = event_set.get_event(name)

                # scale the precip forcing, keep other forcings
                forcings = []
                delta_precip = (1 + self.params.alpha) ** (dT)
                for forcing in event.forcings:
                    if forcing.type == "rainfall":
                        # update and write forcing timeseries to csv
                        future_event_df = forcing.data.copy() * delta_precip
                        future_event_df.to_csv(output["future_event_csv"], index=True)
                        forcing.path = output["future_event_csv"]
                    forcings.append(forcing)

                # write event to yaml
                future_event = Event(
                    name=name,
                    forcings=forcings,
                    return_period=event.return_period,
                )
                future_event.set_time_range_from_forcings()
                future_event.to_yaml(output["future_event_yaml"])

                # append event to list
                future_events_list.append(
                    {"name": name, "path": output["future_event_yaml"]}
                )

            # make and save event set yaml file
            future_event_set = EventSet(events=future_events_list)
            future_event_set.to_yaml(output["future_event_set_yaml"])
