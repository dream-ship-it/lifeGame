"""
Created on 2022-09-05 18:08
@author: wateryear
"""

class Intro_game:
    def __init__(self):
        pass

    def Introduce(self):
        txt = '''【生命游戏】\n\n生存定律：\
        (1)当前细胞为湮灭状态时，当周围有３个存活细胞时，则迭代后该细胞变成存活状态(模拟繁殖)。\
        (2)当前细胞为存活状态时，当周围的邻居细胞少于２个存活时，该细胞变成湮灭状态(数量稀少)。\
        (3)当前细胞为存活状态时，当周围有３个以上的存活细胞时，该细胞变成湮灭状态(数量过多)。\
        (4)当前细胞为存活状态时，当周围有２个或３个存活细胞时，该细胞保持原样。'''
        return txt

    def Copyright(self):
        return 'Written by 杨一鸣&王美帅, 2022/09/02.'

    def StartLife_Info(self):
        return '请点击小方块填入生命细胞，或者使用随机功能！'

    def Quit(self):
        return '你确定想要退出吗？'

    def end_point(self, isStable):
        if isStable== True:
            return '生命繁殖与湮灭进入稳定状态！！！'
        else:
            return '生命全部湮灭，进入死亡状态！！！'