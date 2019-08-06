import pygame

class Ship():
    def __init__(self,screen,settings):
        #初始化飞船并设置其位置
        self.screen = screen
        self.settings = settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的center属性中存储小数值代表当前飞船中心位置，所以可以精确调节
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.speed_of_ship
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.speed_of_ship
        self.rect.centerx = self.center
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx