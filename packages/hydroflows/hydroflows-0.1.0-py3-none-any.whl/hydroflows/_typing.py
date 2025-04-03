import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Union

from pydantic import AfterValidator, BeforeValidator, Json
from typing_extensions import Annotated, TypedDict

from hydroflows.utils.parsers import (
    has_wildcards,
    str_to_list,
    str_to_list_nested,
    str_to_tuple,
)

ListOfStr = Annotated[
    list[str],
    BeforeValidator(lambda x: str_to_list(x) if isinstance(x, str) else x),
]

ListOfInt = Annotated[
    list[int],
    BeforeValidator(lambda x: str_to_list(x) if isinstance(x, str) else x),
]

ListOfFloat = Annotated[
    list[float],
    BeforeValidator(lambda x: str_to_list(x) if isinstance(x, str) else x),
]

ListOfListOfInt = Annotated[
    list[list[int]],
    BeforeValidator(lambda x: str_to_list_nested(x) if isinstance(x, str) else x),
]

TupleOfInt = Annotated[
    Tuple[int, int],
    BeforeValidator(
        lambda x: tuple(
            int(float(i)) if float(i).is_integer() else int(i) for i in str_to_tuple(x)
        )
        if isinstance(x, str)
        else x
    ),
]

ListOfPath = Annotated[
    List[Path],
    BeforeValidator(lambda x: str_to_list(x) if isinstance(x, str) else x),
]

JsonDict = Annotated[
    Union[Dict, Json],
    BeforeValidator(
        lambda x: json.loads(x.replace("'", '"')) if isinstance(x, str) else x
    ),
]


def _check_path_has_wildcard(path: Union[Path, List[Path]]) -> Path:
    """Check if a path contains a wildcard."""
    if isinstance(path, Path) and not has_wildcards(path):
        raise ValueError(f"Path {path} does not contain any wildcards")
    return path


WildcardPath = Annotated[
    Path,
    AfterValidator(_check_path_has_wildcard),
]

WildcardStr = Annotated[
    str,
    AfterValidator(_check_path_has_wildcard),
]

EventDatesDict = Annotated[
    Dict[
        str,
        TypedDict(
            "EventInfoDict",
            {
                "startdate": datetime,
                "enddate": datetime,
            },
        ),
    ],
    BeforeValidator(
        lambda x: json.loads(x.replace("'", '"')) if isinstance(x, str) else x
    ),
]

ClimateScenariosDict = Annotated[
    Dict[str, float],
    BeforeValidator(
        lambda x: json.loads(x.replace("'", '"')) if isinstance(x, str) else x
    ),
]

DataCatalogPath = Union[ListOfStr, ListOfPath, Path]


class filedirpath(Path):
    """Subtype Path to indicate when parent folder is needed for workflow execution."""

    _flavour = type(Path())._flavour


def filedir_validator(x: Path) -> filedirpath:
    """Promote Path to filedirpath type."""
    return filedirpath(x)


FileDirPath = Annotated[Path, AfterValidator(filedir_validator)]


class outputdirpath(Path):
    """Subclass Path to indicate Param is used as root for output locations."""

    _flavour = type(Path())._flavour


def outputdirpath_validator(x: Path) -> outputdirpath:
    """Promote Path to outputdirpath."""
    return outputdirpath(x)


OutputDirPath = Annotated[Path, AfterValidator(outputdirpath_validator)]
