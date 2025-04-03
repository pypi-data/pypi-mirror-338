from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from hydroflows.methods.script.script_method import ScriptMethod
from hydroflows.utils.parsers import get_wildcards

if TYPE_CHECKING:
    from hydroflows.workflow.method import Method
    from hydroflows.workflow.rule import Rule


class JinjaSnakeRule:
    """ViewModel for a Rule to print in a Jinja Snakemake template."""

    def __init__(self, rule: "Rule"):
        self.rule = rule

    @property
    def method(self) -> "Method":
        """Get the rule method instance."""
        return self.rule.method

    @property
    def rule_id(self) -> str:
        """Get the name of the rule."""
        return self.rule.rule_id

    @property
    def method_name(self) -> str:
        """Get the name of the method."""
        return self.method.name

    @property
    def input(self) -> Dict[str, str]:
        """Get the rule input path parameters."""
        wildcards = self.rule.wildcards["reduce"]
        wildcard_fields = []
        for wc in wildcards:
            wildcard_fields.extend(self.rule.wildcard_fields.get(wc))
        result = self.method.input.to_dict(
            mode="json",
            filter_types=Path,
            return_refs=True,
            exclude_ref_keys=wildcard_fields,
            posix_path=True,
            quote_str=True,
        )
        for key, val in result.items():
            if wildcards and any(get_wildcards(val, wildcards)):
                result[key] = self._expand_variable(val, wildcards)
            else:
                result[key] = self._parse_variable(val)
        return result

    @property
    def output(self) -> Dict[str, str]:
        """Get the rule output path parameters."""
        result = self.method.output.to_dict(
            mode="json",
            filter_types=Path,
            posix_path=True,
            quote_str=True,
        )
        wildcards = self.rule.wildcards["expand"]
        for key, val in result.items():
            if wildcards and any(get_wildcards(val, wildcards)):
                result[key] = self._expand_variable(val, wildcards)
            else:
                result[key] = self._parse_variable(val)
        return result

    @property
    def params(self) -> Dict[str, str]:
        """Get the rule parameters."""
        result = self.method.params.to_dict(
            mode="json",
            exclude_defaults=True,
            return_refs=True,
            posix_path=True,
            quote_str=True,
        )
        return {key: self._parse_variable(val) for key, val in result.items()}

    @property
    def rule_all_input(self) -> str | None:
        """Get single output path for result rule, or None if not result rule."""
        if self.rule_id not in self.rule.workflow.rules.result_rules:
            return None
        result = self.method.output.to_dict(
            mode="json",
            filter_types=Path,
            posix_path=True,
            quote_str=True,
        )
        wildcards = self.rule.workflow.wildcards.names
        # get first key and value of the output
        key, val = next(iter(result.items()))
        if key in self.rule._all_wildcard_fields:
            val = self._expand_variable(val, wildcards)
        return val

    @property
    def hydroflows_shell_kwargs(self) -> Dict[str, str]:
        """Get the rule shell arguments."""
        return self.method._kwargs_to_key_mapping()

    @property
    def script(self) -> Optional[str]:
        """Get the rule script."""
        if isinstance(self.method, ScriptMethod):
            return self.method.input.script.as_posix()
        return None

    def _expand_variable(self, val: str, wildcards: List) -> Any:
        expand_lst = []
        for wc in get_wildcards(val, wildcards):
            expand_lst.append(f"{wc}={wc.upper()}")
        escape_wc = list(set(self.rule.wildcards["repeat"]) - set(wildcards))
        for wc in get_wildcards(val, escape_wc):
            # escape wildcard in the value which is not expanded
            val = val.replace("{" + wc + "}", "{{" + wc + "}}")
        if len(expand_lst) == 0:
            return val
        expand_str = ", ".join(expand_lst)
        val = f"expand({val}, {expand_str})"
        return val

    def _parse_variable(self, val: Any) -> str:
        """Parse references to snakemake format."""
        if isinstance(val, str) and val.startswith("$config."):
            dict_keys = val.split(".")[1:]
            val = 'config["' + '"]["'.join(dict_keys) + '"]'
        elif isinstance(val, str) and val.startswith("$rules."):
            ref = self.rule.workflow.get_ref(val)
            # exclude reference to snake expand(..) fields
            if ref.is_expand_field:
                val = ref.get_str_value()
            else:
                val = val[1:]
        elif isinstance(val, str) and val.startswith("$wildcards."):
            val = val.split(".")[1].upper()
        return str(val)
