import flet as ft
from django.contrib.admin.templatetags.admin_list import result_list
from flet import AppBar, ElevatedButton, Text, Colors, View, Page
from flet.auth import user
from flet.core.alignment import Alignment

from models import *


def main(page: Page):
    # Configuração da página
    page.title = 'Eercicio 2'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def add_titulo_lista(e):
        lv_livros.controls.clear()
        lv_resultado = select(Livro)
        resul_livros = db_session.execute(lv_resultado).scalars().all()

        for livro in resul_livros:
            lv_livros.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(f'Título - {livro.titulo}'),
                    subtitle=ft.Text(f'Categoria - {livro.categoria}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f'Detalhes',
                                             on_click=lambda _, l=livro: exibir_detalhes(l)),

                        ],
                    )
                )
            )
        page.update()


    def exibir_detalhes(livro):
        txt_resultado.value = (f'Titulo: {livro.titulo}\n'
                               f'Categoria: {livro.categoria}\n'
                               f'Autor: {livro.autor}\n'
                               f'Descrição: {livro.descricao}')
        page.go('/terceira')



    def salvar_livros(e):
        if (input_titulo.value == '' or input_autor.value == ''
                or input_categoria.value == '' or input_descricao.value == ''):
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = Livro(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                autor=input_autor.value,
                categoria=input_categoria.value,
            )

            obj_user.save()
            input_descricao.value = ''
            input_categoria.value = ''
            input_autor.value = ''
            input_titulo.value = ''
            page.overlay.append(msg_sucesso)  # overlay sob escreve a página
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_livros.controls.clear()
        lv_resultado = select(Livro)
        resultado_livros = db_session.execute(lv_resultado).scalars().all()
        for livro in resultado_livros:
            lv_livros.controls.append(
                ft.Text(value=f'Título: {livro.titulo}\n'
                              f'Descrição:  {livro.descricao}\n'
                              f'Autor:  {livro.autor} \n'
                              f'Categoria: {livro.categoria}\n', )
            )
        page.update()

    def example():
        return ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text("One-line list tile"),
                        ),
                        ft.ListTile(title=ft.Text("One-line dense list tile"), dense=True),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.SETTINGS),
                            title=ft.Text("One-line selected list tile"),
                            selected=True,
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="/logo.svg", fit=ft.ImageFit.CONTAIN),
                            title=ft.Text("One-line with leading control"),
                        ),
                        ft.ListTile(
                            title=ft.Text("One-line with trailing control"),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ALBUM),
                            title=ft.Text("One-line with leading and trailing controls"),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.SNOOZE),
                            title=ft.Text("Two-line with leading and trailing controls"),
                            subtitle=ft.Text("Here is a second title."),
                            trailing=ft.PopupMenuButton(
                                icon=ft.Icons.MORE_VERT,
                                items=[
                                    ft.PopupMenuItem(text="Item 1"),
                                    ft.PopupMenuItem(text="Item 2"),
                                ],
                            ),
                        ),
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=10),
            )
        )

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Livro', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT, center_title=True),
                    input_titulo,
                    input_descricao,
                    input_autor,
                    input_categoria,
                    ft.Button(
                        text="Salvar",
                        bgcolor=Colors.BLUE_ACCENT,
                        color=Colors.BLACK,

                        on_click=lambda _: salvar_livros(e),

                    ),
                    ft.Button(
                        text="Exibir Lista",
                        bgcolor=Colors.BLUE_ACCENT,
                        color=Colors.BLACK,
                        on_click=lambda _: page.go('/segunda')
                    ),

                ],
                bgcolor=Colors.BLUE_GREY_700,
            )

        )

        if page.route == '/segunda' or page.route == '/terceira':
            add_titulo_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Livros', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT),
                        lv_livros,
                    ],
                    bgcolor=Colors.BLUE_GREY_700,
                )
            )

        if page.route == '/terceira':
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text('Detalhes', font_family="Arial", ), bgcolor=Colors.BLUE_ACCENT),
                        # lv_livros,
                        txt_resultado
                    ],
                    bgcolor=Colors.BLUE_GREY_700,
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

    # Criação de componentes
    msg_sucesso = ft.SnackBar(

        content=ft.Text("campos salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text('campos não podem estar vazios'),
        bgcolor=Colors.RED
    )

    input_titulo = ft.TextField(label='Titulo', hint_text='insira titulo', col=4, hover_color=Colors.BLUE)
    input_descricao = ft.TextField(label='Descrição', hint_text='insira descrição', col=4, hover_color=Colors.BLUE)
    input_categoria = ft.TextField(label='Categoria', hint_text='insira categoria', col=4, hover_color=Colors.BLUE)
    input_autor = ft.TextField(label='Autor', hint_text='insira autor', col=4, hover_color=Colors.BLUE)
    txt_resultado = ft.Text('', font_family="Arial", size=20, color=Colors.BLACK)

    lv_livros = ft.ListView(
        height=700,
        spacing=5,
        divider_thickness=2
    )


ft.app(main)
