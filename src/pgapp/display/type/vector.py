"""
    Vector data classes use in display
"""

# import numpy
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
    int, float,
    _numpy.int_, _numpy.int8, _numpy.int16, _numpy.int32, _numpy.int64, _numpy.intc, _numpy.intp,
    _numpy.uint, _numpy.uint8, _numpy.uint32, _numpy.uint64, _numpy.uintc, _numpy.uintp,
    _numpy.float_, _numpy.float32, _numpy.float64,
    _numpy.cfloat, _numpy.clongfloat, _numpy.longfloat,
    tuple, list, _numpy.ndarray,
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
            data_type=_numpy.int64,
            **kwargs,
    ):
        """
            Create vector instance.
        :param initial_value: Initial vector.
        :param data_type: Vector data type.
        """
        self = super().__new__(cls, [len(initial_value)], data_type)
        return self

    def __init__(
            self,
            initial_value: tuple[int | float] | list[int | float] | _numpy.ndarray,
            data_type=_numpy.int64,
    ):
        """
            Initialize value value.
        :param initial_value: Initial vector.
        :param data_type: Vector data type.
        """
        self[0:len(initial_value)] = _numpy.array(initial_value, dtype=data_type)
        return

    def validator(self, key: str | int | tuple, value: any) -> None:
        if type(key) is not slice:
            _built_in_validate_function(value, (
                int, float,
                _numpy.int_, _numpy.int8, _numpy.int16, _numpy.int32, _numpy.int64, _numpy.intc, _numpy.intp,
                _numpy.uint, _numpy.uint8, _numpy.uint32, _numpy.uint64, _numpy.uintc, _numpy.uintp,
                _numpy.float_, _numpy.float32, _numpy.float64,
                _numpy.cfloat, _numpy.clongfloat, _numpy.longfloat,
            ))
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
            data_type=_numpy.int64,
            **kwargs,
    ):
        """
            Create Vec2 instance.
        :param initial_value: Initial vector.
        :param data_type: Vector data type.
        """
        self = super().__new__(cls, [0, 0], data_type=data_type)
        return self


""" in object class """


class Position(Vec2):
    """
        Position vec2 class.

    This class manage object position Vec2.
    """

    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = float(self[0] + value)
        return

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = float(self[1] + value)
        return


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
