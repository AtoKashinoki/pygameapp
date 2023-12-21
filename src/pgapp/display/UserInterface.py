"""
    display.UserInterface classes.
"""

# import abc and functools
import abc as _abc
import functools as _functools

# import pygame and numpy
import pygame as _pygame
import numpy as _numpy

# import descriptor
from pgapp.descriptor import Descriptor as _Descriptor

# import attribute validator class
from pgapp.display.type.dict import (
    Attribute as _Attribute,
    AttributeValidateDict as _AttributeValidateDict
)

# import Objects
from pgapp.display import Objects as _Objects

# import ObjectFramework
from pgapp.display import ObjectFramework as _ObjectFramework

# import attribute key
from pgapp.display import attribute as _attribute


""" Blueprint class """


class Blueprint(_Objects.Blueprint, _abc.ABC):
    """
        User interface blueprint class.

    This is inheritance class.
    Can be used to display surface class blueprint.
    """

    # descriptor

    @_abc.abstractmethod
    def update(self, app_instance) -> None: ...

""" Decorator and Rapper """


class Decorator:
    """
        User interface decorator.

    This class is decorator class.
    Can be used to create UseInterface class.
    """

    def __init__(
            self,
            background_color: str | list[int] | tuple[int] | _numpy.ndarray[int] = "black",
            initial_attribute: dict = None
    ):
        """ pass """
        self.wrapper_args = (background_color, initial_attribute)
        return

    def __call__(self, wrapped_class):
        return _user_interface_wrapper(self, wrapped_class)


def _user_interface_wrapper(instance: Decorator, super_class):
    """
        Generate UserInterface class.
    :param instance: Decorator class instance.
    :param super_class: Be wrapped class.
    :return: Wrapped class with UserInterfaceWrapper.
    """

    @_functools.wraps(super_class, updated=())
    class UserInterfaceWrapper(super_class, Blueprint):
        """
            pass
        """

        def __init__(self, *args, **kwargs):
            """
                Initialize value and execute super class initializer.
            :param args: Initializer args.
            :param kwargs: Initializer key word args.
            """
            # initial value
            background_color, initial_attribute = instance.wrapper_args
            self.background_color = background_color
            self.attribute = _Attribute(
                dict() if initial_attribute is None else initial_attribute
            )
            self.objects = _AttributeValidateDict()

            # set attribute
            self.attribute[_attribute.keys.object_type] = _attribute.values.user_interface

            # execute super class
            super_class.__init__(self, *args, **kwargs)
            return

        def update(self, app_instance) -> None:
            super().update(app_instance)
            for key, value in self.objects.items():
                value.update(app_instance, self)
            return

        def draw(self, master: _pygame.Surface) -> None:
            master.fill(self.background_color)
            super().draw(master)
            for key, value in self.objects.items():
                value.draw(master)
            return

    return UserInterfaceWrapper
