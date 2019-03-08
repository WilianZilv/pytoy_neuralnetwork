from tkinter import *
from player import Player
from obstacle import Obstacle


class Main:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x400')
        self.root['bg'] = 'black'

        self.txt_generation = 0
        self.g_label = Label(self.root, text='Generation: 0')
        self.f_label = Label(self.root, text='Best fitness: 0')

        self.g_label.grid(row=0, column=0)
        self.f_label.grid(row=1, column=0)

        Button(self.root, text='Force Next Generation', command=self.force_next_generation).place(x=200, y=0)

        self.obstacle = Obstacle(self.root)

        self.players = []
        self.next_generation(None)

        self.fixed_update()

        self.root.mainloop()

    def fixed_update(self):

        all_dead = True

        for p in self.players:
            p.physics()

            if p.dead is False:
                all_dead = False

        if all_dead is True:
            self.next_generation(self.best_player().brain)
            self.obstacle.reset()

        self.obstacle.physics()

        self.root.after(16, self.fixed_update)

    def force_next_generation(self):
        self.next_generation(self.best_player().brain)

    def next_generation(self, brain):

        self.txt_generation += 1

        self.g_label.config(text=f'Generation: {self.txt_generation}')

        for p in self.players:
            p.player.destroy()

        self.players = []

        for i in range(250):
            player = Player(self.root, brain, self.obstacle)
            player.brain.mutate()
            self.players.append(player)

        self.obstacle.reset()

    def best_player(self):
        best = self.players[0]
        for p in self.players:
            if p.get_fitness() > best.get_fitness():
                best = p

        self.f_label.config(text=f'Best fitness: {best.get_fitness()}')

        return best


Main()