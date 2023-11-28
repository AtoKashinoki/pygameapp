"""
    Descriptor classes
"""

# import abc
from abc import ABC, abstractmethod


""" Descriptor Basis """


class DescriptorBasis(ABC):
    """
        Descriptor inheritance class

    This class is inheritance class.
    You can use to create Descriptor class.
    """

    def __init__(self, *built_in_types, initial_value: any = None):
        """
            Initialize Descriptor class.

        initial_value argument is not affected by built-in validators.

        :param built_in_types: Built-in validator conditions when assignment a value to a variable.
        :param initial_value: Initial value of variable.
        """
        # assignment values
        self.__built_in_types = built_in_types
        self.__initial_value = initial_value
        return

    @property
    def built_in_types(self) -> tuple:
        """ Return built-in types assigned during self-initialization """
        return self.__built_in_types

    @property
    def initial_value(self) -> any:
        """ Return initial value assigned during self-initialization """
        return self.__initial_value

    @abstractmethod
    def validator(self, value: any) -> None:
        """
            Validator add-on on assignment.
        :param value: Assignment value.
        """
        return

    """ descriptor methods """

    def __set_name__(self, owner, name) -> None:
        """
            Initialize variable.
        """
        # assignment values
        self.__owner = owner
        self.__name = name
        return

    def __set__(self, instance: object, value: any) -> None:
        """
            Set a value to a variable.
        :param value: value to Assignment.
        """
        # validate value
        # Error response function
        def built_in_types_error():
            raise TypeError(f"This value type cannot be assigned: {type(value)}('{value}')")
        #  built-in
        if any in self.__built_in_types:
            ...
        elif value is None:
            if None not in self.__built_in_types:
                built_in_types_error()
        elif type(value) not in self.__built_in_types:
            built_in_types_error()
        #  add-on
        self.validator(value)

        # assignment value
        instance.__dict__[self.__name] = value
        return

    def __get__(self, instance: object, owner) -> built_in_types:
        """
            Get value from variable.
        :return: value to reference
        """
        return instance.__dict__[self.__name]


class Descriptor(DescriptorBasis):
    """
        Descriptor class.

    This class is a regular descriptor without validator add-ons.
    """
    def validator(self, value: any) -> None: ...
