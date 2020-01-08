import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.speed_factor = ai_settings.ship_speed_factor
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞船的位置范围
        self.min_centerx = self.screen_rect.left + self.rect.width / 2
        self.max_centerx = self.screen_rect.right - self.rect.width / 2

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        self.center_ship()
        
        # 在飞船的属性float_centerx中存储小数值
        self.float_centerx = float(self.rect.centerx)

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的float_centerx值，而不是rect
        if self.moving_right:
            temp = self.float_centerx + self.speed_factor
            self.float_centerx = min(temp, self.max_centerx)
        if self.moving_left and self.rect.left > 0:
            temp = self.float_centerx - self.speed_factor
            self.float_centerx = max(temp, self.min_centerx)

        # 根据float_centerx更新rect对象
        self.rect.centerx = self.float_centerx

    def center_ship(self):
        """将飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
