import asyncio
import flet as ft # 1.

def main(page: ft.Page): # 2.
    page.title = "Flet counter example" # 3.
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # 4.

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100, read_only=True) # 5.
    history: list[int] = []

    def minus_click(e): # 6.
        txt_number.value = str(int(txt_number.value) - 1)
        history.append(-1)
        page.update()

    def plus_click(e): # 6.
        txt_number.value = str(int(txt_number.value) + 1)
        history.append(1)
        page.update()

    async def replay_click(e):
        if not history:
            return

        txt_number.value = "0"
        page.update()

        running_total = 0
        for step in history:
            running_total += step
            txt_number.value = str(running_total)
            page.update()
            await asyncio.sleep(0.3)

    page.add( # 7.
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
                ft.IconButton(ft.Icons.PLAY_ARROW, on_click=replay_click, tooltip="Replay changes"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main) # 8.
