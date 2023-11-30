"""
    pgapp
This module can be used to create pygame application
"""

# import support modules
import os
import glob
import pkg_resources

# import main modules
import pygame
import numpy

# import self modules
from pgapp.descriptor import Descriptor as _Descriptor
from pgapp import config


""" print self name and version """
name = "pgapp"
version = pkg_resources.get_distribution(name).version
print(f"{name} {version}")


class __InitializePygameApp:
    """
        Initialize PygameApp class.

    Can be used to initialize about PygameApp.
    """

    # descriptor
    system_config = _Descriptor(config.Config, dict)

    # initial config data
    initial_system_config = {"config_directory_path": "config"}
    initial_display_config = {}

    def __init__(self):
        """ initialize values """
        # system config
        try:
            self.system_config = config.Config(file_path="config/system.config")
        except FileNotFoundError:
            self.system_config = dict()

    """ check config directory condition """

    def initialize_configs(self) -> None:
        """
            Initialize configs
        """
        # config directory
        if not glob.glob("config"):
            os.mkdir("config")

        # system config
        system_config_path = f"config/system.config"
        if not glob.glob(system_config_path):
            config.write_config(system_config_path, self.initial_system_config)
            self.system_config = config.Config(file_path="config/system.config")

        # display config
        display_config_path = f"{self.system_config['config_directory_path']}/display.config"
        if not glob.glob(display_config_path):
            config.write_config(display_config_path, self.initial_system_config)

        return


if __name__ == name:
    _init_pgapp = __InitializePygameApp()
    _init_pgapp.initialize_configs()
