from tkinter import Text

import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Page


def main(page: Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def gerecia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Livro'), bgcolor=Colors.PRIMARY_CONTAINER),
                    ElevatedButton(text='Navegar', on_click=lambda _: page.go('/segunda')),
                    input_titulo,
                    input_descricao,
                    input_autor,
                    input_categoria


                ]
            )
        )

        if page.route == '/segunda':
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Informações'), bgcolor=Colors.RED),
                        ft.TextField(value=f'Titulo: {input_titulo.value} '),
                        ft.TextField(value=f'Descrição: {input_descricao.value}'),
                        ft.TextField(value=f'Categoria: {input_categoria.value}'),
                        ft.TextField(value=f'Autor: {input_autor.value}')

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
    input_titulo = ft.TextField(label='Titulo', hint_text='insira titulo', col=4)
    input_descricao = ft.TextField(label='Descrição', hint_text='insira descrição', col=4)
    input_categoria = ft.TextField(label='Categoria', hint_text='insira categoria', col=4)
    input_autor = ft.TextField(label='Autor', hint_text='insira autor', col=4)


ft.app(main)
