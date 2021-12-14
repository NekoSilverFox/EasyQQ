"""
    包含敌机类的相关功能及对象
"""
import random
from plane_sprites import GameSprite, WIDTH, SCREEN_RECT

PATH_ENEMY = "./images/enemy1.png"
MIN_RANDOM_ENEMY = 1
MAX_RANDOM_ENEMY = 3

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时制定敌机图片
        super().__init__(PATH_ENEMY)
        # 制定敌机随机速度
        self.speed = random.randint(MIN_RANDOM_ENEMY, MAX_RANDOM_ENEMY)
        self.rect.bottom = 0
        # 制定敌机随机位置
        self.rect.x = random.randint(0, WIDTH - self.rect.width)

    def update(self):
        """更新敌机位置"""
        # 调用父类方法，保持垂直飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机销毁 " + self.rect.__str__())