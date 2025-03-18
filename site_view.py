import flet as ft

def main(page: ft.Page):
    page.title = "Пример приложения"
    page.window_icon = "phis_icon.ico"  # Укажите путь к вашей иконке

    # Добавление элементов на страницу
    page.add(ft.Text("Привет, мир!"))

ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)