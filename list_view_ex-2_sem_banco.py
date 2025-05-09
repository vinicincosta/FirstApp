import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Page
from flet.auth import user
from flet.core.alignment import Alignment

from models import *
class User():
    def __init__(self, titulo, descricao, autor, categoria):
        self.titulo = titulo
        self.descricao = descricao
        self.autor = autor
        self.categoria = categoria

def main(page: Page):
    # Configuração da página
    page.title = 'Eercicio 2'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def add_titulo_lista(e):
        lv_livros.controls.clear()
        for user in lista:
            lv_livros.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f'Título - {user.titulo}'),
                    subtitle=ft.Text(f'Categoria - {user.categoria}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f'Detalhes',
                                             on_click=lambda _: page.go('/terceira')),

                        ],
                    )
                )
            )
        page.update()


    # Definição de funções
    lista = []
    def salvar_livros(e):
        if (input_titulo.value == '' or input_autor.value == ''
                or input_categoria.value == '' or input_descricao.value == ''):
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = User(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                autor=input_autor.value,
                categoria=input_categoria.value,
            )

            lista.append(obj_user)
            input_descricao.value = ''
            input_categoria.value = ''
            input_autor.value = ''
            input_titulo.value = ''
            page.overlay.append(msg_sucesso)  # overlay sob escreve a página
            msg_sucesso.open = True

            page.update()

    def exibir_lista(e):
        lv_livros.controls.clear()
        for livro in lista:
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
                            subtitle=ft.Text("Here is a second title.."),
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

    def gerecia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Livro'), bgcolor=Colors.BLUE_ACCENT, center_title=True),
                    input_titulo,
                    input_descricao,
                    input_autor,
                    input_categoria,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_livros(e)
                    ),
                    ft.Button(
                        text="Exibir Lista",
                        on_click=lambda _: page.go('/segunda')
                    ),


                ]
            )
        )

        if page.route == '/segunda':
            add_titulo_lista(e)
            page.views.append(

                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Informações'), bgcolor=Colors.BLUE_ACCENT),
                       lv_livros,
                        ft.Button(
                            text="Exibir terceira teste",
                            on_click=lambda _: page.go('/terceira')
                        )
                    ],

                )
            )

        if page.route == '/terceira':
            exibir_lista(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text('Detalhes'), bgcolor=Colors.BLUE_ACCENT),
                        lv_livros,
                    ]
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
    input_categoria = ft.TextField(label='Categoria', hint_text='insira categoria', col=4,hover_color=Colors.BLUE)
    input_autor = ft.TextField(label='Autor', hint_text='insira autor', col=4,hover_color=Colors.BLUE)

    lv_livros = ft.ListView(
        height=700,
        spacing = 5,
        divider_thickness = 2
    )




ft.app(main)
