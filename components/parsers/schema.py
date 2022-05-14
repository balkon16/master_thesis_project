from dataclasses import dataclass


@dataclass(frozen=True)
class Schema:
    field_name: str
    type: str # TODO: create a list of casting rules, e.g. float -> decimal etc.
    required: bool
