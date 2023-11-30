"""
    config classes
"""

# import descriptor
from pgapp.descriptor import (
    Descriptor as _Descriptor,
    ContainerValidateDecorator as _ContainerValidateDecorator,
    ValidatorFramework as _ValidatorFramework,
    built_in_validate_function as _built_in_validate_function,
    ContainerValidatorDescriptors as _ContainerValidatorDescriptors,
)


""" Validator """


@_ContainerValidateDecorator(
    str, int, float, bool, None,
    initial_assignment=True
)
class ConfigTuple(tuple, _ContainerValidatorDescriptors):
    """
        Config tuple validator.

    This is tuple class for config.
    """
    def __init__(self, *args):
        """
            Assignment tuple object.
        :param args: tuple to assign.
        """
        for arg in args[0]:
            _built_in_validate_function(arg, self.built_in_validate_value_types)
        return

    def __setitem__(self, key, value): ...
    def validator(self, key: int, value: any) -> None: ...


""" Config class """


def write_config(file_path: str, config_dict: dict) -> None:
    """
        Write config file.
    :param file_path: config file to write.
    :param config_dict: config data.
    """
    # write config file
    with open(file=file_path, mode="w", encoding="utf-8") as write_file:
        [
            print(f"{key}: {value}", file=write_file)
            for key, value in config_dict.items()
        ]
    return


@_ContainerValidateDecorator(str, int, float, bool, tuple, None)
class Config(dict, _ValidatorFramework):
    """
        Config management class.

    Can be used to get config datas from config file.
    """
    # import re
    import re as __re

    # data type
    class __FilePath(str):
        ...
    # descriptor
    file_path = _Descriptor(__FilePath)

    def __init__(self, file_path: str):
        """
            Read config file and assign config data in dict.
        :param file_path: Config file path to read.
        """
        # initialize values
        self.file_path = self.__FilePath(file_path)

        # read config file
        self.read()

        # initialize dict
        super().__init__()
        return

    def validator(self, key: str | int | tuple, value: any) -> None: ...

    def read(self) -> None:
        """
            Read config file.
        """
        # change type from str
        def change_type(value: str, indent: int = 0) -> str | int | float | bool | ConfigTuple:
            """
                Change type from str.
            :param value: value to change type.
            :param indent: tuple indent.
            """
            return_value = [
                float(value) if self.__re.match(r"^\d+\.\d*$", value) else
                int(value) if self.__re.match(r"^\d+$", value) else
                bool(value) if self.__re.match(r"^(True|False)$", value) else
                ConfigTuple(
                    [
                        change_type(value_in_tuple, indent=indent+1)
                        for value_in_tuple in self.__re.findall(
                            f"(\([^)]+\)|[^,]+)[,)]",
                            value.replace(" ", "")[1:]
                        )
                        if not value_in_tuple == ""
                    ]
                ) if self.__re.match(r"^\(.+\)$", value) and indent < 1 else
                None if self.__re.match(r"None", value) else
                self.__re.sub(r"[\"']", "", value)
            ][0]
            return return_value

        # Read and create config dict
        with open(file=self.file_path, mode="r", encoding="utf-8") as config_file:
            config_dict = dict([
                [key, change_type(value)]
                for line in config_file.readlines()
                for key, value in [
                    line
                    .replace(": ", ":")
                    .replace(":", ": ")
                    .replace("\n", "")
                    .split(": ")
                ]
            ])

            # update config
            super().__init__(config_dict)
        return

    def write(self) -> None:
        write_config(self.file_path, self)
        return

    def __setitem__(self, key, value) -> None:
        """
            Validate config tuple.
        :param key: key to assign in config data.
        :param value: value to assign in config data.
        """
        if type(value) is tuple:
            value = ConfigTuple(value)
        super().__setitem__(key, value)
        self.write()
        return
