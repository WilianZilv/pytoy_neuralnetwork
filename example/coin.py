from tkinter import *
import random


class Coin:
    pos_x = 520
    pos_y = 350
    vel_x = -5

    def __init__(self, root):

        self.player = Frame(root, width=20, height=20, bg='yellow')

    def physics(self):
        self.player.place(x=self.pos_x, y=self.pos_y)

        if self.pos_x < -20:
            self.reset()

        self.pos_x += self.vel_x

    def reset(self):
        self.pos_x = 520
        self.pos_y = random.randrange(50, 350)
        self.vel_x = random.randrange(-8, -5)