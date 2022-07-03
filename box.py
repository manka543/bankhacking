import pygame


class Box:
    def __init__(self, number, position, fakeNumber):
        self.value = number
        self.position = position
        self.fakeNumber = fakeNumber

        print(self.value)

    def __str__(self):
        return str(self.value)
