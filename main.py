import random
from math import pi
import time
import flet as ft, flet
import pyperclip

from pprint import pprint
from flet import Container, ElevatedButton, Page, Stack, colors, IconButton
from db import autorisation_user, regestration_new_user, generate_key, check_email, check_username, add_class, take_teacher_key, download_classes, give_tasks, open_lab, take_name, download_tasks, add_solution, get_solutions, get_file_solution
from config import labs
from auth_mail import send_auth_mail

def main(page: Page):
    page.title = "PhisLab app"
    page.window_maximized = True
    start_time = time.time()
    size = 40
    gap = 6
    duration = 1750
    page.theme_mode = "dark"
    page.window_icon = "phis_icon.ico"
    # page.fonts = "Inter-Regular.ttf"
    # page.window_full_screen = True
    # page.window_maximizable = True

    c1 = colors.PINK_500
    c2 = colors.AMBER_500
    c3 = colors.LIGHT_GREEN_500
    c4 = colors.DEEP_PURPLE_500

    all_colors = [
        colors.AMBER_400,
        colors.AMBER_ACCENT_400,
        colors.BLUE_400,
        colors.BROWN_400,
        colors.CYAN_700,
        colors.DEEP_ORANGE_500,
        colors.CYAN_500,
        colors.INDIGO_600,
        colors.ORANGE_ACCENT_100,
        colors.PINK,
        colors.RED_600,
        colors.GREEN_400,
        colors.GREEN_ACCENT_200,
        colors.TEAL_ACCENT_200,
        colors.LIGHT_BLUE_500,
    ]

    parts = [
        # P
        (0, 0, c1),
        (0, 1, c1),
        (0, 2, c1),
        (0, 3, c1),
        (0, 4, c1),
        (1, 0, c1),
        (1, 2, c1),
        (2, 0, c1),
        (2, 1, c1),
        (2, 2, c1),
        # H
        (4, 0, c1),
        (4, 1, c1),
        (4, 2, c1),
        (4, 3, c1),
        (4, 4, c1),
        (5, 2, c1),
        (6, 0, c1),
        (6, 1, c1),
        (6, 2, c1),
        (6, 3, c1),
        (6, 4, c1),
        # I
        (8, 0, c1),
        (8, 1, c1),
        (8, 2, c1),
        (8, 3, c1),
        (8, 4, c1),
        # S
        (10, 0, c1),
        (11, 0, c1),
        (12, 0, c1),
        (10, 1, c1),
        (10, 2, c1),
        (11, 2, c1),
        (12, 2, c1),
        (12, 3, c1),
        (12, 4, c1),
        (11, 4, c1),
        (10, 4, c1),
        # L
        (14, 0, c4),
        (14, 1, c4),
        (14, 2, c4),
        (14, 3, c4),
        (14, 4, c4),
        (15, 4, c4),
        (16, 4, c4),
        # A
        (18, 0, c4),
        (18, 1, c4),
        (18, 2, c4),
        (18, 3, c4),
        (18, 4, c4),
        (20, 0, c4),
        (20, 1, c4),
        (20, 2, c4),
        (20, 3, c4),
        (20, 4, c4),
        (19, 0, c4),
        (19, 2, c4),
        # B
        (22, 0, c4),
        (22, 1, c4),
        (22, 2, c4),
        (22, 3, c4),
        (22, 4, c4),
        (23, 0, c4),
        (24, 1, c4),
        (23, 2, c4),
        (24, 3, c4),
        (23, 4, c4),
    ]

    width = 25 * (size + gap)
    height = 10 * (size + gap)

    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.001
        page.update()

    def randomize3(e):

        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.001
        page.update()

    def randomize2(e):
        Login_button.opacity = 1
        for i in range(len(parts)):
            c = canvas.controls[i]
            c.bgcolor = random.choice([c1, c4])
        page.update()

    def assemble(e):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = (top) * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        page.update()

    def change_theme(e):
        if page.theme_mode == "dark":
            page.theme_mode = "light"
        else:
            page.theme_mode = "dark"
        page.update()

    def button_clicked(e):
        Login_button.opacity = 0
        randomize3(1)
        start_time = time.time()
        while 1:
            if time.time() - start_time > 2:
                page.remove(canvas)
                page.add(
                    reg
                )
                break
        start_time = time.time()
        while 1:
            if time.time() - start_time > 0.1:
                animate_reg(1)
                break

    def animate_reg(e):
        reg.opacity = 0 if reg.opacity == 1 else 1
        reg.update()
        page.update()
        
    def reg_dialog_close(e):
        animate_reg_page(1)
        reg_dialog.open = False
        page.update()    

    reg_page_1 = ft.Container(
        ft.Text("Нам не удалось найти пользователя с вашими данными... \nЗарегистрировать нового пользователя?", font_family="Inter-Regular.ttf", size=16),
        height=60,
        width=450
    )
    reg_page_2 = ft.Container(
        content=ft.Stack(
            [
                ft.Column(
                    [
                        ft.Text("На вашу почту был отправлен код подтверждения", font_family="Inter-Regular.ttf", size=16),
                        user_code := ft.TextField(
                            label="Введите код подтверждения",
                            multiline=False,
                            width=450
                        ),
                    ]
                )
            ]
        ),
        height=100,
        width=450
    )
    reg_page = ft.AnimatedSwitcher(
        reg_page_1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.DECELERATE,
        switch_out_curve=ft.AnimationCurve.DECELERATE,
    )
    def confirm_reg(e):
        print("start reg", user_code.value, auth_key)
        if int(user_code.value) == auth_key:
            print("reg...")
            regestration_new_user(name.value, email.value, generate_key(), type_int.selected_index)
            reg_dialog_close(1)
            print("reg finished")
        else:
            animate_reg_page(1)
            page.update()
            
            
    
    def animate_reg_page(e):
        reg_page.content = reg_page_2 if reg_page.content == reg_page_1 else reg_page_1
        if reg_button.text == "Зарегистрироваться":
            reg_button.text = "Подтвердить" 
            send_auth_mail(email.value, auth_key) 
            reg_button.on_click=confirm_reg
        else:
            reg_button.text = "Зарегистрироваться"
            reg_button.on_click=animate_reg_page
        page.update()
        
    auth_key = random.randint(100000, 999999)
        
    reg_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Ups... Пользователь не найден..."),
        content=reg_page,
       
        actions=[
            ft.Column(
                [
                    ft.Row(
                        [
                            reg_button := ft.ElevatedButton(
                                "Зарегистрироваться",
                                icon=ft.icons.CHECK_CIRCLE_OUTLINED,
                                on_click=animate_reg_page
                            ),
                            ft.ElevatedButton(
                                "Отменить",
                                icon=ft.icons.CLOSE,
                                on_click=reg_dialog_close
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                ]
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=reg_dialog_close
    )

    def reg_dialog_open():
        page.dialog = reg_dialog
        reg_dialog.open = True
        page.update()
        
    def autorisation(e) -> None:
        print("autorisation started...")
        if autorisation_user(name.value, email.value, key.value, type_int.selected_index):
            print("autorisated")
            
            
            if not type_int.selected_index: #teacher window
                teacher_key = take_teacher_key(name.value, email.value)
                print("teacher")
                animate_reg(1)
                page.clean()
                font = "Inter-Regular.ttf"
                selected = "#6F45BB"
                white = "#FFFFFF"
                page_number = 1
                width_for_switcher = page.width * 0.6 * 0.8
                heigth_for_switcher = page.height * 0.8
                contents = [flet.Container(
                                    flet.Text("2"), width=width_for_switcher, height=heigth_for_switcher, bgcolor="#343537", border_radius=50, border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                                ),
                            flet.Container(
                                    flet.Text("2"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.BLUE_300, border_radius=50, border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                                ),
                            flet.Container(
                                    flet.Text("3"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.PINK_300, border_radius=50, border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                                ),
                            flet.Container(
                                    flet.Text("4"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.GREEN_300, border_radius=50, border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                                ),
                            flet.Container(
                                    flet.Text("5"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.PURPLE_300, border_radius=50, border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                                ),
                            ]
                contents_value = len(contents) - 1
                slider = flet.Slider(min=0, max=contents_value, divisions=contents_value, active_color="#6F45BB", width=width_for_switcher)
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
                def close_solution_dialog(e):
                    page.dialog.open = False
                    page.update()
                
                solution_dialog = ft.AlertDialog(
                    modal=False,
                    title=ft.Column(
                        [
                            ft.Text("Тема", size=26),
                            ft.Text("Имя", size=20)
                        ]
                    ),
                    content=ft.Row(
                        [
                            
                        ], width=350
                    ),
                
                    actions=[
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Просмотреть файл",
                                            icon=ft.icons.FILE_OPEN,
                                            disabled=True
                                        ),
                                        ft.ElevatedButton(
                                            "Закрыть",
                                            icon=ft.icons.ARROW_FORWARD_OUTLINED,
                                            on_click=close_solution_dialog
                                        ),
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                            ]
                        ),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                
                def check_solution_on_click(student_name: str, theme: str, description: str, filename: str, class_key: str, id: int):
                    solution_dialog.title = ft.Column(
                        [
                            ft.Text(f"Тема: {theme}", size=26),
                            ft.Text(f"Ученик: {student_name}", size=20)
                        ]
                    )
                    solution_dialog.content = ft.Row(
                        [
                            ft.TextField(
                                label="Описание",
                                multiline=True,
                                value=description,
                                width=350,
                                border_color=ft.colors.WHITE,
                                max_lines=5,
                            )
                        ], width=350
                    )
                    if filename != "":
                        solution_dialog.actions = [
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.ElevatedButton(
                                                filename,
                                                icon=ft.icons.FILE_OPEN,
                                                on_click=lambda _: get_file_solution(filename, id, class_key)
                                            ),
                                            ft.ElevatedButton(
                                                "Закрыть",
                                                icon=ft.icons.ARROW_FORWARD_OUTLINED,
                                                on_click=close_solution_dialog
                                            ),
                                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    ),
                                ]
                            ),
                        ]
                    page.dialog = solution_dialog
                    solution_dialog.open = True
                    page.update()
                    
                def open_solution(e):
                    print("Solutions opening...")

                def create_block(student_name: str, theme: str, id: int, class_key: str, filename: str, description: str) -> ft.Container: 
                    block_content = ft.Container(
                        content=ft.Stack(
                            [
                                ft.Row(
                                    [
                                        ft.Row(
                                            [
                                                ft.CircleAvatar(
                                                    bgcolor="#6F45BB",
                                                    content=ft.Text(student_name[0].upper()),
                                                    tooltip=student_name
                                                ),
                                                ft.Text(f"Тема: {theme}"),
                                            ]
                                        ),
                                        ft.ElevatedButton(text="Открыть решение", 
                                            bgcolor="#7B9467", 
                                            color="#FFFFFF", on_click=lambda _: check_solution_on_click(student_name, theme, description, filename, class_key, id))
                                    ], ft.MainAxisAlignment.SPACE_BETWEEN
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
                        on_click=open_solution,
                        
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                def refresh(e):
                    solutions_download = get_solutions(teacher_key)
                    blocks.clear()
                    for solution in solutions_download: blocks.append(create_block(solution["student_name"], solution["theme"], solution["id"], solution["class_key"], solution["filename"], solution["description"]))
                    blocks.append(ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373"))))
                    teacher_classes = download_classes(teacher_key)
                    classes_blocks.clear()
                    for i in teacher_classes: classes_blocks.append(create_block_class(i[0], i[1]))
                    classes_blocks.append(ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373"))))
                    listv.update()
                    classes_listv.update()
                    print("Done refresh")
                    
                
                print(teacher_key)
                solutions_blocks = get_solutions(teacher_key)
                pprint(solutions_blocks)
                blocks = list()
                for solution in solutions_blocks:
                    blocks.append(create_block(solution["student_name"], solution["theme"], solution["id"], solution["class_key"], solution["filename"], solution["description"]))
                
                blocks += [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
                listv = ft.ListView(
                        controls=blocks,
                        expand=True,
                    )

                solutions = flet.Container(
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
                                width=page.width * 0.4, 
                                height=page.height * 0.4, 
                                bgcolor="#343537", 
                                border_radius=50, 
                                border=ft.border.only(right=ft.border.BorderSide(1, "#5C5555"), bottom=ft.border.BorderSide(1, "#5C5555"))
                            )
                
                #messages box

                def open_message(e):
                    print("message opening...")

                def create_block_message(student_name: str, message: str) -> ft.Container: 
                    if len(message) > 30:
                        message = message[:30] + "..."
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
                                        ft.Text(f"{message}"),
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
                        on_click=open_message
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                    
                messages_blocks = [create_block_message("Кирилл", "Математический маятник") for i in range(10)] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
                listv2 = ft.ListView(
                        controls=messages_blocks,
                        expand=True,
                    )

                messages =  flet.Container(
                                content=flet.Stack(
                                    [
                                    flet.Column(
                                        [
                                            flet.Row(
                                                [
                                                    flet.Text("Сообщения", font_family="Inter-Regular.ttf", size=26,),
                                                ], alignment=flet.MainAxisAlignment.CENTER
                                            ),
                                            listv2
                                        ], alignment=flet.MainAxisAlignment.START
                                    )    
                                    ]
                                ), 
                                width=page.width * 0.4, 
                                height=page.height * 0.4, 
                                bgcolor="#343537", 
                                border_radius=50,
                                border=ft.border.only(right=ft.border.BorderSide(1, "#5C5555"), bottom=ft.border.BorderSide(1, "#5C5555"))
                            )
                            
                
                
                
                solutions.margin = ft.margin.only(left=100)
                messages.margin = ft.margin.only(left=100, top=30)
                
                        

                main_page = ft.Row([
                    carousel, 
                    ft.Column(
                        [
                            solutions,
                            messages
                        ]
                    )
                ], width=page.width, alignment=flet.MainAxisAlignment.START, animate_opacity=500, height=page.height, key="main")
                
                def close_add_class_dialog(e):
                    add_class_dlg.open = False
                    page.update()
                    key = add_class(name_new_class.value, teacher_key)
                    classes_blocks.insert(-1, create_block_class(name_new_class.value, key))
                    classes_listv.update()
                    
                
                name_new_class = ft.TextField(label="Название класса", hint_text='8 "И"', color="white")
                add_class_dlg = ft.AlertDialog(
                    modal=False,
                    title=ft.Text("Введите название класса"),
                    content=name_new_class,
                    actions=[
                        ft.TextButton("Добавить класс", on_click=close_add_class_dialog),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                
                
                def add_new_class(e):
                    print("adding new class...")
                    page.dialog = add_class_dlg
                    add_class_dlg.open = True
                    page.update()
                    
                

                def open_class(key):
                    print(f"class № {key} is opening...")
                    students = download_classes(key)
                    class_cont_blocks.clear()
                    for i in students: class_cont_blocks.append(create_block_student_section(i[0], i[1]))
                    class_cont_blocks.append(ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373"))))
                    key_text.value = f"Ключ: {key}"
                    key_text.update()
                    print("open class!")
                    

                def create_block_class(class_name: str, class_key: str) -> ft.Container: 
                    block_content = ft.Container(
                        content=ft.Stack(
                            [
                                ft.Row(
                                    [
                                        ft.CircleAvatar(
                                            bgcolor="#6F45BB",
                                            content=ft.Text(class_name[:2]),
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
                        on_click=lambda _: open_class(class_key)
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                #download teacher's classes
                teacher_classes = download_classes(teacher_key)
                classes_blocks = [create_block_class(i[0], i[1]) for i in teacher_classes] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
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
                                                    flet.Text("Классы", font_family="Inter-Regular.ttf", size=27,),
                                                ], alignment=flet.MainAxisAlignment.CENTER
                                            ),
                                            classes_listv,
                                            ft.Container(content=ft.Row([ft.Text("Добавить класс", size=20, color="#A3DEFF")], alignment=ft.MainAxisAlignment.CENTER), width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")), on_click=add_new_class)
                                        ], alignment=flet.MainAxisAlignment.START
                                    )    
                                    ]
                                ), 
                                width=page.width * 0.3, 
                                height=page.height * 0.8, 
                                bgcolor="#343537", 
                                border_radius=50,
                                border=ft.border.only(left=ft.border.BorderSide(1, "#5C5555"), top=ft.border.BorderSide(1, "#5C5555"))
                            )
                            
                        ], alignment=flet.MainAxisAlignment.CENTER
                )
                
                def closs_new_task_deailog(e):
                    add_task_dlg.open = False
                    for i in tasks_blocks:
                        for j in i:
                            if j.bgcolor != None: j.bgcolor = None
                    key = key_text.value.split()[-1]
                    print(given_tasks, key)
                    if key != "": give_tasks(list(set(given_tasks)), key)
                    given_tasks.clear()
                    
                def select_task(e: ft.Container):
                    if e.bgcolor != "#57585C": e.bgcolor = "#57585C"; given_tasks.append(e.key)
                    else: e.bgcolor = None; given_tasks.remove(e.key)
                    print(e.key)
                    
                def create_block_task(name: str, key_name: str):
                    block_content = ft.Container(
                        content=ft.Stack(
                            [
                                ft.Row(
                                    [
                                        ft.Text(f"{name}"),
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
                        height=50,
                        key=key_name,
                        on_click=lambda _: select_task(block)
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                def change_tasks_class(e):
                    tasks_lv.controls=tasks_blocks[select_class.selected_index]
                    add_task_dlg.update()
                
                select_class = flet.CupertinoSlidingSegmentedButton(
                    selected_index=1,
                    thumb_color=flet.colors.BLUE_400,
                    on_change=change_tasks_class,
                    padding=flet.padding.symmetric(0, 10),
                    width=300,
                    controls=[
                        flet.Text("7 класс", font_family="Inter-Regular.ttf"),
                        flet.Text("8 класс", font_family="Inter-Regular.ttf"),
                        flet.Text("9 класс", font_family="Inter-Regular.ttf"),
                    ],
                )
                #creating menu with tasks
                tasks_blocks = [[create_block_task("Маятник", "7class_pendulum")], #7 class
                                [create_block_task("Пружинный маятник", "8class_springpendulum")], #8 class
                                [create_block_task("Скорость мячика от угла наклона бруска", "9class_speed of ball")]] #9 class
                tasks_lv = ft.ListView(
                        controls=tasks_blocks[select_class.selected_index],
                        expand=True,
                    )
                
                given_tasks = []
                
                add_task_dlg = ft.AlertDialog(
                    modal=False,
                    title=ft.Text("Выберете задания"),
                    content=ft.Stack([
                            ft.Column(
                                [
                                    ft.Row([
                                        select_class,
                                    ]),
                                    tasks_lv
                                ], height=400
                            )
                        ]),
                    actions=[
                        ft.TextButton("Выдать", on_click=closs_new_task_deailog),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                    
                )
                
                def add_new_task(e):
                    print("adding new task...")
                    page.dialog = add_task_dlg
                    add_task_dlg.open = True
                    page.update()


                def create_block_student_section(student: str, mail: str): 
                    block_content = ft.Container(
                        content=ft.Stack(
                            [
                                ft.Row(
                                    [
                                        ft.Text(student, size=20),
                                        ft.Text(mail, size=20),
                                        ft.PopupMenuButton(
                                            items=[
                                                ft.PopupMenuItem(text="Удалить ученика"),
                                                ft.PopupMenuItem(),  # divider
                                                ft.PopupMenuItem(
                                                    text="Посмотреть решения", checked=False, on_click=lambda x: print(10)
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
                    
                
                    
                class_cont_blocks = [] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
                class_listv = ft.ListView(
                        controls=class_cont_blocks,
                        expand=True,
                    )
                key_text = flet.Text("Ключ: ", font_family="Inter-Regular.ttf", size=26)
                class_section = flet.Row(
                        [
                            flet.Container(
                                content=flet.Stack(
                                    [
                                    flet.Column(
                                        [
                                            flet.Row(
                                                [
                                                    flet.Text("Фамилия Имя", font_family="Inter-Regular.ttf", size=26,),
                                                    flet.Text("Почта", font_family="Inter-Regular.ttf", size=26,),
                                                    ft.Row(
                                                        [
                                                            key_text,
                                                            ft.IconButton(icon=ft.icons.COPY, on_click=lambda _: pyperclip.copy(key_text.value.split()[1]), icon_color=ft.colors.WHITE)
                                                        ]
                                                    )
                                                ], alignment=flet.MainAxisAlignment.SPACE_AROUND, 
                                            ),
                                            class_listv,
                                            ft.Container(content=ft.Row([ft.Text("Выдать задание", size=20, color="#A3DEFF")], alignment=ft.MainAxisAlignment.CENTER), width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")), on_click=add_new_task)
                                            ], alignment=flet.MainAxisAlignment.START
                                    )    
                                    ]
                                ), 
                                width=700, 
                                height=page.height * 0.8,  
                                bgcolor="#343537", 
                                border_radius=50,
                                border=ft.border.only(right=ft.border.BorderSide(1, "#5C5555"), bottom=ft.border.BorderSide(1, "#5C5555"))
                            )
                            
                        ], alignment=flet.MainAxisAlignment.CENTER
                )
                
                classes_page = ft.Row([
                    classes, class_section
                ], width=page.width, alignment=flet.MainAxisAlignment.CENTER, animate_opacity=500, height=page.height, key="class")
                lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=False, on_scroll_interval=20, controls=[
                    main_page, classes_page
                ])

                count = 1



                page.add(lv)

                def check_item_clicked(e):
                    e.control.checked = not e.control.checked
                    page.update()

                def exit_acc(e):
                    print("Exit to registration menu")  
                    page.clean()
                    page.appbar = None
                    page.add(reg)
                    reg.opacity = 0
                    animate_reg(1)

                def main(e):
                    print("Main")
                    main_text.color = selected
                    class_text.color = white
                    lv.scroll_to(key="main", duration=500)
                    page.update()

                def classes(e):
                    print("Class")
                    main_text.color = white
                    class_text.color = selected
                    lv.scroll_to(key="class", duration=500)
                    page.update()

                main_text = ft.Text("Главная", font_family=font, color=selected, size=20)
                class_text = ft.Text("Классы", font_family=font, color=white, size=20)
                main_button = ft.TextButton(content=ft.Container(
                    content=ft.Row(controls=[main_text])), on_click=main)
                class_button = ft.TextButton(content=ft.Container(
                    content=ft.Row(controls=[class_text])), on_click=classes)

                app_bar = ft.AppBar(
                    title=ft.Row(
                        controls=[
                            main_button,
                            class_button
                        ], width=200
                    ),
                    center_title=True,
                    actions=[

                        ft.CircleAvatar(
                            bgcolor="#6F45BB",
                            content=ft.Text(name.value[0]),

                        ),
                        ft.IconButton(ft.icons.REFRESH, on_click=refresh),
                        ft.IconButton(ft.icons.EXIT_TO_APP, on_click=lambda _: exit()),
                    ],
                )

                page.appbar = app_bar

                start_time = time.time()
                while 1:
                    t = (time.time() - start_time) // 3 % len(contents)
                    slider.value = t 
                    slider.update()
                    t = int(t)
                    if switcher.content != contents[t % len(contents)]:
                        switcher.content = contents[t % len(contents)]
                        switcher.update()
                    page.update()
            else: #student window
                print("student")
                animate_reg(1)
                page.clean()
                width_for_switcher = page.width * 0.5
                heigth_for_switcher = page.height * 0.8
                contents = [flet.Container(
                                    flet.Text("1"), width=width_for_switcher, height=heigth_for_switcher, bgcolor="#343537", border_radius=50
                                ),
                            flet.Container(
                                    flet.Text("2"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.BLUE_300, border_radius=50
                                ),
                            flet.Container(
                                    flet.Text("3"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.PINK_300, border_radius=50
                                ),
                            flet.Container(
                                    flet.Text("4"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.GREEN_300, border_radius=50
                                ),
                            flet.Container(
                                    flet.Text("5"), width=width_for_switcher, height=heigth_for_switcher, bgcolor=flet.colors.PURPLE_300, border_radius=50
                                ),
                            ]
                contents_value = len(contents) - 1
                slider = flet.Slider(min=0, max=contents_value, divisions=contents_value, active_color="#6F45BB", width=width_for_switcher)
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
                def close_send_dialog(e):
                    page.dialog.open = False
                    filename, filepath = select_file_button.key
                    print([filepath])

                    add_solution(key.value, name.value, title_text.value, describe.value, filename, filepath)
                    page.update()
                    
                def pick_files_result(e: ft.FilePickerResultEvent):
                    select_file_button.text = (
                        ", ".join(map(lambda f: f.name, e.files))[:14] if e.files else "Выберете файл"
                    )
                    file_path = ", ".join(map(lambda f: f.path, e.files))
                    file_name = ", ".join(map(lambda f: f.name, e.files))
                    select_file_button.key = [file_name, file_path]
                    select_file_button.update()

                pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
                file_name, file_path = "", ""

                page.overlay.append(pick_files_dialog)
                
                select_file_button = ft.ElevatedButton(
                                            "Выберете файл",
                                            icon=ft.icons.UPLOAD_FILE,
                                            on_click=lambda _: pick_files_dialog.pick_files(
                                                allow_multiple=True
                                            ),
                                            key=["name", "path"]
                                        )
                title_text = ft.Text("Theme name")
                # def print_value(e):
                #     print(e)
                
                
                send_dialog = ft.AlertDialog(
                    modal=False,
                    title=title_text,
                    content=ft.Row(
                        [
                            describe := ft.TextField(
                                label="Описание вашей работы",
                                multiline=True,
                                min_lines=1,
                                max_lines=7,
                                width=350,
                                # on_change=lambda _: print_value(describe.value)
                            )
                        ], width=350
                    ),
                
                    actions=[
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        select_file_button,
                                        ft.ElevatedButton(
                                            "Отправить",
                                            icon=ft.icons.SEND,
                                            on_click=lambda _: close_send_dialog(send_dialog)
                                        ),
                                        # ft.TextButton("Отправить", on_click=close_send_dialog),
                                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                ),
                            ]
                        ),
                    ],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                
                def send_solution(key):
                    title_text.value = labs[key][0]
                    send_dialog.title=ft.Text(labs[key][0])
                    page.dialog = send_dialog
                    send_dialog.open = True
                    page.update()
                    
                def open_task(e: ft.Container):
                    open_lab(e.key)

                def create_block(theme: str, key: str) -> ft.Container: 
                    block_content = ft.Container(
                        content=ft.Stack(
                            [
                                ft.Row(
                                    [
                                        ft.Row(
                                            [
                                                ft.CircleAvatar(
                                                    bgcolor="#6F45BB",
                                                    content=ft.Text(theme[0]),
                                                    tooltip=theme
                                                ),
                                                ft.Text(f"Тема: {theme}"),
                                            ]
                                        ),
                                        ft.ElevatedButton(text="Отправить решение", 
                                            bgcolor="#7B9467", 
                                            color="#FFFFFF", on_click=lambda _: send_solution(key))
                                    ], ft.MainAxisAlignment.SPACE_BETWEEN
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
                        key=key,
                        on_click=lambda _: open_task(block)
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                def refresh(e):
                    tasks = download_tasks(key.value)
                    blocks.clear()
                    for i in tasks: blocks.append(create_block(take_name(i), i))
                    blocks.append(ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373"))))
                    listv.update()
                    print("Done Refresh")
                
                tasks = download_tasks(key.value)
                blocks = [create_block(take_name(i), i) for i in tasks] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
                listv = ft.ListView(
                        controls=blocks,
                        expand=True,
                    )

                solutions = flet.Container(
                                content=flet.Stack(
                                    [
                                    flet.Column(
                                        [
                                            flet.Row(
                                                [
                                                    flet.Text("Задания", font_family="Inter-Regular.ttf", size=26,),
                                                ], alignment=flet.MainAxisAlignment.CENTER
                                            ),
                                            listv
                                        ], alignment=flet.MainAxisAlignment.START
                                    )    
                                    ]
                                ), 
                                width=page.width * 0.4, 
                                height=page.height * 0.4, 
                                bgcolor="#343537", 
                                border_radius=50
                            )
                
                #messages box

                def open_message(e):
                    print("message opening...")

                def create_block_message(student_name: str, message: str) -> ft.Container: 
                    if len(message) > 30:
                        message = message[:30] + "..."
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
                                        ft.Text(f"{message}"),
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
                        on_click=open_message
                    )
                    block_content.margin = ft.margin.all(10)
                    block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
                    return block
                
                    
                messages_blocks = [create_block_message("Кирилл", "Математический маятник") for i in range(10)] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
                listv2 = ft.ListView(
                        controls=messages_blocks,
                        expand=True,
                    )

                messages =  flet.Container(
                                content=flet.Stack(
                                    [
                                    flet.Column(
                                        [
                                            flet.Row(
                                                [
                                                    flet.Text("Сообщения", font_family="Inter-Regular.ttf", size=26,),
                                                ], alignment=flet.MainAxisAlignment.CENTER
                                            ),
                                            listv2
                                        ], alignment=flet.MainAxisAlignment.START
                                    )    
                                    ]
                                ), 
                                width=page.width * 0.4, 
                                height=page.height * 0.4, 
                                bgcolor="#343537", 
                                border_radius=50
                            )
                            
                
                
                
                solutions.margin = ft.margin.only(left=100)
                messages.margin = ft.margin.only(left=100, top=30)
                
                        

                main_page = ft.Row([
                    carousel, 
                    ft.Column(
                        [
                            solutions,
                            messages
                        ]
                    )
                ], width=page.width, alignment=flet.MainAxisAlignment.START, animate_opacity=500, height=page.height, key="main")
                
                page.add(main_page)
                
                def check_item_clicked(e):
                    e.control.checked = not e.control.checked
                    page.update()

                def exit_acc(e):
                    print("Exit to registration menu")  
                    
                



                app_bar = ft.AppBar(
                    title=ft.Row(
                        controls=[
                        ], width=200
                    ),
                    center_title=True,
                    actions=[

                        ft.CircleAvatar(
                            bgcolor="#6F45BB",
                            content=ft.Text(name.value[0]),

                        ),
                        ft.IconButton(ft.icons.REFRESH, on_click=refresh),
                        ft.IconButton(ft.icons.EXIT_TO_APP, on_click=exit_acc),
                    ],
                )

                page.appbar = app_bar

                start_time = time.time()
                while 1:
                    t = (time.time() - start_time) // 3 % len(contents)
                    slider.value = t 
                    slider.update()
                    t = int(t)
                    if switcher.content != contents[t % len(contents)]:
                        switcher.content = contents[t % len(contents)]
                        switcher.update()
                    page.update()
        else:
            #registration user
            print("Not autorisated")
            if not type_int.selected_index and check_username(name.value) and check_email(email.value):
                print("starting regestration...")
                reg_dialog_open()
                # send_auth_mail(email.value, auth_key)

            else:
                print("User can't to registration")
                return None
        
        
        
    name, email, key = flet.TextField(label="Имя", hint_text="Иван Иванов", color="white"), flet.TextField(
        label="email", hint_text="email@mail.com", color="white"), flet.TextField(label="Ключ класса (при его наличии)", hint_text="key2134", color="white")
    type_int = flet.CupertinoSlidingSegmentedButton(
        selected_index=1,
        thumb_color=flet.colors.BLUE_400,
        on_change=lambda e: print(f"selected_index: {e.data}"),
        padding=flet.padding.symmetric(0, 10),
        width=200,
        controls=[
            flet.Text("Я учитель", font_family="Inter-Regular.ttf"),
            flet.Text("Я ученик", font_family="Inter-Regular.ttf"),
        ],
    )
    auth_button = flet.ElevatedButton(color=flet.colors.BLUE_400, bgcolor=flet.colors.GREY_900, height=80, on_click=autorisation, content=flet.Text(
        "Авторизироваться", font_family="Inter-Regular.ttf"
    ))
    reg = flet.Row(
        [
            flet.Container(
                content=flet.Stack(
                    controls=[

                        flet.Column(
                            controls=[
                                flet.Row(
                                    controls=[
                                        flet.Text("Регистрация",
                                                  size=20, color="white", font_family="Inter-Regular.ttf"),
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                name, email, key,
                                flet.Row(
                                    controls=[
                                        type_int,
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                ),
                                flet.Divider(
                                    height=70, color="transparent"),
                                flet.Row(
                                    controls=[
                                        auth_button,
                                    ], alignment=flet.MainAxisAlignment.CENTER
                                )

                            ], alignment=flet.MainAxisAlignment.START
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
        ], alignment=flet.MainAxisAlignment.CENTER, animate_opacity=500
    )
    reg.opacity = 0

    randomize(None)

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.spacing = 30

    Login_button = ElevatedButton(on_click=button_clicked, width=300, height=70, content=flet.Text("Войти", size=20, font_family="Inter-Regular.ttf"))
    Login_button.opacity = 0
    page.add(canvas, Login_button)
    Login_button.focus()

    while 1:
        if time.time() - start_time >= 0.1:
            assemble(1)
            break
    while 1:
        i = 1
        if time.time() - start_time >= 2.1 * i:

            randomize2(1)
            break


flet.app(main)
