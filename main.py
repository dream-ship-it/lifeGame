
from game_map import GameMap

# 主程序用于运行
class Main(object):
    if __name__ == '__main__':
        newGame = GameMap()
        newGame.drawCanvas()
        newGame.drawLifes()
        # 开始展示
        newGame.show()
