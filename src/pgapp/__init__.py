"""
    pgapp
This module can be used to create pygame application
"""

# import support modules
import os
import glob as _glob
import pkg_resources

# import self modules
from pgapp.descriptor import Descriptor as _Descriptor
from pgapp import (
    config,
    display,
)


""" print self name and version """
name = "pgapp"
version = pkg_resources.get_distribution(name).version
print(f"{name} {version}")


class __InitializePygameApp:
    """
        Initialize PygameApp class.

    Can be used to initialize about PygameApp.
    """
    # data type classes
    class FilePath(str):
        """
            File path class
        """
        mode = "w"

        def __init__(self, path: str):
            """
                Validate path.
            :param path: file path str to assign
            """
            if not _glob.glob(path) and self.mode != "i":
                raise FileNotFoundError(f"Not found file -> file path: {path}")
            __class__.mode = "w"
            return

    # descriptor
    system_config = _Descriptor(config.Config)
    display_config_path = _Descriptor(FilePath)

    # initial config data
    initial_system_config = {"''": "pgapp system configs", "config_directory_path": "config"}
    initial_display_config = {"''": "display configs"}

    def __init__(self):
        """ initialize values """
        # system config
        try:
            self.system_config = config.Config(file_path="config/system.config")
        except FileNotFoundError:
            ...
        self.initialize_configs()
        return

    """ check config directory condition """

    def initialize_configs(self) -> None:
        """
            Initialize configs
        """
        # config directory
        if not _glob.glob("config"):
            os.mkdir("config")

        # system config
        system_config_path = f"config/system.config"
        if not _glob.glob(system_config_path):
            config.write_config(system_config_path, self.initial_system_config)
            self.system_config = config.Config(file_path="config/system.config")

        # display config
        self.FilePath.mode = "i"
        self.display_config_path = self.FilePath(
            f"{self.system_config['config_directory_path']}/display.config"
        )
        if not _glob.glob(self.display_config_path):
            config.write_config(self.display_config_path, self.initial_display_config)

        return


if __name__ == name:
    _init_pgapp = __InitializePygameApp()
    display_config = config.Config(file_path=_init_pgapp.display_config_path)
