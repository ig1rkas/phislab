import random
from math import pi
import time

import flet as ft, flet
from flet import Container, ElevatedButton, Page, Stack, colors, IconButton

def registration(page: flet.Page):
    page.title = "registration"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = "dark"

    #messages box
    
    def add_new_class(e):
        print("adding new class...")

    def open_class(e):
        print("class opening...")

    def create_block_class(class_name: str) -> Container: 
        block_content = ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        [
                            ft.CircleAvatar(
                                bgcolor="#6F45BB",
                                content=ft.Text(class_name.split()[0]),
                                tooltip=class_name
                            ),
                            ft.Text(f"{class_name}"),
                        ], 
                    )
                ]
            )
        )
        block = ft.Container(
            content=flet.Stack(
                [
                    block_content
                ]
            ),
            width=700,
            height=50,
            on_click=open_class
        )
        block_content.margin = ft.margin.all(10)
        block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
        return block
    
        
    classes_blocks = [create_block_class('10 "И" Класс')] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
    classes_listv = ft.ListView(
            controls=classes_blocks,
            expand=True,
        )

    classes = flet.Row(
            [
                flet.Container(
                    content=flet.Stack(
                        [
                        flet.Column(
                            [
                                flet.Row(
                                    [
                                        flet.Text("Классы", font_family="Inter-Regular.ttf", size=26,),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                classes_listv,
                                ft.Container(content=ft.Row([ft.Text("Добавить класс", size=20, color="#A3DEFF")], alignment=ft.MainAxisAlignment.CENTER), width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")), on_click=add_new_class)
                            ], alignment=flet.MainAxisAlignment.START
                        )    
                        ]
                    ), 
                    width=700, 
                    height=500, 
                    bgcolor="#343537", 
                    border_radius=50
                )
                
            ], alignment=flet.MainAxisAlignment.CENTER
    )
    


    page.add(
        classes
    )
    
    
flet.app(target=registration)

