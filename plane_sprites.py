"""
    1. 封装游戏中所有需要使用的精灵子类
    2. 提供游戏的 相关工具
"""
import pygame

WIDTH = 480
HEIGHT = 700
SCREEN_RECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
FRAME_PER_SEC = 60  # 每秒刷新帧率
CREATE_ENEMY_EVENT = pygame.USEREVENT  # 敌机的定时器常量
PATH_HERO = "./images/me1.png"


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def update(self):
        """更新位置"""

    def set_info(self):
        """更新信息"""
