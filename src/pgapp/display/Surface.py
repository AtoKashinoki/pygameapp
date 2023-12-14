"""
    display.Surface classes.
"""

# import abc and functools
import abc as _abc
import functools as _functools

# import pygame and numpy
import pygame as _pygame
import numpy as _numpy

# import descriptor
from pgapp.display.type.descriptor import (
    ImageDescriptor as _ImageDescriptor
)

# import ObjectFramework
from pgapp.display import ObjectFramework as _ObjectFramework


""" Blueprint class """


class Blueprint(_ObjectFramework.Blueprint, _abc.ABC):
    """
        Surface blueprint class.

    This is inheritance class.
    Can be used to display surface class blueprint.
    """

    # descriptor
    image: _pygame.Surface = _ImageDescriptor(_pygame.Surface)


""" Decorator and Rapper """


class Decorator:
    """
        Surface Decorator.

    This class is decorator class.
    Can be used to create surface class.
    """

    # descriptor

    def __init__(
            self,
            initial_position:
            list[int | float, int | float] | tuple[int | float, int | float] | _numpy.ndarray[int | float, int | float]
            = (0, 0),
            initial_size: list[int, int] | tuple[int, int] | _numpy.ndarray[int, int] = (0, 0),
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

    def __call__(self, wrapped_class):
        """
            Wrap surface classes with surface rappers.
        :param wrapped_class: Class to wrap with SurfaceWrapper.
        :return: Wrapped class with SurfaceWrapper.
        """
        return _surface_wrapper(self, wrapped_class)


def _surface_wrapper(instance: Decorator, super_class):
    """
        Generate surface class.
    :param instance: Decorator class instance.
    :param super_class: Be wrapped class.
    :return: Wrapped class with SurfaceWrapper.
    """

    @_functools.wraps(super_class, updated=())
    class SurfaceWrapper(super_class, _ObjectFramework.Framework, Blueprint):
        """
            Surface class.

        Return from _surface_rapper function.
        """

        def __init__(self, *args, **kwargs):
            """
                Initialize values and execute super class initializer.
            :param args: Initializer args.
            :param kwargs: Initializer key word args.
            """
            # initial value
            _ObjectFramework.Framework.__init__(
                self, *instance.wrapper_args
            )
            self.image = _pygame.Surface(instance.wrapper_args[1])

            # execute super class
            super().__init__(*args, **kwargs)
            return

        def update(self, app_instance, UI_instance) -> None:
            # pass
            super().update(app_instance, UI_instance)
            return

        def draw(self, master: _pygame.Surface) -> None:
            super().draw(master)
            return

    return SurfaceWrapper
