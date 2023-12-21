"""
    display.ObjectFramework classes.
"""

# import abc
import abc as _abc

# import pygame and numpy
import pygame as _pygame
import numpy as _numpy

# import descriptor
from pgapp.descriptor import Descriptor as _Descriptor

# import display.type
from pgapp.display.type.vector import (
    Position as _Position,
    Size as _Size,
)
from pgapp.display.type.dict import (
    Attribute as _Attribute,
)


""" Object framework class """


class Blueprint(_abc.ABC):
    """
        Object framework class.

    This class is inheritance class.
    Can be used to display ObjectFramework class blueprint.
    """

    # descriptor
    position: _Position = _Descriptor(_Position)
    size: _Size = _Descriptor(_Size)
    attribute: _Attribute = _Descriptor(_Attribute)

    @property
    def rect(self):
        """ Get self rect """
        return _pygame.Rect((*self.position, *self.size))

    @_abc.abstractmethod
    def update(self, app_instance, UI_instance) -> None:
        """
            Update function.
        :param app_instance: Application class instance.
        :param UI_instance: UI class instance.
        """
        return

    @_abc.abstractmethod
    def draw(self, master: _pygame.Surface) -> None:
        """ pass """
        return


class Framework(Blueprint, _abc.ABC):
    """
        Object framework class.

    This class is inheritance class.
    Can be used to create display object classes.
    """

    def __init__(
            self,
            initial_position: list[int | float] | tuple[int | float] | _numpy.ndarray[int | float] = (0, 0),
            initial_size: list[int] | tuple[int] | _numpy.ndarray[int] = (0, 0),
            initial_attribute: dict = None,
            size_validate_mode: str = "N"
    ):
        """
            Initialize values.
        :param initial_position: Object position.
        :param initial_size: Object size.
        :param initial_attribute: Object attributes.
        :param size_validate_mode: Object size class mode.
        """
        self.position = _Position(initial_position, data_type=_numpy.float64)
        self.size = _Size(initial_size, mode=size_validate_mode)
        self.attribute = _Attribute(
            dict() if initial_attribute is None else initial_attribute
        )
        return


""" decorator framework class """


class DecoratorFramework(_abc.ABC):
    """
        Decorator framework class.

    This class is inheritance class.
    Can be used to create display object classes.
    """

    def __init__(
            self,
            initial_position:
            list[int | float] | tuple[int | float] | _numpy.ndarray[int | float]
            = (0, 0),
            initial_size: list[int] | tuple[int] | _numpy.ndarray[int] = (0, 0),
            initial_attribute: dict = None,
            size_validate_mode: str = "N",
    ):
        """
            Set wrapper class instance values.
        :param initial_position: Object position.
        :param initial_size: Object size.
        :param initial_attribute: Object attributes.
        :param size_validate_mode: Object size class mode.
        """
        self.wrapper_args = (initial_position, initial_size, initial_attribute, size_validate_mode)
        return

    @_abc.abstractmethod
    def __call__(self, wrapped_class):
        """
            Wrap surface classes with surface rappers.
        :param wrapped_class: Class to wrap with SurfaceWrapper.
        :return: Wrapped class with SurfaceWrapper.
        """
        return
