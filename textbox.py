import pygame


class TextBox:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.active = False
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.text = ""
        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.textRender = self.renderText()

    def draw(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect, border_radius=3)
        self.surface.blit(self.textRender,(self.x + 10, self.y + 10))

    def renderText(self):
        return self.font.render(self.text, True, (0, 0, 0))

    def service(self, key):
        if self.active:
            if key == pygame.K_BACKSPACE:
                if len(self.text) > 0:
                    self.text = self.text[:-1]
            else:
                self.text += key.unicode
                self.textRender = self.renderText()
