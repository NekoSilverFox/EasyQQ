"""
游戏背景
"""

from plane_main import GameSprite
from plane_main import SCREEN_RECT
PATH_BACKGROUND = "./images/background.png"


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法，完成精灵的基本属性设置
        super().__init__(PATH_BACKGROUND)
        # 判断是否为交替图像，如果是，设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        """更新图像"""
        # 调用父类方法实现
        super().update()

        # 判断图像是否移出屏幕，如果移出，重新设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

    def change_background(self, background):
        """改变游戏背景"""
