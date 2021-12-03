<p align="center">
 <img width="100px" src="https://github.com/NekoSilverFox/EasyQQ/blob/main/docs/pic/logo.svg" align="center" alt="EasyQQ" />
 <h1 align="center">飞机大战</h2>
 <p align="center">玩得开心！</p>
</p>

<div align=center>

[![CodeQL](https://github.com/NekoSilverFox/EasyQQ/actions/workflows/codeql-analysis.yml/badge.svg?branch=main)]
[![Pylint CI](https://github.com/NekoSilverFox/EasyQQ/actions/workflows/pylint.yml/badge.svg)](https://github.com/NekoSilverFox/EasyQQ/actions/workflows/pylint.yml)

[![License](https://img.shields.io/badge/license-Apache%202.0-brightgreen)](LICENSE)
![project](https://img.shields.io/badge/project-SPbSTU-green)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
[![pygame](https://img.shields.io/badge/pygame-pygame%20v2-orange)](https://www.pygame.org/news)

<p align="center">
    <a href="../README.md">Русский язык</a>
</p>

<div align=left>

## 开发者

- NekoSilverfox (Peter the Great St.Petersburg Polytechnic University)
- liyijiadou2020 (Peter the Great St.Petersburg Polytechnic University)
- Miracle-Milk (Keimyung University)



## 简介

玩家可以通过控制自己的飞机并与敌机进行对战！



## 工具

- Git - 分布式版本控制
- GitHub - 代码仓库
- PyCharm - 软件开发及测试
- CI/CD - 持续集成
- Pylink - 自动化代码测试，保证代码风格统一且遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 风格
- Drawio - 流程图绘制



## 游戏背景

* 游戏启动后，**背景图像** 会 **连续不断地** **向下方** 移动
* 在 **视觉上** 产生英雄的飞机不断向上方飞行的 **错觉**
  * **游戏的背景** 不断变化
  * **游戏的主角** 位置保持不变



## 开发流程

1. 项目理解及简单说明

   - 把一些 **静止的图像** 绘制到 **游戏窗口** 中
   - 根据 **用户的交互** 或其他情况，**移动** 这些图像，产生动画效果
   - 根据 **图像之间** 是否发生重叠，判断 **敌机是否被摧毁** 等其他情况

2. 游戏框架搭建

   - 明确主程序职责
   - 实现主程序类
   - 准备游戏精灵组

3. 使用 `pygame` 创建图形窗口

   - 游戏的初始化和退出

   - 理解游戏中的坐标系

   - 创建游戏主窗口

   - 简单的游戏循环

     | 游戏初始化       | 游戏循环         |
     | ---------------- | ---------------- |
     | 设置游戏窗口     | 设置刷新率       |
     | 绘制图像初始位置 | 检测用户交互     |
     | 设置游戏时钟     | 更新所有图像位置 |
     |                  | 更新屏幕显示     |

4. 英雄的简单动画实现

   - 记录英雄的初始位置
   - 在 **游戏循环** 中每次让 **英雄** 的 `y - 1` —— 向上移动 
   - `y <= 0` 将英雄移动到屏幕的底部
   - 需求：
     - 游戏启动后，**英雄** 出现在屏幕的 **水平中间** 位置，距离 **屏幕底部** `120` **像素**
     - **英雄** 每隔 `0.5` 秒发射一次子弹，每次 **连发三枚子弹**
     - **英雄** 默认不会移动，需要通过 **左/右** 方向键，控制 **英雄** 在水平方向移动

5. 在游戏循环中监听事件 

   - **捕获** 用户具体的操作，并且针对性的做出响应

6. 精灵 和 精灵组

   - **精灵** 需要 有 **两个重要的属性**
     * `image` 要显示的图像
     * `rect` 图像要显示在屏幕的位置
   - 精灵组，一个 **精灵组** 可以包含多个 **精灵** 对象

7. 使用 游戏精灵 和 精灵组 创建敌机

   - 使用派生的 **游戏精灵** 和 **精灵组** 创建 敌机 并且实现敌机动画
   - 导入 `plane_sprites` 模块 
   - 在 **游戏初始化** 创建 **精灵对象** 和 **精灵组对象**
   - 在 **游戏循环中** 让 **精灵组** 分别调用 `update()` 和 `draw(screen)` 方法
   - 精灵
     * 封装 **图像 image**、**位置 rect** 和 **速度 speed**
     * 提供 `update()` 方法，根据游戏需求，**更新位置 rect**
   - 精灵组
     * 包含 **多个** **精灵对象**
     * `update` 方法，让精灵组中的所有精灵调用 `update` 方法更新位置
     * `draw(screen)` 方法，在 `screen` 上绘制精灵组中的所有精灵
   - 需求：
     - 游戏启动后，**每隔 1 秒** 会 **出现一架敌机**
     - 每架敌机 **向屏幕下方飞行**，飞行 **速度各不相同**
     - 每架敌机出现的 **水平位置** 也不尽相同
     - 当敌机 **从屏幕下方飞出**，不会再飞回到屏幕中



## 文件职责

* `plane_main` 
  1. 封装 **主游戏类**
  2. 创建 **游戏对象**
  3. **启动游戏**
* `plane_sprites`
  * 封装游戏中 **所有** 需要使用的 **精灵子类**
  * 提供游戏的 **相关工具**



## 贡献

如果你在使用过程中发现任何问题，可以[提交 issue](https://github.com/NekoSilverFox/EasyQQ/issues) 或自行 fork 修改后提交 pull request。

如果你要提交 pull request，请确保你的代码风格和项目已有的代码保持一致（遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/)），变量命名清晰，有适当的注释。
