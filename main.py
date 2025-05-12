import flet as ft

def main(page: ft.Page):
    page.title = "تطبيق Flet بسيط"
    page.add(
        ft.Text("مرحبًا بك في Flet!", size=30),
        ft.ElevatedButton(text="اضغطني", on_click=lambda e: print("تم الضغط"))
    )

ft.app(target=main)
