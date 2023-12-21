import pygame as _pygame

import pgapp
import time
import pygame
import numpy


@pgapp.display.Surface.Decorator(
    [10, 10], [10, 20]
)
class SurfaceTest(pgapp.display.Surface.Blueprint):

    def __init__(self, position):
        self.image.fill("black")
        self.position[:] = position
        return

    def update(self, app_instance, UI_instance) -> None: ...

    def draw(self, master: _pygame.Surface) -> None:
        master.blit(self.image, self.rect)
        return


@pgapp.display.Objects.Decorator()
class ObjectsTest(pgapp.display.Objects.Blueprint):
    def update(self, app_instance, UI_instance) -> None: ...
    def draw(self, master: _pygame.Surface) -> None: ...


if __name__ == '__main__':
    root = pygame.display.set_mode([900, 600])
    objects = ObjectsTest()
    objects.objects["test"] = SurfaceTest([10, 10])
    objects.objects["test2"] = SurfaceTest([880, 570])
    done = False
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
        root.fill("White")
        objects.update("", "")
        objects.draw(root)
        pygame.display.update()
        continue
