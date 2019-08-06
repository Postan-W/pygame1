import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def runGame():
    #初始化游戏界面
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption("打飞船的并不无聊的无聊游戏")
    #初始化飞船
    ship = Ship(screen,settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings,screen,aliens,ship)
    stats = GameStats(settings)
    play_button = Button(settings,screen,"开始")
    scoreborad = Scoreboard(settings,screen,stats)
    while True:
        gf.check_events(stats,play_button,ship,settings,screen,bullets,aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,settings,screen,ship,stats,scoreborad)
            gf.update_aliens(settings,aliens,stats,screen,ship,bullets)
        gf.update_screen(settings,screen,ship,bullets,aliens,stats,play_button,scoreborad)
runGame()