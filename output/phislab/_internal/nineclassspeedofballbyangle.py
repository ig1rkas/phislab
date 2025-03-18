import pygame 
import pymunk.pygame_util
import time

from config import *
from images_up import load_image
from format import *
from math import *
from degree_to_radian import degree_to_radians

class Game():
    def __init__(self, angle = 45, mass = 10, gravity = 0, pos_start = 0, position = (0, 0), time_started = False) -> None:
        pygame.init()

        #main options
        self.FPS = 60
        self.running = True
        self.screen = pygame.display.set_mode(SIZE)
        pymunk.pygame_util.positive_y_is_up = False
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = 0, gravity
        self.time = 0
        self.time_start = time.time()

        # buttons
        # start button
        self.start_button = pygame.image.load(start_button_picture)
        self.start_button = pygame.transform.scale(self.start_button, (x_const, y_const))
        self.start_button_x = y_const / 6
        self.start_button_y = y_const / 6
        
        # restart image
        self.restart_button = pygame.image.load(restart_button_picture)
        self.restart_button = pygame.transform.scale(self.restart_button, (x_const, y_const))
        self.restart_button_x = self.start_button_x + y_const / 6 + x_const
        self.restart_button_y = self.start_button_y

        # text
        # angle
        self.angle = angle
        self.angle_text = "а = " + str(self.angle) + "°"
        self.angle_text_x = y_const / 6 
        self.angle_text_y = self.start_button_y + y_const 
        self.angle_text_size = int(y_const / 3)
        self.angle_text_color = black
        self.angle_text_is_pressed = False
        
        # mass
        self.mass = mass
        self.mass_text = "m = " + str(self.mass) + "г"
        self.mass_text_x = self.angle_text_x
        self.mass_text_y = self.angle_text_y + y_const // 2
        self.mass_text_size = self.angle_text_size
        self.mass_text_color = black
        self.mass_text_is_pressed = False
        
        # time
        self.time_started = time_started
        self.time_text = "время: 0"
        self.time_text_x = self.angle_text_x
        self.time_text_y = self.mass_text_y + y_const // 2
        self.time_text_size = self.mass_text_size
        self.time_text_color = black
        
        # shapes
        # wall options
        delta = (9 * x_const) / cos(radians(self.angle))
        y = sin(radians(self.angle)) * delta
        wall = pygame.image.load(wall_picture)
        self.wall = pygame.transform.scale(wall, (((9 * x_const) ** 2 + y ** 2) ** 0.5 + x_const, y_const))
        self.wall_x, self.wall_y = 7 * x_const - x_const / 2, SIZE[1] - y - y_const * 7 / 8
        self.wall.set_colorkey((255, 255, 255))
        self.wall = pygame.transform.rotate(self.wall, self.angle)
        self.wall_shape = pymunk.Segment(self.space.static_body, (7 * x_const, SIZE[1]), (SIZE[0], SIZE[1] - y), y_const / 2)
        self.wall_shape.elasticity = 0.6
        self.wall_shape.friction = 0.4
        self.space.add(self.wall_shape)

        # ball options
        ball = pygame.image.load(ball_picture)
        self.ball = pygame.transform.scale(ball, (y_const, y_const))
        self.ball_mass, self.ball_radius = mass, y_const / 2
        self.ball_moment = pymunk.moment_for_circle(self.ball_mass, 0, self.ball_radius)
        self.ball_body = pymunk.Body(self.ball_mass, self.ball_moment)
        if pos_start:
            self.ball_body.position = position
        else:
            self.ball_body.position = SIZE[0] - y_const, SIZE[1] - y - y_const / 2
        self.ball_shape = pymunk.Circle(self.ball_body, self.ball_radius)
        self.ball_shape.elasticity = 0.6
        self.ball_shape.friction = 0.4
        self.space.add(self.ball_body, self.ball_shape)


        # borders
        # down border
        self.segment_shape = pymunk.Segment(self.space.static_body, (0, SIZE[1]), SIZE, 0)
        self.segment_shape.elasticity = 0.6
        self.segment_shape.friction = 0.4
        self.space.add(self.segment_shape)
        
        # left border
        self.segment_left_shape = pymunk.Segment(self.space.static_body, (0, 0), (0, SIZE[1]), 0)
        self.segment_left_shape.elasticity = 0
        self.segment_left_shape.friction=1
        self.space.add(self.segment_left_shape)
        

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.angle_text_y <= event.pos[1] < self.mass_text_y:
                        self.angle_text_is_pressed = True
                    if self.mass_text_y <= event.pos[1] < self.mass_text_y + y_const:
                        self.mass_text_is_pressed = True
                    if self.start_button_y <= event.pos[1] <= self.start_button_y + y_const and self.start_button_x <= event.pos[0] <= self.start_button_x + x_const:
                        self.__init__(angle=int(self.angle_text[4:-1]), mass = int(self.mass_text[4:-1]), gravity=GRAVITY, pos_start=1, position=self.ball_body.position, time_started=True)
                    if self.restart_button_x <= event.pos[0] <= self.restart_button_x + x_const and self.restart_button_y <= event.pos[1] <= self.restart_button_y + y_const:
                        self.__init__(angle=int(self.angle_text[4:-1]), mass = int(self.mass_text[4:-1]), gravity=0)

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]: self.running = 0
                if pygame.key.get_pressed()[pygame.K_RETURN]: 
                    if self.angle_text_is_pressed:
                        self.angle_text_is_pressed = False
                        try:
                            if 0 <= int(self.angle_text[4:-1]) <= 45: 
                                self.__init__(angle=int(self.angle_text[4:-1]), mass = int(self.mass_text[4:-1]), gravity=0)
                            else:
                                self.__init__()
                        except:
                            self.__init__()
                    if self.mass_text_is_pressed:
                        self.mass_text_is_pressed = False
                        try:
                            if 1 <= int(self.mass_text[4:-1]) <= 1000: 
                                self.__init__(angle=int(self.angle_text[4:-1]), mass = int(self.mass_text[4:-1]), gravity=0)
                            else:
                                self.__init__()
                        except:
                            self.__init__()
                elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    if self.angle_text_is_pressed and len(self.angle_text) > 5: self.angle_text = self.angle_text[:-2] + "°"
                    if self.mass_text_is_pressed and len(self.mass_text) > 5: self.mass_text = self.mass_text[:-2] + "г"
                else:
                    s = event.unicode
                    if self.angle_text_is_pressed: 
                        if len(self.angle_text) < 10:
                            if s.isdigit(): 
                                if self.angle_text_is_pressed and 5 <= len(self.angle_text[:-1] + s + "°") < 8: self.angle_text = self.angle_text[:-1] + s + "°"
                    if self.mass_text_is_pressed:
                        if len(self.mass_text) < 10:
                            if s.isdigit(): 
                                if self.mass_text_is_pressed and 5 <= len(self.mass_text[:-1] + s + "°") < 10: self.mass_text = self.mass_text[:-1] + s + "г"

    def update(self):
        if self.angle_text_is_pressed: 
            self.angle_text_color = green
        else: self.angle_text_color = black
        if self.mass_text_is_pressed: 
            self.mass_text_color = green
        else:
            self.mass_text_color = black
        if self.time_started:
            self.time_text = "время: " + str(round(time.time() - self.time_start, 2)) + "с"
            if self.convert_coordinats_ball(self.ball_body.position)[1] >= SIZE[1] - y_const:
                self.time_started = False
        self.clock.tick(self.FPS)
        
    def convert_coordinats_ball(self, point):
        return int(point[0]) - y_const / 2, int(point[1]) - y_const / 2

    def render(self):
        self.screen.fill(background_color)
        self.print_text(self.angle_text, self.angle_text_x, self.angle_text_y, font_color=self.angle_text_color, font_size=self.angle_text_size)
        self.print_text(self.mass_text, self.mass_text_x, self.mass_text_y, font_size=self.mass_text_size, font_color=self.mass_text_color)
        self.print_text(self.time_text, self.time_text_x, self.time_text_y, font_size=self.time_text_size, font_color=self.time_text_color)
        self.screen.blit(self.start_button, (self.start_button_x, self.start_button_y))
        self.screen.blit(self.restart_button, (self.restart_button_x, self.restart_button_y))
        self.space.step(1 / self.FPS)
        self.screen.blit(self.wall, (self.wall_x, self.wall_y))
        self.screen.blit(self.ball, self.convert_coordinats_ball(self.ball_body.position))
        # self.space.debug_draw(self.draw_options)
        pygame.display.flip()

    def print_text(self, message, x, y, font_color = (0, 0, 0), font_size = 20, font_type = 'Roboto-Regular.ttf'):
        self.font_type = pygame.font.Font(font_type, font_size)
        self.text = self.font_type.render(message, True, font_color)
        self.screen.blit(self.text, (x, y))

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.events()

if __name__ == '__main__':
    game = Game()
    game.run()
    