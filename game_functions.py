import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown(event,ship,settings,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ship,settings,screen,bullets)
def check_keyup(event,ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_play_button(stats, play_button, mouse_x, mouse_y,aliens,ship,bullets,settings,screen):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        settings.initialize_dynamic_settings()
        stats.reset_stats()
        pygame.mouse.set_visible(False)
        stats.game_active = True
        aliens.empty
        bullets.empty
        create_fleet(settings,screen,aliens,ship)
        ship.center_ship()

def check_events(stats,play_button,ship,settings,screen,bullets,aliens):
    #响应鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event,ship,settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,ship,bullets,settings,screen)
def show_information(settings,screen,scoreboard,stats):
    bullets_speed = int(settings.bullet_speed)
    ship_speed = int(settings.speed_of_ship)
    fleet_speed = int(settings.fleet_drop_speed)
    bullets_width = int(settings.bullet_width)
    life_left = str(stats.ships_left)
    score_rect = scoreboard.score_rect
    bg_color = settings.bg_color
    text_color = (0, 0, 0)
    font = pygame.font.Font("C:\WINDOWS\FONTS\SIMHEI.TTF", 20)

    bullets_str = "子弹速度:" + str(bullets_speed)
    ship_str = "战机速度:" + str(ship_speed)
    fleet_str = "飞船速度:" + str(fleet_speed)
    bullets_width_str = "子弹宽度: " + str(bullets_width)
    left_life_str = "剩余生命:" + str(life_left)
    str1 = bullets_str + "  " + ship_str + "  " + fleet_str + "  " + bullets_width_str+ "  "
    image1 = font.render(str1,True,text_color,bg_color)
    rect1 = image1.get_rect()
    rect1.centerx = screen.get_rect().centerx
    rect1.top = 20
    screen.blit(image1,rect1)
    image2 =font.render(left_life_str,True,text_color,bg_color)
    rect2 = image2.get_rect()
    rect2.left = screen.get_rect().left
    rect2.top = 20
    screen.blit(image2,rect2)
    file2= open("score.txt", 'r')
    score_record = file2.read()
    image3 = font.render("历史最高:" + score_record,True,text_color,bg_color)
    rect3 = image3.get_rect()
    rect3.top = 20
    rect3.right = scoreboard.score_rect.left - 20
    screen.blit(image3,rect3)
##################################刷新屏幕图像################################
def update_screen(settings,screen,ship,bullets,aliens,stats,play_button,scoreboard):
    #更新屏幕上的图像并切换到新屏幕
    #每次循环时都重绘屏幕
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    scoreboard.show_score()
    show_information(settings,screen,scoreboard,stats)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
##############################################################################
def update_bullets(bullets,aliens,settings,screen,ship,stats,scoreboard):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collision(bullets,aliens,settings,screen,ship,stats,scoreboard)
def check_collision(bullets,aliens,settings,screen,ship,stats,scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        pygame.mixer.init()
        sound = pygame.mixer.Sound("bloom.wav")
        sound.play()
        for ali in collisions.values():
            stats.score += len(ali)
            scoreboard.prep_score()
    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, aliens, ship)


def fire_bullet(ship,settings,screen,bullets):
    if len(bullets) < settings.bullet_count_allowed:
        new_bullet = Bullet(settings, screen, ship)
        pygame.mixer.init()
        pygame.mixer.music.load("shoot.mp3")
        pygame.mixer.music.play(0,0.0)
        bullets.add(new_bullet)

#创建外星飞船的相关函数
def rows_of_fleet(settings,ship_hight,alien_hight):
    return  int((settings.screen_height - 6* alien_hight - ship_hight)/(1.5 * alien_hight))

def get_number(settings,alien_width):
    return int((settings.screen_width - 30)/(1.5*alien_width))
def create_alien(settings,screen,aliens,number,row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 0.5 * alien_width + number * 1.5 * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)
def create_fleet(settings,screen,aliens,ship):
    alien = Alien(settings,screen)
    number = get_number(settings,alien.rect.width)
    rows = rows_of_fleet(settings,ship.rect.height,alien.rect.height)
    for alien_number in range(number):
        for rows_number in range(rows):
            create_alien(settings,screen,aliens,alien_number,rows_number)

def check_aliens_bottom(settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings,stats,screen,aliens,ship,bullets)
            break

def ship_hit(settings,stats,screen,aliens,ship,bullets):
    if stats.ships_left > 1:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        #此时将分数写入文件
        score_file = open("score.txt",'w')
        score_file.write(str(stats.score))
        score_file.close()
        pygame.mouse.set_visible(True)
def update_aliens(settings,aliens,stats,screen,ship,bullets):
    check_fleet_edges(settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, aliens, ship, bullets)
    check_aliens_bottom(settings,stats,screen,ship,aliens,bullets)
def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings,aliens)
            break


def change_fleet_direction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1
