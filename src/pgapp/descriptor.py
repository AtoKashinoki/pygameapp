"""
    Descriptor classes
"""

# import abc
from abc import ABC as _ABC, abstractmethod as _abstractmethod


""" validate function """


def _built_in_validate_function(checking: any, validate_condition: tuple[any]) -> None:
    """
        Built-in validate.
    :param checking: data to validate.
    :param validate_condition: validate conditions.
    """
    # Error response function
    def built_in_validate_error() -> None:
        raise TypeError(f"This value type cannot be assigned: {type(checking)}('{checking}')")

    # validate
    if any in validate_condition:
        ...
    elif checking is None:
        if None not in validate_condition:
            built_in_validate_error()
    elif type(checking) not in validate_condition:
        built_in_validate_error()
    return


""" Descriptor framework """


class DescriptorFramework(_ABC):
    """
        Descriptor framework class

    This class is inheritance class.
    Can be used to create descriptor class.
    """

    def __init__(self, *built_in_validate, initial_value: any = None):
        """
            Initialize descriptor class.

        initial_value argument is not affected by built-in validators.

        :param built_in_validate: Built-in validator conditions when assignment a value to a variable.
        :param initial_value: Initial value of variable.
        """
        # assignment values
        self.__built_in_validate = built_in_validate
        self.__initial_value = initial_value
        return

    @property
    def built_in_validate(self) -> tuple:
        """ Return built-in validator conditions assigned during self-initialization """
        return self.__built_in_validate

    @property
    def initial_value(self) -> any:
        """ Return initial value assigned during self-initialization """
        return self.__initial_value

    @_abstractmethod
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
        # built-in
        _built_in_validate_function(value, self.__built_in_validate)

        #  add-on
        self.validator(value)

        # assignment value
        instance.__dict__[self.__name] = value
        return

    def __get__(self, instance: object, owner):
        """
            Get value from variable.
        :return: value to reference.
        """
        return instance.__dict__[self.__name]


class Descriptor(DescriptorFramework):
    """
        Descriptor class.

    This class is a regular descriptor without validator add-ons.
    """

    def validator(self, value: any) -> None: ...


""" Validator framework """


class ValidatorFramework(_ABC):
    """
        Validator class framework.

    This class is inheritance class.
    Can be used to create a framework for validator classes.
    """
    @_abstractmethod
    def validator(self, key: str | int | tuple, value: any) -> None:
        """
            Validator add-on on assignment.
        :param key: Assignment key.
        :param value: Assignment value.
        """
        return


""" Container validator wrapper """


class _tupleValidator(tuple):
    ...


class _ContainerValidatorDescriptors(_ABC):
    """
        Container validator class's descriptor
    """
    # descriptor
    built_in_validate_value_types = Descriptor(_tupleValidator)
    built_in_validate_key_types = Descriptor(_tupleValidator)

    @_abstractmethod
    def __setitem__(self, key, value): ...


def _get_ContainerValidator(instance, container):
    """
        Returns the validator class inherited from the container class.
    :param instance: Decorator class instance.
    :param container: Container class to inherit from validator class.
    :return: Validator class inherited from container class.
    """

    class ContainerValidator(container, _ContainerValidatorDescriptors):
        """
            Container validate class

        This class is inheritance class.
        Return class from _get_ContainerValidator function.
        """

        def __init__(self, *args):
            """
                Initialize validate conditions and container class.
            :param args: Initial container class key and values.
            """
            # import copy
            from copy import copy

            # get validate conditions
            self.built_in_validate_value_types = copy(instance.validate_value_types)
            self.built_in_validate_key_types = copy(instance.validate_key_types)

            # initialize container
            if instance.initial_assignment[0]:
                container.__init__(self, *args)
            else:
                if not len(args) == 0:
                    raise TypeError(f"Initial assignment rejection: initial_assignment = False")
                container.__init__(self)

            return

        def __setitem__(self, key: str | int | tuple, value: any) -> None:
            """
                Validate key and value.
            :param key: container key.
            :param value: container value.
            """

            # validator
            #  built-in
            [
                _built_in_validate_function(*args)
                for args in zip(
                    [key, value], [self.built_in_validate_key_types, self.built_in_validate_value_types]
                )
            ]

            # add-on
            self.validator(key, value)

            # assignment key and value
            super().__setitem__(key, value)
            return

    return ContainerValidator


class ContainerValidateDecorator:
    """
        Container validate decorator class.

    This class is decorator class.
    Can be to use to create Container validate class.
    """
    # descriptor
    validate_value_types: Descriptor(_tupleValidator)
    validate_key_types: Descriptor(_tupleValidator)
    initial_assignment: Descriptor(_tupleValidator)

    def __init__(
            self,
            *built_in_validate_value_types,
            built_in_validate_key_types: tuple | list = (any, ),
            initial_assignment: bool = False
    ):
        """
            initialize decorator
        :param built_in_validate_value_types: Built-in validator conditions when assignment a value to a container.
        :param built_in_validate_key_types: Built-in validator conditions when assignment a key to a container.
        """
        # initialize values
        self.validate_value_types = _tupleValidator(built_in_validate_value_types)
        self.validate_key_types = _tupleValidator(built_in_validate_key_types)
        self.initial_assignment = _tupleValidator((initial_assignment, ))
        return

    def __call__(
            self, container: tuple | list | dict | set | object
    ) -> type[tuple | list | dict | set | object | _ContainerValidatorDescriptors]:
        """
            Wrap container classes with validators.
        :param container: Container class wrapped in a validator.
        :return: Container class wrapped in validator.
        """
        return _get_ContainerValidator(self, container)
