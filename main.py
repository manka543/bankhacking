import pygame
import box
import textbox
import button


class Game:
    def __init__(self):
        # First
        pygame.init()
        self.screen = pygame.display.set_mode((1275, 760))
        # order doesn't care
        self.running = True
        self.fps = 60
        self.startBtn = button.Button(self.screen, (485, 300), (300, 160), 72, "START")
        self.textBox = textbox.TextBox()
        self.gamePhase = "start"
        # Last
        pygame.display.set_caption("BANK HACKING GAME")
        self.clock = pygame.time.Clock()
        self.game_loop()
        self.box = box.Box()

    def graphic(self):
        self.screen.fill((32, 40, 46))
        if self.gamePhase == "start":
            self.startBtn.draw(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3)[0])
        pygame.display.update()

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    pass
            if self.gamePhase == "start":
                if self.startBtn.isClicked(pygame.mouse.get_pos(), pygame.mouse.get_pressed(3)[0]):
                    self.gamePhase = "counting down"

            self.graphic()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
