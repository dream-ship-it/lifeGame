"""
Created on 2022-08-30 15:14
@author: wateryear
"""
import random

from GameTimer import GameTimer


class LifeGame(object):

    # 用于调节时间间隔
    game_T = GameTimer(100)

    def __init__(self, rows=38, cols=38):
        self.row = rows
        self.col = cols
        self.items = [[0] * self.col for _ in range(self.row)]
        self.histroy = []
        self.histroySize = 30
        self.running = False
        self.runningSpeed = self.game_T.interval

    def rndinit(self, rate=0.1):
        self.histroy = []
        for i in range(self.row):
            for j in range(self.col):
                rnd = random.random()
                if rnd > 1 - rate:
                    self.items[i][j] = 1

    def reproduce(self):
        new = [[0] * self.col for _ in range(self.row)]
        self.add_histroy()
        if len(self.histroy) > self.histroySize:
            self.histroy.pop(0)
        for i in range(self.row):
            for j in range(self.col):
                if i * j == 0 or i == self.row - 1 or j == self.col - 1:
                    new[i][j] = 0
                else:
                    lifes = 0
                    for m in range(i - 1, i + 2):
                        for n in range(j - 1, j + 2):
                            if m == i and n == j:
                                continue
                            lifes += self.items[m][n]
                    if self.items[i][j]:
                        if lifes == 2 or lifes == 3:
                            new[i][j] = 1
                        else:
                            new[i][j] = 0
                    else:
                        if lifes == 3:
                            new[i][j] = 1
        for idx, narray in enumerate(new):
            self.items[idx] = narray

    def is_stable(self):
        if len(self.histroy) < self.histroySize:
            return False
        arr = []
        for i in self.histroy:
            if i not in arr:
                arr.append(i)
        if len(arr) < 10:
            return True

    def add_histroy(self, Items = None):
        arr = []
        if Items == None:
            Items = self.items[:]
        for item in Items:
            b = 0
            for i, n in enumerate(item[::-1]):
                b += n * 2 ** i
            arr.append(b)
        self.histroy.append(arr)

