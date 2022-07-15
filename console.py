import pygame
import json


class Console:
    screen: pygame.surface.Surface

    def __init__(self, screen, x, y, width, height, font_size, background, textcolor):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fontSize = font_size
        self.font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        self.background = background
        self.textColor = textcolor
        with open("comands.json") as file:
            self.commands = json.load(file)
        self.systemRender = self.font.render('system>>', True, self.textColor)
        self.text = ["ale oro na"]
        self.textRenders = []
        self.currentLine = 0
        self.renderLines()
        self.cursor = pygame.rect.Rect(0, 0, self.fontSize / 5, self.fontSize)
        print(self.systemRender.get_size())

    def writeLine(self, line):
        if self.currentLine + 1 > len(self.text):
            self.text.append(line)
        else:
            self.text[self.currentLine] = line
        self.renderLines()

    def makeCommand(self, line):
        if line == "hack":
            print("hack")
        elif line == "update":
            pass
        self.currentLine += 1
        self.writeLine(" ")

    def renderLines(self):
        self.textRenders = []
        for i in range(len(self.text)):
            self.textRenders.append(self.font.render(self.text[i], True, self.textColor))

    def service(self, event):
        if event.key == pygame.K_BACKSPACE:
            if len(self.text[self.currentLine]) > 0:
                self.text[self.currentLine] = self.text[self.currentLine][:-1]
                self.renderLines()
        elif event.key == pygame.K_RETURN:
            self.makeCommand(self.text[self.currentLine])
        elif event.unicode.isprintable():
            self.text[self.currentLine] += event.unicode
            self.renderLines()
        return "nextPhase"

    def draw(self, tics):
        pygame.draw.rect(self.screen, self.background, (self.x, self.y, self.width, self.height), 5, 20)
        for i in range(len(self.textRenders)):
            self.screen.blit(self.systemRender, (self.x + 20, self.y + 20 + i * (self.fontSize + 2)))
            self.screen.blit(self.textRenders[i], (self.x + 20 + 115, self.y + 20 + i * (self.fontSize + 2)))
        self.cursor.x, self.cursor.y = self.textRenders[
                                           self.currentLine].get_width() + self.x + 137, self.y + 18 + self.currentLine * (
                                               self.fontSize + 2)
        if round(tics / 1000) % 2 == 0:
            pygame.draw.rect(self.screen, self.textColor, self.cursor)