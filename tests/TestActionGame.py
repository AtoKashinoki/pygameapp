"""

    Action game program.

"""
# import sys
import sys

# import pygame and pgapp
import pygame
import pygame as _pygame

import pgapp

# import numpy
import numpy


""" charactor """


@pgapp.display.Surface.Decorator(initial_size=[20, 20])
class Charactor(pgapp.display.Surface.Blueprint):
    """ Charactor object """

    def __init__(self):
        """ Initialize values """
        self.image.fill([127, 127, 127])
        self.position[:] = [100, 450]
        self.movement = [0, 0]
        self.jump_count = 0
        return

    def update(self, app_instance, UI_instance) -> None:
        self.control(app_instance)
        self.side_move(UI_instance)
        self.gravity(UI_instance)
        return

    def control(self, app_instance):
        self.movement[0] = 0
        key = app_instance.operations["key_pressed"]
        events = app_instance.operations["event"]
        for event in events:
            if event.type == pygame.KEYDOWN and self.jump_count <= 0 and key[pygame.K_UP]:
                self.jump_count += 1
                self.movement[1] = -10
        if key[pygame.K_LEFT]:
            self.movement[0] += -5
        if key[pygame.K_RIGHT]:
            self.movement[0] += 5
        return

    def gravity(self, UI_instance):
        self.movement[1] += 0.5
        self.position[1] += self.movement[1]
        for field_rect in UI_instance.objects["stage"].objects.keys():
            if self.coll(field_rect):
                self.position[1] = field_rect[1] - self.size[1]
                self.movement[1] = 0
                self.jump_count = 0
            continue
        return

    def side_move(self, UI_instance):
        self.position[0] += self.movement[0]
        for field_rect in UI_instance.objects["stage"].objects.keys():
            if self.coll(field_rect):
                if self.movement[0] >= 0:
                    self.position[0] = field_rect[0] - self.size[0]
                else:
                    self.position[0] = field_rect[0] + field_rect[2]
                self.movement[0] = 0
            continue
        return

    def coll(self, field_rect):
        if self.side_coll(field_rect):
            if self.top_bottom_coll(field_rect):
                return True
        return False

    def side_coll(self, field_rect):
        char_sides = [self.position[0], self.position[0] + self.size[1]]
        if not char_sides[0] < field_rect[0] + field_rect[2]:
            return False
        if not char_sides[1] > field_rect[0]:
            return False
        return True

    def top_bottom_coll(self, field_rect):
        if not self.position[1] < field_rect[1] + field_rect[2]:
            return False
        if not self.position[1] + self.size[1] > field_rect[1]:
            return False
        return True

    def draw(self, master: _pygame.Surface) -> None:
        master.blit(self.image, self.rect)
        return


""" stage objects """


@pgapp.display.Surface.Decorator()
class Rect(pgapp.display.Surface.Blueprint):
    """ Rect field class """

    def __init__(self, rect: tuple[int, int, int, int] | numpy.ndarray):
        """ Initialize values """
        self.position[:] = rect[:2]
        self.image = pygame.Surface(rect[2:])
        self.image.fill("black")
        return

    def update(self, app_instance, UI_instance) -> None: ...

    def draw(self, master: pygame.Surface) -> None:
        master.blit(self.image, self.rect)
        return


@pgapp.display.Objects.Decorator()
class Stage(pgapp.display.Objects.Blueprint):
    """ Stage object classes """

    # initialize field
    field_rects = [
        (50, 0, 800, 40),
        (500, -40, 40, 40),
    ]

    def __init__(self):
        """ Initialize field classes """
        diff = numpy.array([0, 500, 0, 0])
        for rect in self.field_rects:
            rect = rect + diff
            self.objects[tuple(rect)] = Rect(rect)
        return

    def update(self, app_instance, UI_instance) -> None: ...
    def draw(self, master: pygame.Surface) -> None: ...


""" action UI """


@pgapp.display.UserInterface.Decorator("white")
class Action(pgapp.display.UserInterface.Blueprint):
    """ UI about action """

    def __init__(self):
        """ Initialize values about action game """
        self.objects["stage"] = Stage()
        self.objects["charactor"] = Charactor()
        return

    def update(self, app_instance) -> None: ...
    def draw(self, master: pygame.Surface) -> None: ...


""" Application """


@pgapp.display.Application.Decorator()
class ActionGame(pgapp.display.Application.Blueprint):
    """ Action game application class """

    def __init__(self):
        """ Initialize action game app values """
        self.user_interfaces["action"] = Action()
        self.main_user_interface = "action"
        return

    def update(self) -> None:
        return

    def operation_check(self) -> bool:
        return False


""" execute process """

if __name__ == '__main__':
    app = ActionGame()
    app.exe()
    sys.exit()

