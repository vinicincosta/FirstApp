from tkinter import Text

import flet as ft

from flet import AppBar, ElevatedButton, Text, Colors, View, Page


def main(page: Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição  de funções

    def gerecia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Home'), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text='Navegar', on_click=lambda _: page.go('/segunda')),
                    input_nome,

                ]
            )
        )

        if page.route == '/segunda':
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Segunda tela'), bgcolor=Colors.SECONDARY_CONTAINER),
                        ft.TextField(value=f'{input_nome.value}'),
                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerecia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

    # Criação de componentes
    input_nome = ft.TextField(label='Nome', hint_text='Digite seu nome', col=4)


ft.app(main)
