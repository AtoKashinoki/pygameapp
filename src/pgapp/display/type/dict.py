"""
    dict type classes
"""


# import descriptors
from pgapp.descriptor import (
    Descriptor as _Descriptor,
    ContainerValidateDecorator as _ContainerValidateDecorator,
    ContainerValidatorBlueprint as _ContainerValidatorBlueprint,
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
