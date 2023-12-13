import pygame as _pygame

import pgapp
import time
import numpy


class testObject(pgapp.display.Surface.Blueprint):

    def update(self, app_instance, UI_instance) -> None: ...
    def draw(self, master: _pygame.Surface) -> None: ...


if __name__ == '__main__':
    obj = testObject()
    print(obj.position, obj.size, obj.attribute)
