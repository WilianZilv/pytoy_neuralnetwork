from neuralnetwork import NeuralNetwork
from tkinter import *
import random

class Player:
    pos_x = 100
    pos_y = 200
    vel_y = 0

    def __init__(self, root, brain, obstacle, coin):

        self.root = root
        self.dead = False
        self.time_to_collect = 0
        self.can_collect_coin = True
        self.coins = 0
        self.jumps = 0
        self.time_alive = 0
        self.brain = brain
        self.player = Frame(root, width=10, height=10, bg=self.random_color())
        self.obstacle = obstacle
        self.coin = coin

        #self.pos_x += random.gauss(0, 1) * 20

    @staticmethod
    def random_color():
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def physics(self):

        if self.dead is True:
            return

        self.time_alive += .01
        self.time_to_collect += 1
        self.vel_y += .5

        self.pos_y += self.vel_y

        self.player.place(x=self.pos_x, y=self.pos_y)

        inputs = []
        inputs.append(self.pos_y / 400)
        inputs.append(self.vel_y / 100)

        inputs.append(self.obstacle.pos_x / 500)
        inputs.append(self.obstacle.pos_y / 400)
        inputs.append(self.obstacle.vel_x / 100)

        inputs.append(self.coin.pos_x / 500)
        inputs.append(self.coin.pos_y / 400)
        inputs.append(self.coin.vel_x / 100)

        outputs = self.brain.predict(inputs)

        if outputs[0] > .5:
            self.jump()

        coin_hit = False
        if self.pos_x + 10 >= self.coin.pos_x and self.pos_x <= self.coin.pos_x + 20:
            if self.pos_y + 10 >= self.coin.pos_y and self.pos_y <= self.coin.pos_y + 20:
                coin_hit = True

        if coin_hit is True:
            self.time_to_collect = 0
            self.can_collect_coin = False
            self.coins += 1
            coin_label = Label(text='+1 COIN', bg='black', fg='yellow')
            coin_label.place(x=self.pos_x, y=self.pos_y - 10)
            self.root.after(1000, coin_label.destroy)
        else:
            self.can_collect_coin = True

        if self.pos_x + 10 >= self.obstacle.pos_x and self.pos_x <= self.obstacle.pos_x + 25:
            if self.pos_y + 10 >= self.obstacle.pos_y:
                self.die()
                return

        if self.time_to_collect >= 500:
            self.die()

        if self.pos_y < 0 or self.pos_y > 400:
            self.die()

    def get_fitness(self):
        return (self.coins + 1) * self.time_alive

    def jump(self):

        #if self.pos_y >= 390:
        self.vel_y -= 8
        self.jumps += 1

    def die(self):
        self.player.destroy()
        self.dead = True

