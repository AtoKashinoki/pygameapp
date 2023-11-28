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


""" print self name and version """
name = "pgapp"
version = pkg_resources.get_distribution(name).version
print(f"{name} {version}")
