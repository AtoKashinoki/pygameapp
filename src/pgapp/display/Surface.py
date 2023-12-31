"""
    display.Surface classes.
"""

# import abc and functools
import abc as _abc
import functools as _functools

# import pygame
import pygame as _pygame

# import descriptor
from pgapp.display.type.descriptor import (
    ImageDescriptor as _ImageDescriptor
)

# import ObjectFramework
from pgapp.display import ObjectFramework as _ObjectFramework

# import attribute key
from pgapp.display import attribute as _attribute


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


class Decorator(_ObjectFramework.DecoratorFramework):
    """
        Surface Decorator.

    This class is decorator class.
    Can be used to create surface class.
    """

    def __call__(self, wrapped_class):
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

            # set attribute
            self.attribute[_attribute.keys.object_type] = _attribute.values.surface

            # execute super class
            super_class.__init__(self, *args, **kwargs)
            return

        def update(self, app_instance, UI_instance) -> None:
            super().update(app_instance, UI_instance)
            return

        def draw(self, master: _pygame.Surface) -> None:
            super().draw(master)
            return

    return SurfaceWrapper
