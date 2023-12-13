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


class ObjectFramework(_abc.ABC):
    """
        Object framework class.

    This class is inheritance class.
    Can be used to create display object classes.
    """

    # descriptor
    position = _Descriptor(_Position)
    size = _Descriptor(_Size)
    attribute = _Descriptor(_Attribute)

    def __init__(
            self,
            initial_position: list[int | float] | tuple[int | float] | _numpy.ndarray[int | float] = (0, 0),
            initial_size: list[int] | tuple[int] | _numpy.ndarray[int] = (0, 0),
            initial_attribute: dict = None,
            size_validate_mode: str = "N"
    ):
        """
            Initialize values.
        :param initial_position:
        :param initial_size:
        :param initial_attribute:
        :param size_validate_mode:
        """
        self.position = _Position(initial_position)
        self.size = _Size(initial_size, mode=size_validate_mode)
        self.attribute = _Attribute(
            dict() if initial_attribute is None else initial_attribute
        )
        return

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
