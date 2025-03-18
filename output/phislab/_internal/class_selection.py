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
    
    def add_new_task(e):
        print("adding new task...")


    def create_block_student_section(student: str, mail: str) -> Container: 
        block_content = ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        [
                            ft.Text(student, size=20),
                            ft.Text(mail, size=20),
                            ft.PopupMenuButton(
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(),  # divider
                                    ft.PopupMenuItem(
                                        text="Checked item", checked=False, on_click=lambda x: print(10)
                                    ),
                                ], icon_color="F"*6
                            ),
                        ], alignment=flet.MainAxisAlignment.SPACE_AROUND
                    )
                ]
            )
        )
        block = ft.Container(
            content=flet.Stack(
                [
                    block_content,
                ]
            ),
            width=700,
            height=50,
        )
        block_content.margin = ft.margin.all(10)
        block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
        return block
        
    
        
    class_cont_blocks = [create_block_student_section('Сабуров Кирилл', "pro100top@mail.com")] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
    class_listv = ft.ListView(
            controls=class_cont_blocks,
            expand=True,
        )

    class_section = flet.Row(
            [
                flet.Container(
                    content=flet.Stack(
                        [
                        flet.Column(
                            [
                                flet.Row(
                                    [
                                        flet.Text("Фамилия Имя", font_family="Inter-Regular.ttf", size=20,),
                                        flet.Text("Почта", font_family="Inter-Regular.ttf", size=20,),
                                        flet.Text("Ключ: ", font_family="Inter-Regular.ttf", size=20,),
                                    ], alignment=flet.MainAxisAlignment.SPACE_AROUND
                                ),
                                class_listv,
                                ft.Container(content=ft.Row([ft.Text("Выдать задание", size=20, color="#A3DEFF")], alignment=ft.MainAxisAlignment.CENTER), width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")), on_click=add_new_task)
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
        class_section
    )
    
    
flet.app(target=registration)

