import random
from math import pi
import time

import flet as flet
from flet import Container, ElevatedButton, Page, Stack, colors, IconButton

def registration(page: flet.Page):
    page.title = "registration"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = "dark"
    contents = [flet.Container(
                        flet.Text("1"), width=500, height=500, bgcolor="#343537", border_radius=50
                    ),
                flet.Container(
                        flet.Text("2"), width=500, height=500, bgcolor=flet.colors.BLUE_300, border_radius=50
                    ),
                flet.Container(
                        flet.Text("3"), width=500, height=500, bgcolor=flet.colors.PINK_300, border_radius=50
                    ),
                flet.Container(
                        flet.Text("4"), width=500, height=500, bgcolor=flet.colors.GREEN_300, border_radius=50
                    ),
                flet.Container(
                        flet.Text("4"), width=500, height=500, bgcolor=flet.colors.PURPLE_300, border_radius=50
                    ),
                ]


    contents_value = len(contents) - 1
    slider = flet.Slider(min=0, max=contents_value, divisions=contents_value, active_color="#6F45BB", width=500)
    switcher = flet.AnimatedSwitcher(
        content=contents[0],
        transition=flet.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=flet.AnimationCurve.EASE_IN,
        switch_out_curve=flet.AnimationCurve.EASE_OUT
        
    )
    carousel = flet.Row(
            [
                flet.Column(
                    [
                    switcher,
                    slider
                    ]
                )
                
            ], alignment=flet.MainAxisAlignment.CENTER
    )

    page.add(
        carousel
    )
    start_time = time.time()
    while 1:
        t = (time.time() - start_time) // 3 % len(contents)
        slider.value = t 
        slider.update()
        t = int(t)
        if switcher.content != contents[t % len(contents)]:
            switcher.content = contents[t % len(contents)]
            switcher.update()
            
    
    
flet.app(target=registration)