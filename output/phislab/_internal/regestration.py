import random
from math import pi
import time

import flet
from flet import Container, ElevatedButton, Page, Stack, colors, IconButton

def registration(page: flet.Page):
    page.title = "registration"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = "dark"
    reg = flet.Row(
            [
                flet.Container(
                    content=flet.Stack(
                        controls=[
                            
                        flet.Column(
                            controls=[
                                flet.Row(
                                    controls=[
                                        flet.Text("Регистрация", size=20, color="white"),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                flet.TextField(label="Имя", hint_text="Иван Иванов", color="white"),
                                flet.TextField(label="email", hint_text="email@mail.com", color="white"),
                                flet.TextField(label="Ключ класса", hint_text="key2134", color="white"),
                                flet.Row(
                                    controls=[

                                    flet.CupertinoSlidingSegmentedButton(
                                        selected_index=1,
                                        thumb_color=flet.colors.BLUE_400,
                                        on_change=lambda e: print(f"selected_index: {e.data}"),
                                        padding=flet.padding.symmetric(0, 10),
                                        controls=[
                                            flet.Text("Я учитель"),
                                            flet.Text("Я ученик"),
                                        ], 
                                    ),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                flet.Divider(height=70, color="transparent"),
                                flet.Row(
                                    controls=[
                                        
                                        flet.ElevatedButton(text="Авторизироваться", color=flet.colors.BLUE_400, bgcolor=flet.colors.GREY_900, height=80),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                )
                                
                            ],alignment=flet.MainAxisAlignment.START
                        )
                        ]
                        ),
                    margin=10,
                    padding=10,
                    alignment=flet.alignment.top_left,
                    bgcolor="#1f1f1f",
                    width=page.window_width / 2.5,
                    height=page.window_height / 1.5,
                    border_radius=10,
                )
            ], alignment=flet.MainAxisAlignment.CENTER, animate_opacity=1000
    )
    reg.opacity = 0

    page.add(
        reg
    )
    
    def animate_opacity(e):
        reg.opacity = 0 if reg.opacity == 1 else 1
        reg.update()
        
    start_time = time.time()
    while 1:
        if time.time() - start_time > 1:
            animate_opacity(1)
            break
    
flet.app(target=registration)