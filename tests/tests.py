import pgapp
import time
import pygame
import numpy


@pgapp.display.Surface.Decorator(
    initial_position=(10, 20), initial_size=(30, 40), initial_attribute={"Itest": "Itest"}
)
class testObject(pgapp.display.Surface.Blueprint):

    def __init__(self, *args, **kwargs):
        self.attribute["test"] = "test"
        self.image.fill("white")
        speed = 0.1
        self.movement = numpy.array([1., 1.]) * speed
        return

    def update(self, app_instance, UI_instance) -> None:
        now = time.time()
        for i, d in enumerate([600, 400]):
            if d <= self.position[i] + self.size[i] or 0 >= self.position[i]:
                self.movement[i] = -self.movement[i]
                continue
            continue
        self.position += self.movement
        print(self.position)
        return

    def draw(self, master: pygame.Surface) -> None:
        master.blit(self.image, self.rect)
        return


if __name__ == '__main__':
    obj = testObject()
    root = pygame.display.set_mode([600, 400])
    done = False
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
        obj.update("app", "UI")
        root.fill("black")
        obj.draw(root)
        pygame.display.update()
        continue
    print(obj.position, obj.size, obj.attribute)
