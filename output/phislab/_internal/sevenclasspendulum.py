import pygame
import pymunk.pygame_util
import time

from config import *
from math import *

        
class pendulum_lab():
    def __init__(self, f_angle = 90, l = 100, gravity=0, time_started=0) -> None:
        # main config
        pygame.init()
        pymunk.pygame_util.positive_y_is_up = False
        self.screen = pygame.display.set_mode(SIZE)
        self.running = True
        self.clock = pygame.time.Clock()
        self.space = pymunk.Space()
        self.space.gravity = 0, gravity
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
        # f text
        self.f_text = "f0 = " + str(f_angle) + "°"
        self.f_text_x = y_const / 6 
        self.f_text_y = self.start_button_y + y_const
        self.f_text_size = int(y_const / 3)
        self.f_text_color = black
        self.f_text_is_pressed = False

        # l text 
        self.l_text = "длина = " + str(l) + "мм"
        self.l_text_x = y_const / 6 
        self.l_text_y = self.f_text_y + y_const // 2
        self.l_text_size = int(y_const / 3)
        self.l_text_color = black
        self.l_text_is_pressed = False

        # time text
        self.time_started = time_started
        self.time_text = "время: 0"
        self.time_text_x = self.l_text_x
        self.time_text_y = self.l_text_y + y_const // 2
        self.time_text_size = self.l_text_size
        self.time_text_color = black

        # pendulum settings
        pendulum = pygame.image.load(pendulum_picture)
        self.pendulum = pygame.transform.scale(pendulum, (x_const * 3, y_const * 4))
        self.pendulum = pygame.transform.flip(self.pendulum, True, False)
        self.pendulum_x, self.pendulum_y = SIZE[0] - x_const * 3, SIZE[1] - y_const * 4
        self.start_rope_position = self.pendulum_x + x_const / 6, self.pendulum_y + y_const / 6 

        # ball options
        ball = pygame.image.load(ball_picture)
        self.ball = pygame.transform.scale(ball, (x_const, y_const))
        self.ball_body = pymunk.Body()
        x_ball = sin(radians(f_angle)) * l
        y_ball = (l ** 2 - x_ball ** 2) ** 0.5
        self.ball_body.position = self.pendulum_x - x_ball + x_const / 6, self.pendulum_y + y_ball + y_const / 6
        self.ball_shape = pymunk.Circle(self.ball_body,  y_const / 2)
        self.ball_shape.density = 1
        self.ball_shape.elasticity = 1   
        self.space.add(self.ball_body, self.ball_shape)


        # fixed block of pendulum
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = self.start_rope_position
        self.joint = pymunk.PinJoint(self.ball_body, self.body)
        self.space.add(self.joint) 


    def convert_coordinats_ball(self, point):
        return int(point[0]) - y_const / 2, int(point[1]) - y_const / 2

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.f_text_y <= event.pos[1] <= self.l_text_y:
                    self.f_text_is_pressed = True
                if self.l_text_y <= event.pos[1] <= self.l_text_y + y_const:
                    self.l_text_is_pressed = True
                if self.start_button_x <= event.pos[0] <= self.start_button_x + x_const and self.start_button_y <= event.pos[1] <= self.start_button_y + y_const:
                    self.__init__(f_angle=int(self.f_text[5:-1]), l=int(self.l_text[8:-2]), gravity=GRAVITY, time_started=True)
                if self.restart_button_x <= event.pos[0] <= self.restart_button_x + x_const and self.restart_button_y <= event.pos[1] <= self.restart_button_y + y_const:
                    self.__init__(f_angle=int(self.f_text[5:-1]), l=int(self.l_text[8:-2]), gravity=0)

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_ESCAPE]: self.running = False
                elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    if self.f_text_is_pressed:
                        if 6 < len(self.f_text) < 9:
                            self.f_text = self.f_text[:-2] + "°"
                    if self.l_text_is_pressed:
                        if 10 < len(self.l_text) < 15:
                            self.l_text = self.l_text[:-3] + "мм"
                elif pygame.key.get_pressed()[pygame.K_RETURN]:
                    if self.f_text_is_pressed:
                        if 0 <= int(self.f_text[5:-1]) <= 90:
                            self.__init__(f_angle=int(self.f_text[5:-1]), l=int(self.l_text[8:-2]), gravity=0) 
                        else:
                            self.__init__()
                    if self.l_text_is_pressed:
                        if 20 <= int(self.l_text[8:-2]) < y_const * 4:
                            self.__init__(l=int(self.l_text[8:-2]), f_angle=int(self.f_text[5:-1]), gravity=0)
                        else:
                            self.__init__()
                else:
                    s = event.unicode
                    if self.f_text_is_pressed: 
                        if len(self.f_text) < 10:
                            if s.isdigit(): 
                                if self.f_text_is_pressed and 5 <= len(self.f_text[:-1] + s + "°") < 9: self.f_text = self.f_text[:-1] + s + "°"
                    if self.l_text_is_pressed:
                        if len(self.l_text) < 15:
                            if s.isdigit(): 
                                if self.l_text_is_pressed and 10 <= len(self.l_text[:-2] + s + "мм") < 14: self.l_text = self.l_text[:-2] + s + "мм"

    def update(self):
        self.clock.tick(FPS)
        self.space.step(1 / FPS)
        if self.time_started: self.time_text = "время " + str(round(time.time() - self.time_start, 2))
        if self.f_text_is_pressed: self.f_text_color = green
        if self.l_text_is_pressed: self.l_text_color = green

    def render(self):
        self.screen.fill(background_color)
        self.screen.blit(self.pendulum, (self.pendulum_x, self.pendulum_y))
        pygame.draw.line(self.screen, brown, self.ball_body.position, self.body.position, int(x_const / 60))
        self.screen.blit(self.ball, self.convert_coordinats_ball(self.ball_body.position))
        self.screen.blit(self.start_button, (self.start_button_x, self.start_button_y))
        self.screen.blit(self.restart_button, (self.restart_button_x, self.restart_button_y))
        self.print_text(self.f_text, self.f_text_x, self.f_text_y, font_color=self.f_text_color, font_size=self.f_text_size)
        self.print_text(self.l_text, self.l_text_x, self.l_text_y, font_color=self.l_text_color, font_size=self.l_text_size)
        self.print_text(self.time_text, self.time_text_x, self.time_text_y, font_size=self.time_text_size, font_color=self.time_text_color)

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
    
if __name__ == "__main__":
    game = pendulum_lab()
    game.run()
