"""
    dict type classes
"""


# import descriptors
from pgapp.descriptor import (
    Descriptor as _Descriptor,
    ContainerValidateDecorator as _ContainerValidateDecorator,
    ContainerValidatorBlueprint as _ContainerValidatorBlueprint,
)

# import attribute keys and values
from pgapp.display.attribute import (
    keys as _keys, values as _values,
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


@_ContainerValidateDecorator(any, built_in_validate_key_types=(str, tuple))
class AttributeValidateDict(dict, _ContainerValidatorBlueprint):
    """
        Validate attribute dictionary class.

    This class manage pgapp display classes.
    """

    def validator(self, key: str | int | tuple, value: any) -> None:
        try:
            if value.attribute[_keys.object_type] not in [_values.objects, _values.surface]:
                raise AttributeError
        except AttributeError:
            raise TypeError(f"pass")
        return
