"""
    display.Application classes.
"""

# import abc and functools
import abc as _abc
import functools as _functools

# import pygame and numpy
import pygame as _pygame
import numpy as _numpy

# import descriptor
from pgapp.descriptor import (
    Descriptor as _Descriptor,
    DescriptorFramework as _DescriptorFramework,
)

# import attribute validator class
from pgapp.display.type.dict import AttributeValidateDict as _AttributeValidateDict

# import ObjectFramework
from pgapp.display import ObjectFramework as _ObjectFramework

# import attribute key and value class
from pgapp.display import attribute as _attribute


""" Blueprint class """


class Blueprint(_abc.ABC):
    """
        Application blueprint class.

    This is inheritance class.
    Can be used to display surface class blueprint.
    """

    # descriptor
    user_interfaces = _Descriptor(_AttributeValidateDict)
    main_user_interface = _Descriptor(str)
    operations = _Descriptor(dict)

    @_abc.abstractmethod
    def operation_check(self) -> bool:
        """
            Check operation when looping.
        :return: loop stop bool (True: stop <-> False: not stop)
        """
        return False

    @_abc.abstractmethod
    def update(self) -> None:
        """
            Update function.
        """
        return

    def exe(self):
        """
            Execute application.
        """
        return


""" Decorator and Wrapper """


class Decorator:
    """
        Application decorator.

    This class is decorator class.
    Can be used to create surface class.
    """

    def __init__(self):
        """ pass """
        return

    def __call__(self, wrapped_class):
        return _application_wrapper(self, wrapped_class)


def _application_wrapper(instance: Decorator, super_class):
    """
        Generate application class.
    :param instance: Decorator class instance.
    :param super_class: Be wrapped class.
    :return: Wrapped class with ApplicationWrapper.
    """

    @_functools.wraps(super_class, updated=())
    class ApplicationWrapper(super_class, Blueprint):
        """ pass """

        def __init__(self):
            """ pass """
            self.operations = {}
            self.user_interfaces = _AttributeValidateDict(_attribute.values.user_interface)
            self.main_user_interface = ""
            super_class.__init__(self)
            return

        def exe(self):
            # setup values
            clock = self.__setup()

            # loop
            done = False
            while not done:

                # get operations
                self.__get_operations()

                # check operations
                done = (
                    self.__system_special_keys() or
                    super_class.operation_check(self)
                )

                # update
                self.__update()

                # draw
                self.__draw()

                # pass
                clock.tick(self.framerate)
                self.frame_count += 1

                continue

            self.__exit()
            return

        def __setup(self):
            """ pass """
            # pygame initialize
            _pygame.init()

            # display
            # import display config
            import pgapp
            size, caption, icon, framerate = [
                pgapp.display_config[key]
                for key in ["size", "caption", "icon", "framerate"]
            ]
            # initialize
            self.master = _pygame.display.set_mode(size)
            if caption is not None:
                _pygame.display.set_caption(caption)
            if icon is not None:
                _pygame.display.set_icon(icon)
            self.framerate = framerate
            self.frame_count = 0
            return _pygame.time.Clock()

        def __get_operations(self):
            """ pass """
            self.operations = {
                key: value
                for key, value in zip(
                    ["event", "key_pressed", "key_mods", "mouse_pressed", "mouse_pos"],
                    [
                        _pygame.event.get(),
                        _pygame.key.get_pressed(),
                        _pygame.key.get_mods(),
                        _pygame.mouse.get_pressed(),
                        _pygame.mouse.get_pos(),
                    ]
                )
            }
            return

        def operation_check(self) -> bool:
            return super().operation_check()

        def __system_special_keys(self) -> bool:
            """ pass """
            for event in self.operations["event"]:
                if event.type == _pygame.QUIT:
                    return True
            return False

        def update(self) -> None:
            super_class.update(self)
            return

        def __update(self):
            """ pass """
            self.update()
            self.user_interfaces[self.main_user_interface].update(self)
            return

        def __draw(self):
            """ pass """
            self.user_interfaces[self.main_user_interface].draw(self.master)
            _pygame.display.update()
            return

        def __exit(self):
            """ pass """
            return

    return ApplicationWrapper
