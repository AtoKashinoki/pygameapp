"""
    display.Objects classes.
"""

# import abc and functools
import abc as _abc
import functools as _functools

# import pygame
import pygame as _pygame

# import descriptor
from pgapp.descriptor import Descriptor as _Descriptor

# import attribute validator class
from pgapp.display.type.dict import AttributeValidateDict as _AttributeValidateDict

# import ObjectFramework
from pgapp.display import ObjectFramework as _ObjectFramework

# import attribute key and value class
from pgapp.display import attribute as _attribute


""" Blueprint class """


class Blueprint(_ObjectFramework.Blueprint, _abc.ABC):
    """
        Objects blueprint class.

    This is inheritance class.
    Can be used to display surface class blueprint.
    """

    # descriptor
    objects = _Descriptor(_AttributeValidateDict)


""" Decorator and Wrapper """


class Decorator(_ObjectFramework.DecoratorFramework):
    """
        Objects decorator.

    This class is decorator class.
    Can be used to create surface class.
    """

    def __call__(self, wrapped_class):
        return _objects_wrapper(self, wrapped_class)


def _objects_wrapper(instance: Decorator, super_class):
    """
        Generate objects class.
    :param instance: Decorator class instance.
    :param super_class: Be wrapped class.
    :return: Wrapped class with ObjectWrapper.
    """

    @_functools.wraps(super_class, updated=())
    class ObjectsWrapper(super_class, _ObjectFramework.Framework, Blueprint):
        """
            Object class.

        Return from _object_wrapper function.
        """

        def __init__(self, *args, **kwargs):
            """
                Initialize value and execute super class initializer.
            :param args: Initializer args.
            :param kwargs: Initializer key word args.
            """
            # initial value
            _ObjectFramework.Framework.__init__(
                self, *instance.wrapper_args
            )
            self.objects = _AttributeValidateDict(_attribute.values.objects, _attribute.values.surface)

            # set attribute
            self.attribute[_attribute.keys.object_type] = _attribute.values.objects

            # execute super class
            super_class.__init__(self, *args, **kwargs)
            return

        def update(self, app_instance, UI_instance) -> None:
            super().update(app_instance, UI_instance)
            for key, value in self.objects.items():
                value.update(app_instance, UI_instance)
            return

        def draw(self, master: _pygame.Surface) -> None:
            super().draw(master)
            for key, value in self.objects.items():
                value.draw(master)
            return

    return ObjectsWrapper
