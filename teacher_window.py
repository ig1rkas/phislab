from time import sleep
import flet as ft, flet
import time
from db import get_solutions, get_file_solution
from pprint import pprint

def main(page: ft.Page):
    page.title = "Auto-scrolling ListView"
    page.title = "registration"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = "dark"
    name = "Денис Пожидаев"
    font = "Inter-Regular.ttf"
    selected = "#6F45BB"
    white = "#FFFFFF"
    page_number = 1
    teacher_key = "IjQ3jCeO"
    width_for_switcher = page.width * 0.6
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
            on_click=open_solution
        )
        block_content.margin = ft.margin.all(10)
        block.border = ft.border.only(top=ft.border.BorderSide(1, "#767373"))
        return block
    
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
    
    def add_new_class(e):
        print("adding new class...")

    def open_class(e):
        print("class opening...")

    def create_block_class(class_name: str) -> ft.Container: 
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
    
        
    classes_blocks = [create_block_class('10 "И" Класс') for i in range(14)] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
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
                    width=page.width * 0.3, 
                    height=page.height * 0.8, 
                    bgcolor="#343537", 
                    border_radius=50
                )
                
            ], alignment=flet.MainAxisAlignment.CENTER
    )
    
    def closs_new_task_deailog(e):
        add_task_dlg.open = False
        for i in tasks_blocks:
            for j in i:
                if j.bgcolor != None: j.bgcolor = None
        print(given_tasks)
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
    
    tasks_blocks = [[create_block_task("bla", "blaaa") for i in range(10)], 
                    [create_block_task("blabla", "blaaa") for i in range(10)],
                    [create_block_task("blablabla", "blaaa") for i in range(10)]]
    tasks_lv = ft.ListView(
            controls=tasks_blocks[select_class.selected_index],
            expand=True,
        )
    
    given_tasks = []
    
    add_task_dlg = ft.AlertDialog(
        modal=True,
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
                    height=page.height * 0.8,  
                    bgcolor="#343537", 
                    border_radius=50
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
                content=ft.Text(name[0]),

            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ], icon=ft.icons.NOTIFICATIONS
            ),
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



ft.app(target=main)