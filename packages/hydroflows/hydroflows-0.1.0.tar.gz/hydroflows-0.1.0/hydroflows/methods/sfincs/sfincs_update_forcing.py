"""Method to update SFINCS forcing."""

# from datetime.datetime import strftime
import logging
from pathlib import Path
from typing import Optional

from hydroflows._typing import FileDirPath, JsonDict, OutputDirPath
from hydroflows.events import Event
from hydroflows.methods.sfincs.sfincs_utils import parse_event_sfincs
from hydroflows.workflow.method import Method
from hydroflows.workflow.method_parameters import Parameters

__all__ = ["SfincsUpdateForcing", "Input", "Output", "Params"]

logger = logging.getLogger(__name__)


class Input(Parameters):
    """Input parameters for the :py:class:`SfincsUpdateForcing` method."""

    sfincs_inp: FileDirPath
    """The file path to the SFINCS basemodel configuration file (inp)."""

    event_yaml: FileDirPath
    """The path to the event description file,
    see also :py:class:`hydroflows.events.Event`."""


class Output(Parameters):
    """Output parameters for :py:class:`SfincsUpdateForcing` method."""

    sfincs_out_inp: FileDirPath
    """The path to the updated SFINCS configuration (inp) file per event."""


class Params(Parameters):
    """Parameters for the :py:class:`SfincsUpdateForcing` method."""

    event_name: str
    """The name of the event"""

    output_dir: OutputDirPath
    """Output location relative to the workflow root. The updated model will be stored in <output_dir>/<event_name>."""

    copy_model: bool = False
    """Create full copy of model or create rel paths in model config."""

    sfincs_config: JsonDict = {}
    """SFINCS simulation config settings to update sfincs_inp."""


class SfincsUpdateForcing(Method):
    """Method for updating SFINCS forcing with event data.

    SFINCS simulations are stored in {output_dir}/{event_name}.

    Parameters
    ----------
    sfincs_inp : Path
        The file path to the SFINCS basemodel configuration file (inp).
    event_yaml : Path
        The path to the event description file
    output_dir : str
        Output location of updated model
    event_name : str, optional
        The name of the event, by default derived from the event_yaml file name stem.
    **params
        Additional parameters to pass to the SfincsUpdateForcing instance.
        See :py:class:`sfincs_update_forcing Params <hydroflows.methods.sfincs.sfincs_update_forcing.Params>`.

    See Also
    --------
    :py:class:`sfincs_update_forcing Input <hydroflows.methods.sfincs.sfincs_update_forcing.Input>`
    :py:class:`sfincs_update_forcing Output <hydroflows.methods.sfincs.sfincs_update_forcing.Output>`
    :py:class:`sfincs_update_forcing Params <hydroflows.methods.sfincs.sfincs_update_forcing.Params>`
    """

    name: str = "sfincs_update_forcing"

    _test_kwargs = {
        "sfincs_inp": Path("sfincs.inp"),
        "event_yaml": Path("event1.yaml"),
        "output_dir": "simulations",
    }

    def __init__(
        self,
        sfincs_inp: Path,
        event_yaml: Path,
        output_dir: str,
        event_name: Optional[str] = None,
        **params,
    ):
        self.input: Input = Input(sfincs_inp=sfincs_inp, event_yaml=event_yaml)

        if event_name is None:
            # event name is the stem of the event file
            event_name = self.input.event_yaml.stem
        self.params: Params = Params(
            event_name=event_name, output_dir=output_dir, **params
        )
        if self.params.copy_model and not self.params.output_dir:
            raise ValueError("Unknown dest. folder for copy operation.")

        sfincs_out_inp = self.params.output_dir / "sfincs.inp"
        if not self.params.copy_model and not self.params.output_dir.is_relative_to(
            self.input.sfincs_inp.parent
        ):
            raise ValueError(
                "Output directory must be relative to input directory when not copying model."
            )
        self.output: Output = Output(sfincs_out_inp=sfincs_out_inp)

    def _run(self):
        """Run the SfincsUpdateForcing method."""
        # fetch event from event yaml file
        event: Event = Event.from_yaml(self.input.event_yaml)
        if event.name != self.params.event_name:
            raise ValueError(
                f"Event file name {self.input.event_yaml.stem} does not match event name {event.name}"
            )

        # update sfincs model with event forcing
        root = self.input.sfincs_inp.parent
        out_root = self.output.sfincs_out_inp.parent
        copy_model = self.params.copy_model
        parse_event_sfincs(
            root,
            event,
            out_root,
            sfincs_config=self.params.sfincs_config,
            copy_model=copy_model,
        )
