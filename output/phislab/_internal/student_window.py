from time import sleep
import flet as ft, flet
import time

def main(page: ft.Page, name="Денис"):
    page.title = "Auto-scrolling ListView"
    page.title = "registration"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_maximized = True
    page.theme_mode = "dark"
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
        print(select_file_button.key)
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
    
    send_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Введите название класса"),
        content=ft.Row(
            [
                ft.TextField(
                    label="Описание вашей работы",
                    multiline=True,
                    min_lines=1,
                    max_lines=7,
                    width=350
                ),
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
                                on_click=close_send_dialog
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
        send_dialog.title=ft.Text(key)
        page.dialog = send_dialog
        send_dialog.open = True
        page.update()
        
    def open_solution(e):
        print("Solutions opening...")

    def create_block(theme: str, key: str) -> ft.Container: 
        block_content = ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        [
                            ft.CircleAvatar(
                                bgcolor="#6F45BB",
                                content=ft.Text(theme[0]),
                                tooltip=theme
                            ),
                            ft.Text(f"Тема: {theme}"),
                            ft.ElevatedButton(text="Выполнить", 
                                bgcolor="#7B9467", 
                                color="#FFFFFF", on_click=lambda _: send_solution(key))
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
    
        
    blocks = [create_block("Математический маятник", "Математический маятник") for i in range(10)] + [ft.Container(width=700, height=50, border=ft.border.only(top=ft.border.BorderSide(1, "#767373")))]
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