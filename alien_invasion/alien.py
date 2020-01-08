import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.speed_factor = ai_settings.alien_speed_factor
        self.drop_speed = ai_settings.alien_drop_speed

        # 加载外星人图像，并设置 rect 属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)

        # 外星人移动方向, 1 表示向右，-1 表示向左
        self.moving_direction = 1

    def update(self):
        self.float_x += self.moving_direction * self.speed_factor
        self.rect.x = self.float_x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        return (self.rect.right > self.screen.get_rect().right
                or self.rect.left < 0)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
