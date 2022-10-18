"""
Created on 2022-08-30 15:12
@author: wateryear
"""
import tkinter as tk
from tkinter import messagebox as msgbox

from GameTimer import GameTimer
from Intro_game import Intro_game
from life_game import LifeGame

class GameMap(object):
    # 窗口元素
    rect = None
    # 用于处理逻辑
    Life = LifeGame()
    # 用于呈现信息
    Intro = Intro_game()


    '''
        初始化：
        格子大小；
        演进速度
    '''
    def __init__(self):
        self.win = tk.Tk()
        X, Y = self.win.maxsize()
        W, H = 1024, 800
        winPos = f'{W}x{H}+{(X - W) // 2}+{(Y - H) // 2}'
        self.win.geometry(winPos)
        self.win.resizable(False, False)
        self.win.title('生命游戏 Ver1.0')
        self.win.update()

    # 点击点时：
    def on_Click(self,event):
        x, y = (event.x - 40) // 20, (event.y - 40) // 20
        if not self.Life.running:
            if self.Life.items[x + 1][y + 1]:
                self.tv.itemconfig(self.rect[x][y], fill='DeepSkyBlue', outline='DeepSkyBlue')
            else:
                self.tv.itemconfig(self.rect[x][y], fill='Yellow', outline='Yellow')
            self.Life.items[x + 1][y + 1] = not self.Life.items[x + 1][y + 1]

        pass

    # 绘制游戏map效果
    def drawCanvas(self):
        self.tv = tk.Canvas(self.win, width=self.win.winfo_width(), height=self.win.winfo_height())
        self.tv.pack(side="top")
        for i in range(36):
            coord = 40, 40, 760, i * 20 + 40
            self.tv.create_rectangle(coord)
            coord = 40, 40, i * 20 + 40, 760
            self.tv.create_rectangle(coord)

        coord = 38, 38, 760, 760
        self.tv.create_rectangle(coord, width=2)
        coord = 39, 39, 760, 760
        self.tv.create_rectangle(coord, width=2)
        coord = 38, 38, 762, 762
        self.tv.create_rectangle(coord, width=2)
        R, XY = 8, [50 + i * 20 for i in range(36)]
        self.rect = [[0] * 36 for _ in range(36)]
        for i, x in enumerate(XY):
            for j, y in enumerate(XY):
                self.rect[i][j] = self.tv.create_rectangle(x - R, y - R, x + R, y + R, tags=('imgButton1'))
                self.tv.itemconfig(self.rect[i][j], fill='DeepSkyBlue', outline='DeepSkyBlue')
        self.tv.tag_bind('imgButton1', '<Button-1>', self.on_Click)

    def drawLifes(self):
        R, XY = 8, [50 + i * 20 for i in range(36)]
        if self.Life.running:
            for i, x in enumerate(XY):
                for j, y in enumerate(XY):
                    if self.Life.items[i + 1][j + 1]:
                        self.tv.itemconfig(self.rect[i][j], fill='Orange', outline='Orange')
                    else:
                        self.tv.itemconfig(self.rect[i][j], fill='DeepSkyBlue', outline='DeepSkyBlue')
            self.tv.update()
            self.Life.reproduce()
            if self.Life.is_stable():
                self.Life.running = False
                if sum(sum(self.Life.items, [])):
                    msgbox.showinfo('Message', self.Intro.end_point(isStable=True))
                else:
                    msgbox.showinfo('Message', self.Intro.end_point(isStable=False))
        self.win.after(self.Life.runningSpeed, self.drawLifes)

    # 开始游戏按钮
    def StartLife(self):
        if sum(sum(self.Life.items, [])):
            self.Life.histroy = []
            self.Life.running = True
        else:
            msgbox.showinfo('Message', self.Intro.StartLife_Info())
    # 暂停按钮
    def BreakLife(self):
        self.Life.running = not self.Life.running
        if self.Life.running:
            self.Life.histroy.clear()
            self.Life.add_histroy()

    # 随机按钮
    def RandomLife(self):
        self.Life.rndinit()
        self.Life.running = True

    # 清空
    def ClearLife(self):
        self.Life.running = False
        self.Life.histroy = []
        self.Life.items = [[0] * 38 for _ in range(38)]
        for x in range(36):
            for y in range(36):
                self.tv.itemconfig(self.rect[x][y], fill='DeepSkyBlue', outline='DeepSkyBlue')

    # 退出游戏时
    def on_Close(self):
        if msgbox.askokcancel("Quit", "Do you want to quit?"):
            self.Life.running = False
            print(self.Intro.Copyright())
            self.win.destroy()

    def show(self):
        tLabel = tk.Label(self.win, width=30, height=20, background='lightgray')
        tLabel.place(x=780, y=38)
        tLabel.config(text='\n\n\n'.join((self.Intro.Introduce(), self.Intro.Copyright())))
        tLabel.config(justify=tk.LEFT, anchor="nw", borderwidth=10, wraplength=210)

        bX, bY, dY = 835, 458, 50
        # 生命开始
        tButton0 = tk.Button(self.win, text=u'开始', command=self.StartLife)
        tButton0.place(x=bX, y=bY + dY * 0, width=120, height=40)
        # 生命暂停
        tButton1 = tk.Button(self.win, text=u'暂停', command=self.BreakLife)
        tButton1.place(x=bX, y=bY + dY * 1, width=120, height=40)
        # 随机开始
        tButton2 = tk.Button(self.win, text=u'随机', command=self.RandomLife)
        tButton2.place(x=bX, y=bY + dY * 2, width=120, height=40)
        # 清空
        tButton3 = tk.Button(self.win, text=u'清空', command=self.ClearLife)
        tButton3.place(x=bX, y=bY + dY * 3, width=120, height=40)

        self.win.protocol("WM_DELETE_WINDOW", self.on_Close)
        self.win.mainloop()
