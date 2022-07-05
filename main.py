import pygame
from random import shuffle
import box
import textbox
import button
import json


def numberGenerator():
    numbers = [1, 2, 3, 4]
    shuffle(numbers)
    for i in range(4):
        yield numbers.pop(0)


class Game:
    def __init__(self):
        # First
        pygame.init()
        with open("config.json") as file:
            self.config = json.load(file)
            print(self.config)
        self.screen = pygame.display.set_mode((1275, 760))
        # order doesn't care
        self.running = True
        self.fps = 60
        self.startBtn = button.Button(self.screen, (485, 300), (300, 160), 72, "START",
                                      self.config["color"]["startButton"]["normal"],
                                      self.config["color"]["startButton"]["hover"],
                                      self.config["color"]["startButton"]["pressed"])
        self.textBox = textbox.TextBox(self.screen, 500, 400, 200, 70)
        self.font72 = pygame.font.Font('freesansbold.ttf', 72)
        self.numberRenders = {1: self.font72.render("1", True, (255, 255, 255)),
                              2: self.font72.render("2", True, (255, 255, 255)),
                              3: self.font72.render("3", True, (255, 255, 255)),
                              4: self.font72.render("4", True, (255, 255, 255))}
        self.gamePhase = "start"
        self.countValue = 3
        self.countValueFrames = 60
        # TODO: Ten mechanizm losowania może nie działać ale narazie nie sprawdzam
        realNumberGenerator = numberGenerator()
        fakeNumberGenerator = numberGenerator()
        self.numberBoxes = [box.Box(self.screen, next(realNumberGenerator), 0, next(fakeNumberGenerator)),
                            box.Box(self.screen, next(realNumberGenerator), 1, next(fakeNumberGenerator)),
                            box.Box(self.screen, next(realNumberGenerator), 2, next(fakeNumberGenerator)),
                            box.Box(self.screen, next(realNumberGenerator), 3, next(fakeNumberGenerator))]
        # Last
        print(self.numberBoxes)
        pygame.display.set_caption("BANK HACKING GAME")
        self.clock = pygame.time.Clock()
        self.game_loop()

    def graphic(self):
        self.screen.fill(self.config["color"]["bgColor"])
        if self.gamePhase == "start":
            self.startBtn.draw(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3)[0])
        elif self.gamePhase == "counting down":
            self.screen.blit(self.numberRenders[self.countValue], (650, 300))
        elif self.gamePhase == "phase1":
            for i in self.numberBoxes:
                i.draw(self.countValueFrames, self.countValue)

        pygame.display.update()

    def countDown(self):
        self.countValueFrames -= 1
        if self.countValueFrames == 0:
            self.countValue -= 1
            self.countValueFrames = 60
        if self.countValue == 0:
            if self.gamePhase == "counting down":
                self.gamePhase = "phase1"
                self.countValueFrames = 60
                self.countValue = 1
            elif self.gamePhase == "phase1" and self.countValueFrames == 1:
                self.gamePhase = "phase2"

    def logic(self):
        if self.gamePhase == "start":
            if self.startBtn.isClicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3)[0]):
                self.gamePhase = "counting down"
        elif self.gamePhase == "counting down" or self.gamePhase == "phase1":
            self.countDown()
        elif self.gamePhase == "phase2":
            pass

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.textBox.service(event)
            self.logic()
            self.graphic()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
