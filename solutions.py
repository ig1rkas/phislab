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
    
    def check_solution_on_click(e): 
        print("Check!")
        
    def open_solution(e):
        print("Solutions opening...")

    def create_block(student_name: str, theme: str) -> Container: 
        block_content = ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        [
                            ft.CircleAvatar(
                                bgcolor="#6F45BB",
                                content=ft.Text(student_name[0]),
                                tooltip=student_name
                            ),
                            ft.Text(f"Тема: {theme}"),
                            ft.ElevatedButton(text="Отметить", 
                                bgcolor="#7B9467", 
                                color="#FFFFFF", on_click=check_solution_on_click)
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
            on_click=open_solution
        )
        block_content.margin = ft.margin.all(10)
        block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
        return block
    
        
    blocks = [create_block("Кирилл", "Математический маятник")] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
    listv = ft.ListView(
            controls=blocks,
            expand=True,
        )

    solutions = flet.Row(
            [
                flet.Container(
                    content=flet.Stack(
                        [
                        flet.Column(
                            [
                                flet.Row(
                                    [
                                        flet.Text("Решения", font_family="Inter-Regular.ttf", size=26,),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                listv
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
        solutions
    )
    
    
flet.app(target=registration)

