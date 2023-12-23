import pygame as _pygame

import pgapp
import time
import pygame
import numpy


@pgapp.display.Application.Decorator()
class AppTest(pgapp.display.Application.Blueprint):
    def __init__(self):
        self.user_interfaces["test"] = UITest()
        self.main_user_interface = "test"
        return

    def operation_check(self) -> bool: return False
    def update(self) -> None: ...


@pgapp.display.UserInterface.Decorator("white")
class UITest(pgapp.display.UserInterface.Blueprint):
    def __init__(self):
        self.objects["test"] = ObjectsTest()
        return

    def update(self, app_instance: AppTest) -> None: ...
    def draw(self, master: _pygame.Surface) -> None: ...


@pgapp.display.Objects.Decorator()
class ObjectsTest(pgapp.display.Objects.Blueprint):
    def __init__(self):
        self.objects["test"] = SurfaceTest()
        return

    def update(self, app_instance: AppTest, UI_instance: UITest) -> None: ...
    def draw(self, master: _pygame.Surface) -> None: ...


@pgapp.display.Surface.Decorator(
    [10, 10], [10, 20]
)
class SurfaceTest(pgapp.display.Surface.Blueprint):

    def __init__(self, position=None):
        self.image.fill("black")
        if position is not None:
            self.position[:] = position
        return

    def update(self, app_instance: AppTest, UI_instance: UITest) -> None:
        print(app_instance, UI_instance)
        self.position[:] = numpy.array(self.position + [0.5, 0.5], dtype=numpy.float64)
        return

    def draw(self, master: _pygame.Surface) -> None:
        master.blit(self.image, self.rect)
        return


if __name__ == '__main__':
    app = AppTest()
    app.exe()
