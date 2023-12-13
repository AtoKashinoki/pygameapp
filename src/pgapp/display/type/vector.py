"""
    Vector data classes use in display
"""

# import pygame and numpy
import pygame as _pygame
import numpy as _numpy

# import descriptor
from pgapp.descriptor import (
    built_in_validate_function as _built_in_validate_function,
    Descriptor as _Descriptor,
    ValidatorBlueprint as _ValidatorBlueprint,
    ContainerValidatorBlueprint as _ContainerValidatorBlueprint,
    ContainerValidateDecorator as _ContainerValidateDecorator,
)


""" Vector classes """


@_ContainerValidateDecorator(
    int, float, tuple, list, _numpy.ndarray,
    initial_assignment=True
)
class Vector(_numpy.ndarray, _ContainerValidatorBlueprint):
    """
        Vector management class.

    This class manage vector.
    """

    def __new__(
            cls,
            initial_value: tuple[int | float] | list[int | float] | _numpy.ndarray,
            *args,
            **kwargs,
    ):
        """
            Create vector instance.
        :param initial_value: initial vector.
        """
        self = super().__new__(cls, [len(initial_value)], _numpy.int64)
        return self

    def __init__(
            self,
            initial_value: tuple[int | float] | list[int | float] | _numpy.ndarray,
    ):
        """
            Initialize value value.
        :param initial_value: initial vector.
        """
        self[0:len(initial_value)] = initial_value
        return

    def validator(self, key: str | int | tuple, value: any) -> None:
        if type(key) is not slice:
            _built_in_validate_function(value, (int, float))
        return

    def __repr__(self):
        return f"{self}"


class Vec2(Vector):
    """
        Vec2 management class.

    This class manage Vec2.
    """

    def __new__(
            cls,
            initial_value: tuple[int | float] | list[int | float] | _numpy.ndarray,
            *args,
            **kwargs,
    ):
        """
            Create Vec2 instance.
        :param initial_value: initial vec2.
        """
        self = super().__new__(cls, [0, 0])
        return self


""" in object class """


class Position(Vec2):
    """
        Position vec2 class.

    This class manage object position Vec2.
    """


class Size(Vec2):
    """
        Size vec2 class.

    This class manage object image size.
    """
    __validate = True

    def __init__(self, *args, mode: str = "N"):
        """ Initialize value """
        self.__validate = False
        self.__mode = mode
        super().__init__(*args)
        return

    def validator(self, key: str | int | tuple, value: any) -> None:
        if self.__mode == "V" and self.__validate is True:
            raise TypeError()
        self.__validate = True
        return

    def _disable_validator_(self):
        """
            Disable validator function.
        """
        self.__validate = False
        return
