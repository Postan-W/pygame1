import pygame.font

class Scoreboard():
    def __init__(self,settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.text_color = (0,0,0)
        self.font = pygame.font.Font("C:\WINDOWS\FONTS\SIMHEI.TTF", 20)
        self.prep_score()
    def prep_score(self):
        score_str = "击落: " + str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)