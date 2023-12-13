"""
    display.Surface classes.
"""

# import abc
import abc as _abc

import pygame as _pygame

# import descriptor
from pgapp.display.type.descriptor import (
    ImageDescriptor as _ImageDescriptor
)

# import ObjectFramework
from pgapp.display.ObjectFramework import (
    ObjectFramework as _ObjectFramework
)


""" Blueprint class """


class Blueprint(_ObjectFramework, _abc.ABC):
    """
        Surface blueprint class.

    This is inheritance class.
    Can be used to display surface class blueprint.
    """


""" Decorator and Rapper """


class Decorator:
    """
        Surface Decorator.

    This class is decorator class.
    Can be used to create surface class.
    """

    # descriptor

    def __init__(self, *args, **kwargs):
        """ pass """
        return

    def __call__(self, super_class):
        """ pass """
        return _surface_rapper(self, super_class)


def _surface_rapper(instance: Decorator, super_class):
    """ pass """

    class Surface(super_class, Blueprint):
        """
            Surface class.

        Return from _surface_rapper function.
        """

        def __init__(self, *args, **kwargs):
            """pass"""
            super().__init__(*args, **kwargs)
            return

        def update(self, app_instance, UI_instance) -> None:
            super().update(app_instance, UI_instance)
            return

        def draw(self, master: _pygame.Surface) -> None:
            return

    return Surface
