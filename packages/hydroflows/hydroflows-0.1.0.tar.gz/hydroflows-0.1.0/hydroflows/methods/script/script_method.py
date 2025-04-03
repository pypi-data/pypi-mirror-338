"""Method to run python script with HydroFlows."""

import json
import subprocess
from pathlib import Path
from typing import Any, ClassVar, Dict, Optional

from pydantic import ConfigDict, model_validator

from hydroflows.workflow.method import Method
from hydroflows.workflow.method_parameters import Parameters

__all__ = ["ScriptMethod", "ScriptInput", "ScriptOutput", "ScriptParams"]


class ScriptParams(Parameters):
    """Parameters for ScriptMethod class."""

    _type: ClassVar[str] = "param"

    # Allow extra fields in the model
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def _input_to_dict(cls, data: Any) -> Any:
        """Convert the input field to a dictionary."""
        # check if json and convert to dict
        if isinstance(data, str) and data.startswith("{") and data.endswith("}"):
            # replace single quotes with double quotes
            data = json.loads(data.replace("'", '"'))
        # check if single path and convert to dict
        elif isinstance(data, (Path, str)):
            data = {f"{cls._type}1": data}
        # check if list and convert to dict
        elif isinstance(data, list):
            data = {f"{cls._type}{i+1}": item for i, item in enumerate(data)}
        return data


class ScriptOutput(ScriptParams):
    """Input parameters for ScriptMethod class."""

    _type: ClassVar[str] = "output"

    @model_validator(mode="after")
    def check_extra_fields_are_paths(self):
        """Check that all extra fields are Path types."""
        for key, value in self:
            if value is None:
                continue  # skip None values such as initial script
            try:
                setattr(self, key, Path(value))
            except Exception:
                raise ValueError(f"{key} not a Path type ({type(value)})")
        return self


class ScriptInput(ScriptOutput):
    """Output parameters for ScriptMethod class."""

    _type: ClassVar[str] = "input"

    # NOTE script field is set optional here to be able to parse json input and add the script field later
    script: Optional[Path] = None
    """Path to the script file."""


class ScriptMethod(Method):
    """Method to run python script with HydroFlows.

    Parameters
    ----------
    script : Path
        Path to the script file.
    output : Dict[str, Path]
        Output files.
    input : Dict[str, Path]
        Input files.
    params : Dict
        Parameters.
    """

    name = "script_method"

    _test_kwargs = {
        "script": Path("script.py"),
        "input": [Path("input.txt"), Path("input2.txt")],
        "output": Path("output.txt"),
        "params": {"param1": "value1", "param2": 2},
    }

    def __init__(
        self,
        script: Path,
        output: Dict[str, Path],
        input: Dict[str, Path] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> None:
        input = {} if input is None else input
        params = {} if params is None else params
        # use model_validate on input first to to parse json input, then set script field
        self.input: ScriptInput = ScriptInput.model_validate(input)
        self.input.script = Path(script)
        self.output: ScriptOutput = ScriptOutput.model_validate(output)
        self.params: ScriptParams = ScriptParams.model_validate(params)

    def _run(self):
        """Run the python script."""
        # add input, params and output as json argument
        cmd = ["python", self.input.script.as_posix(), self.json_kwargs]
        # run with subprocess
        subprocess.run(cmd, check=True)

    @property
    def json_kwargs(self):
        """Return input, params and output as json string."""
        # remove script field
        data = self.to_dict(posix_path=True)
        data["input"].pop("script")
        if data["params"] == {}:
            data.pop("params")
        if data["input"] == {}:
            data.pop("input")
        return json.dumps(data)

    def to_kwargs(
        self,
        mode="json",
        exclude_defaults=True,
        posix_path=False,
        return_refs=False,
        **kwargs,
    ):
        """Convert the method to a dictionary of keyword arguments."""
        kwargs = dict(
            mode=mode,
            exclude_defaults=exclude_defaults,
            posix_path=posix_path,
            return_refs=return_refs,
            **kwargs,
        )
        input = self.input.to_dict(**kwargs)
        params = self.params.to_dict(**kwargs)
        kwargs = {
            "script": input.pop("script"),  # lower script field
            "output": self.output.to_dict(**kwargs),
        }
        if input:
            kwargs["input"] = input
        if params:
            kwargs["params"] = params
        return kwargs
