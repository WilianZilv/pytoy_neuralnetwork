from neuralnetwork import NeuralNetwork
from tkinter import *
import random

class Player:
    pos_x = 100
    pos_y = 390
    vel_y = 0

    def __init__(self, root, brain, obstacle):

        self.dead = False
        self.jumps = 0
        self.time_alive = 0
        self.brain = brain
        self.player = Frame(root, width=10, height=10, bg=self.random_color())
        self.obstacle = obstacle

        #self.pos_x += random.gauss(0, 1) * 20

    @staticmethod
    def random_color():
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def physics(self):

        if self.dead is True:
            return

        self.time_alive += 1

        if self.pos_y < 390:
            self.vel_y += .5
        elif self.pos_y > 390:
            self.vel_y = 0;
            self.pos_y = 390

        self.pos_y += self.vel_y

        self.player.place(x=self.pos_x, y=self.pos_y)

        inputs = []
        inputs.append(self.vel_y / 100)
        inputs.append((self.obstacle.pos_x - self.pos_x) / 500)
        inputs.append((self.obstacle.pos_y - self.pos_y) / 500)
        inputs.append(self.obstacle.vel_x / 100)

        outputs = self.brain.predict(inputs)

        if outputs[0] > .75:
            self.jump()

        if self.pos_x + 10 >= self.obstacle.pos_x and self.pos_x <= self.obstacle.pos_x + 25:
            if self.pos_y + 10 >= self.obstacle.pos_y:
                self.die()
                return

        if self.pos_y < 0:
            self.die()

    def get_fitness(self):
        return self.time_alive

    def jump(self):

        #if self.pos_y >= 390:
        self.vel_y -= 8
        self.jumps += 1

    def die(self):
        self.player.destroy()
        self.dead = True

