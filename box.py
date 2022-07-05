import pygame


class Box:
    screen: pygame.surface.Surface
    numberRender: pygame.surface.Surface

    def __init__(self, screen, number, position, fakenumber):
        self.screen = screen
        self.number = number
        self.position = position
        self.fakeNumber = fakenumber
        self.font = pygame.font.Font('freesansbold.ttf', 120)
        self.numberRender = self.font.render(str(self.number), True, (255, 255, 255))
        self._x = self.position * 300 + 150
        self._y = 150
        self.rect = pygame.rect.Rect(self._x, self._y, 200, 200)
        print(self.number)

    def __str__(self):
        return str(self.number)

    def draw(self, countvalueframes, countvalue):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        if countvalue == 1:
            self.screen.blit(self.numberRender, (self._x + 70, self._y + 45))
            print(1)
        else:
            print(0)
            self.font = pygame.font.Font('freesansbold.ttf', countvalueframes * 2)
            self.numberRender = self.font.render(str(self.number), True, (255, 255, 255))
            self.screen.blit(self.numberRender, (self._x + 100 - countvalueframes*0.5, self._y + 105 - countvalueframes))
