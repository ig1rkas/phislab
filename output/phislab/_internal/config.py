import pygame

from format import take_format

# constants
GRAVITY = 9810
x_const, y_const = take_format() 
x_m, y_m = int(x_const), int(y_const)
SIZE = (int(16 * x_m), int(9 * y_m))   
FPS = 60

labs = {'7class_pendulum': ["Маятник", "sevenclasspendulum.py"], '9class_speed of ball': ['Скорость мячика от угла наклона бруска', "nineclassspeedofballbyangle.py"], '8class_springpendulum': ["Пружинный маятник", "spring_pendulum.py"]}



wall_picture = 'images\wall.jpg'
ball_picture = 'images\metall_ball.png'
start_button_picture = 'images\start.png'
restart_button_picture = 'images\mrestart_image.png'
pendulum_picture = 'images\stand.png'
barometr_picture = 'images/barometr.png'
transportir_picture = 'images/transportir.png'
termometr_picture = 'images/termometr.png'
# colors
background_color = (200, 200, 200)
black = (0, 0, 0)
green = (0, 255, 0)
brown = (128, 64, 48)

# open_lab("7class_pendulum")