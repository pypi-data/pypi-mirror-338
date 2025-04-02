from enum import StrEnum
from typing import Any, List, Type, get_origin
from mongo_validations_generator.custom_types import Long


class BSONType(StrEnum):
    DOUBLE = "double"
    STRING = "string"
    OBJECT = "object"
    ARRAY = "array"
    BOOL = "bool"
    NULL = "null"
    INT = "int"
    LONG = "long"


TYPE_MAP: dict[Type[Any], str] = {
    str: BSONType.STRING.value,
    int: BSONType.INT.value,
    float: BSONType.DOUBLE.value,
    bool: BSONType.BOOL.value,
    list: BSONType.ARRAY.value,
    type(None): BSONType.NULL.value,
    Long: BSONType.LONG.value,
}


def get_bson_type_for(type_hint: Any) -> str | None:
    """
    Determine the BSON type for a given Python type.

    This function attempts to map a Python type to its corresponding BSON type.
    It first checks if the input type is a subclass of any base type in TYPE_MAP.
    If not found, it checks if the type origin is a list.

    Args:
        type_hint (Any): The Python type to be mapped to a BSON type.

    Returns:
        str | None: The corresponding BSON type as a string if a match is found,
                    or None if no matching BSON type is determined.
    """
    for base in TYPE_MAP:
        if type_hint is bool:
            return TYPE_MAP[bool]

        if isinstance(type_hint, type) and issubclass(type_hint, base):
            return TYPE_MAP[base]

    origin = get_origin(type_hint)

    if origin in (list, List):
        return TYPE_MAP.get(list)

    return None
