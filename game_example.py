from tkinter import *
from example.player import Player
from example.obstacle import Obstacle
from example.coin import Coin
import random
from neuralnetwork import NeuralNetwork

class Main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x400')
        self.root['bg'] = 'black'

        self.txt_generation = 0
        self.g_label = Label(self.root, text='Generation: 0')
        self.f_label = Label(self.root, text='Best fitness: 0')
        self.p_label = Label(self.root, text='Population: 0')

        self.g_label.grid(row=0, column=0)
        self.f_label.grid(row=1, column=0)
        self.p_label.grid(row=2, column=0)

        Button(text='Next Generation', command=self.force_next_generation).grid(row=0, column=2)

        self.obstacle = Obstacle(self.root)
        self.coin = Coin(self.root)

        self.best = None
        self.players = []
        self.next_generation(None)

        self.fixed_update()

        self.root.mainloop()

    def fixed_update(self):

        all_dead = True

        population = 0
        for p in self.players:
            p.physics()
            
            if p.dead is False:
                population += 1
                all_dead = False

        self.update_population(population)

        if all_dead is True:
            self.next_generation(self.best_player().brain)
            self.obstacle.reset()

        self.obstacle.physics()
        self.coin.physics()

        self.root.after(16, self.fixed_update)

    def force_next_generation(self):
        self.next_generation(self.best_player().brain)

    def next_generation(self, brain):

        self.txt_generation += 1

        self.g_label.config(text=f'Generation: {self.txt_generation}')

        for p in self.players:
            p.player.destroy()

        self.players = []

        for i in range(150):

            new_brain = NeuralNetwork(8, 3, 1)

            if brain is not None:
                new_brain = NeuralNetwork.copy_from(brain)

            player = Player(self.root, new_brain, self.obstacle, self.coin)
            new_brain.mutate()
            self.players.append(player)

            print('\nBrain Clone:')
            print(f'W_IH: {new_brain.weights_ih.data}')
            print(f'W_HO: {new_brain.weights_ho.data}')
            print(f'B_H: {new_brain.bias_h.data}')
            print(f'B_O: {new_brain.bias_o.data}')

        self.coin.reset()
        self.obstacle.reset()

    def best_player(self):
        best = self.players[0]
        for p in self.players:
            if p.get_fitness() > best.get_fitness():
                best = p

        if self.best is None:
            self.best = best

        if best.get_fitness() > self.best.get_fitness():
            self.best = best

        self.f_label.config(text=f'Best fitness: {self.best.get_fitness()}')

        return best

    def update_population(self, amt):
        self.p_label.config(text=f'Population: {amt}')

Main()
