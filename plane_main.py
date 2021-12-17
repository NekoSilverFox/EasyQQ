"""
游戏主程序
    1. 封装 主游戏类
    2. 创建 游戏对象
    3. 启动游戏
"""
import sys
import pygame
import background
from plane_sprites import SCREEN_RECT, FRAME_PER_SEC
from enemy import *
from plane_sprites import *
from hero import *


class PlaneGame:
    """用于配置及初始化游戏内容"""
    def __init__(self):
        """初始化"""
        print("游戏初始化...")

        print("设置游戏窗口中...")
        self.__screen = pygame.display.set_mode(SCREEN_RECT.size)

        print("创建游戏时钟中...")
        self.__clock = pygame.time.Clock()

        print("调用私有方法，创建精灵和精灵组...")
        self.__creat_sprites()

    def start_game(self):
        """开始游戏"""
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.__clock.tick(FRAME_PER_SEC)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新/绘制精灵
            self.__update_sprites()

            # 更新显示
            pygame.display.update()

    @property.setter
    def __screen(self, wide, height):
        """屏幕"""

    @property.setter
    def __clock(self, time):
        """游戏时钟"""

    def __creat_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    @classmethod
    def __event_handler(cls):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()  # 使用类名的方式调用静态方法
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()
                # 敌机精灵添加到敌机组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     self.hero.rect.x += 1 这种方法，只能检测按下
            # 应该使用键盘模块，可以按下键盘一直不放
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies =  pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) != 0:
            # 英雄牺牲
            self.hero.kill()
            # 结束游戏
            self.__game_over()

    def __update_sprites(self):
        """更新精灵组"""
        self.back_group.update()
        self.back_group.draw(self.__screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.__screen)

        self.hero_group.update()
        self.hero_group.draw(self.__screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.__screen)

    @staticmethod
    def __game_over():
        """游戏结束"""
        print("游戏结束...")
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
