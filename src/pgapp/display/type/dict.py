"""
    dict type classes
"""


# import descriptors
from pgapp.descriptor import (
    ContainerValidateDecorator as _ContainerValidateDecorator,
    ContainerValidatorBlueprint as _ContainerValidatorBlueprint,
)

# import attribute keys and values
from pgapp.display.attribute import (
    keys as _keys
)


""" dict type classes """


@_ContainerValidateDecorator(
    any, built_in_validate_key_types=[str],
    initial_assignment=True
)
class Attribute(dict, _ContainerValidatorBlueprint):
    """
        Attribute dict class

    This class manage attributes class.
    """

    def validator(self, key: str | int | tuple, value: any) -> None: ...


@_ContainerValidateDecorator(
    any, built_in_validate_key_types=(str, tuple),
    initial_assignment=True
)
class AttributeValidateDict(dict, _ContainerValidatorBlueprint):
    """
        Validate attribute dictionary class.

    This class manage pgapp display classes.
    """

    def __init__(self, *value_types):
        """ pass """
        self.__value_types = value_types
        super().__init__()
        return

    def validator(self, key: str | int | tuple, value: any) -> None:
        try:
            if value.attribute[_keys.object_type] not in self.__value_types:
                raise AttributeError
        except AttributeError:
            raise TypeError(f"pass")
        return
