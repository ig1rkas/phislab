import pygame
import pymunk.pygame_util
import pymunk
import time

from config import *
from math import *
from random import randint


class math_pendulum():
    def __init__(self, gravity=9810, mass=1, period=100000, time_started=False) -> None:
        pygame.init()
        # main config
        # main options
        self.FPS = 60
        self.running = True
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        self.time = 0
        self.time_start = time.time()

        self.space = pymunk.Space()
        self.space.gravity = 0, gravity
        pymunk.pygame_util.positive_y_is_up = False
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = SIZE[0] / 4, 0

        ball = pygame.image.load(ball_picture)
        self.ball = pygame.transform.scale(ball, (y_const / 2, y_const / 2))
        self.ball_mass, self.ball_radius = mass, y_const / 4
        self.ball_moment = pymunk.moment_for_circle(
            self.ball_mass, 0, self.ball_radius)
        self.ball_body = pymunk.Body(self.ball_mass, self.ball_moment)
        self.ball_body.position = SIZE[0] / 2, y_const
        self.ball_shape = pymunk.Circle(self.ball_body, self.ball_radius)
        self.ball_shape.elasticity = 0.6
        self.ball_shape.friction = 0.4

        self.joint = pymunk.constraints.DampedSpring(
            self.body, self.ball_body, self.body.position, (0, 0), 10, 50, period)

        self.segment_shape = pymunk.Segment(
            self.space.static_body, (0, SIZE[1]), SIZE, 0)
        self.segment_shape.elasticity = 0.6
        self.segment_shape.friction = 0.4
        self.space.add(self.segment_shape, self.joint,
                       self.ball_body, self.ball_shape)
        
        # text and button settings
        # play button
        self.start_button = pygame.image.load(start_button_picture)
        self.start_button = pygame.transform.scale(self.start_button, (x_const, y_const))
        self.start_button_x = y_const / 6
        self.start_button_y = y_const / 6
        
        # restart button
        self.restart_button = pygame.image.load(restart_button_picture)
        self.restart_button = pygame.transform.scale(self.restart_button, (x_const, y_const))
        self.restart_button_x = self.start_button_x + y_const / 6 + x_const
        self.restart_button_y = self.start_button_y
        
        # text mass_ball
        self.mass = mass
        self.mass_text = "m = " + str(int(self.mass * 100)) + "г"
        self.mass_text_x = self.start_button_x
        self.mass_text_y = self.start_button_y * 2 + y_const
        self.mass_text_size = int(x_const // 4)
        self.mass_text_color = black
        self.mass_text_is_pressed = False
        
        # time text
        self.time_started = time_started
        self.time_text = "время: 0"
        self.time_text_x = self.mass_text_x
        self.time_text_y = self.mass_text_y + y_const // 2
        self.time_text_size = self.mass_text_size
        self.time_text_color = black
        

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_y <= event.pos[1] <= self.start_button_y + y_const and self.start_button_x <= event.pos[0] <= self.start_button_x + x_const:
                    self.__init__(mass = int(self.mass_text[4:-1]) / 100, period=0, time_started=True)
                if self.restart_button_x <= event.pos[0] <= self.restart_button_x + x_const and self.restart_button_y <= event.pos[1] <= self.restart_button_y + y_const:
                    self.__init__(mass = int(self.mass_text[4:-1]) / 100, period=1000000000)
                if self.mass_text_y <= event.pos[1] < self.mass_text_y + y_const:
                        self.mass_text_is_pressed = True
                else:
                    self.mass_text_is_pressed = False

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]: self.running = 0
                if pygame.key.get_pressed()[pygame.K_RETURN]: 
                    if self.mass_text_is_pressed:
                        self.mass_text_is_pressed = False
                        try:
                            if 50 <= int(self.mass_text[4:-1]) <= 400: 
                                self.__init__(mass = int(self.mass_text[4:-1]) / 100, period=1000000)
                            else:
                                self.__init__()
                        except:
                            self.__init__()
                elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    if self.mass_text_is_pressed and len(self.mass_text) > 5: self.mass_text = self.mass_text[:-2] + "г"
                else:
                    s = event.unicode
                    if self.mass_text_is_pressed:
                        if len(self.mass_text) < 10:
                            if s.isdigit(): 
                                if self.mass_text_is_pressed and 5 <= len(self.mass_text[:-1] + s + "°") < 10: self.mass_text = self.mass_text[:-1] + s + "г"

    def update(self):
        if self.mass_text_is_pressed:
            self.mass_text_color = green
        else:
            self.mass_text_color = black
        if self.time_started: 
            self.time_text = "время " + str(round(time.time() - self.time_start, 2))
            if randint(1, 100) > 30:
                self.time_text = "время " + str(round(time.time() - self.time_start, 2))
        self.clock.tick(FPS)

    def convert_coordinats_ball(self, point):
        return int(point[0]) - y_const / 4, int(point[1]) - y_const / 4

    def render(self):
        self.screen.fill(background_color)
        self.space.step(1 / FPS)
        self.space.debug_draw(self.draw_options)
        pygame.draw.line(self.screen, (0, 200, 0), (SIZE[0] / 2 - x_const / 3, 0), (SIZE[0] / 2 - x_const / 3, self.ball_body.position[1] - y_const / 4), 3)
        self.print_text(message=f"{int(self.ball_body.position[1] - y_const / 4) // 4} см", x=SIZE[0] / 2 - x_const, y=(self.ball_body.position[1] - y_const / 4) / 2, font_color=(0, 200, 0))
        self.screen.blit(self.ball, self.convert_coordinats_ball(
            self.ball_body.position))
        self.screen.blit(self.start_button, (self.start_button_x, self.start_button_y))
        self.screen.blit(self.restart_button, (self.restart_button_x, self.restart_button_y))
        self.print_text(message=self.mass_text, x=self.mass_text_x, y=self.mass_text_y, font_color=self.mass_text_color, font_size=self.mass_text_size)
        self.print_text(message=self.time_text, x=self.time_text_x, y=self.time_text_y, font_color=self.time_text_color, font_size=self.time_text_size)
        pygame.display.flip()

    def print_text(self, message, x, y, font_color=(0, 0, 0), font_size=20, font_type='Roboto-Regular.ttf'):
        self.font_type = pygame.font.Font(font_type, font_size)
        self.text = self.font_type.render(message, True, font_color)
        self.screen.blit(self.text, (x, y))

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.events()


if __name__ == "__main__":
    game = math_pendulum()
    game.run()
