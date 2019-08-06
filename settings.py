class Settings():
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color = (163,163,128)
        self.bullet_height =10
        self.bullet_color = (0,0,0)
        self.bullet_count_allowed = 10
        self.alien_speed = 1
        self.ship_limit = 3
        self.fleet_speed_up_scale = 1.1
        self.ship_speed_up_scale = 1.1
        self.bullet_speed_up_scale = 1.4
        self.bullet_width_speed_up_scale = 1.4
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.bullet_speed = 2
        self.fleet_drop_speed = 7
        self.fleet_direction = 1
        self.speed_of_ship = 1
        self.bullet_width = 10

    def increase_speed(self):
        if self.speed_of_ship <= 10:
            self.speed_of_ship *= self.ship_speed_up_scale
        if self.bullet_speed <= 20:
            self.bullet_speed *= self.bullet_speed_up_scale
        self.fleet_drop_speed *= self.fleet_speed_up_scale
        if self.bullet_width <= 250:
            self.bullet_width *= self.bullet_width_speed_up_scale