import pygame


class Button:
    def __init__(self, screen, position, size, textsize, caption):
        self.rect = pygame.rect.Rect(position, size)
        self.color = (44, 70, 94)
        self.colorMouse = (24, 50, 74)
        self.colorClick = (64, 90, 114)
        self.font = pygame.font.Font('freesansbold.ttf', textsize)
        self.text = self.font.render(caption, True, (255, 255, 255))
        self.screen = screen

    def draw(self, mousepos, isclicked):
        if self.rect.collidepoint(mousepos) and isclicked:
            pygame.draw.rect(self.screen, self.colorClick, self.rect)
        elif self.rect.collidepoint(mousepos):
            pygame.draw.rect(self.screen, self.colorMouse, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.text, (self.rect.x + 30, self.rect.y + 50))

    def isClicked(self, mousepos, isclicked):
        if self.rect.collidepoint(mousepos) and isclicked:
            return True
        return False
