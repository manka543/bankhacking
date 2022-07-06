import pygame
from random import randint


class Box:
    screen: pygame.surface.Surface
    numberRender: pygame.surface.Surface

    def __init__(self, screen, number, position, fakenumber, colors, shapes):
        self.screen = screen
        self.number = number
        self.position = position
        self.fakeNumber = fakenumber
        self.font = pygame.font.Font('freesansbold.ttf', 120)
        self.numberRender = self.font.render(str(self.number), True, (255, 255, 255))
        self._x = self.position * 300 + 90
        self._y = 150
        self.rect = pygame.rect.Rect(self._x, self._y, 200, 200)
        self.colors2RGB = colors
        self.colors = []
        for keys in colors:
            self.colors.append(keys)
        self.shapes = shapes
        # random elements of box
        self.shape = self.shapes[randint(0, len(self.shapes)-1)]
        self.innerShape = self.shapes[randint(0, len(self.shapes)-1)]
        self.shapeText = self.shapes[randint(0, len(self.shapes)-1)]
        self.colorText = self.colors[randint(0, len(self.colors)-1)]
        self.shapeColor = self.colors[randint(0, len(self.colors)-1)]
        self.innerShapeColor = self.colors[randint(0, len(self.colors)-1)]
        self.colorShapeText = self.colors[randint(0, len(self.colors)-1)]
        self.numberColor = self.colors[randint(0, len(self.colors)-1)]
        self.backgroundColor = self.colors[randint(0, len(self.colors)-1)]
        self.colorColorText = self.colors[randint(0, len(self.colors)-1)]
        print(self.number)

    def __str__(self):
        return f"Box in Position {self.position}\nNumber: {self.number}\nFake number: {self.fakeNumber}\n" \
               f"Shape: {self.shape}\nInner shape: {self.innerShape}\nShape text: {self.shapeText}\n" \
               f"Color text: {self.colorText}\nShape color: {self.shapeColor}\n" \
               f"Inner shape color: {self.innerShapeColor}\nColor shape text: {self.colorShapeText}\n" \
               f"Number color: {self.numberColor}\nBackground color: {self.backgroundColor}\n" \
               f"Color color text: {self.colorColorText}"

    def draw(self, gamephase, countvalueframes=None, countvalue=None):
        if gamephase == "phase1":
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
            if countvalue == 1:
                self.screen.blit(self.numberRender, (self._x + 70, self._y + 45))
            else:
                self.font = pygame.font.Font('freesansbold.ttf', countvalueframes * 2)
                self.numberRender = self.font.render(str(self.number), True, (255, 255, 255))
                self.screen.blit(self.numberRender,
                                 (self._x + 100 - countvalueframes * 0.5, self._y + 105 - countvalueframes))
        elif gamephase == "phase2":
            pygame.draw.rect(self.screen, self.backgroundColor, self.rect)
            pygame.draw.rect(self.screen, (0,0,0), self.rect, 5)
            match self.shape:
                case "rectangle":
                    pass
                case "square":
                    pass
                case "circle":
                    pass
                case "triangle":
                    pass
                case _:
                    pass
            match self.innerShape:
                case "rectangle":
                    pass
                case "square":
                    pass
                case "circle":
                    pass
                case "triangle":
                    pass
                case _:
                    pass
