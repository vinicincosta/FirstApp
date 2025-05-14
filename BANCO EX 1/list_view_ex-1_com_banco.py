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

    def add_usuario_lista(e):
        lv_usuario.controls.clear()
        lv_resultado = select(Usuario)
        resul_usuario = db_session.execute(lv_resultado).scalars().all()

        for usuario in resul_usuario:
            lv_usuario.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f'Nome - {usuario.nome}'),
                    subtitle=ft.Text(f'Informações'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f'Detalhes',
                                             on_click=lambda _, u=usuario: exibir_detalhes(u)),

                        ],
                    )
                )
            )
        page.update()


    def exibir_detalhes(usuario):
        txt_resultado.value = (f'Nome: {usuario.nome}\n '
                               f'Profissão: {usuario.profissao}\n '
                               f'Salário: {usuario.salario}'
                               )
        page.go('/terceira')



    def salvar_usuarios(e):
        try:
            global obj_user
            if (input_nome.value == '' or input_salario.value == ''
                    or input_profissao.value == '' ):
                page.overlay.append(msg_error)
                msg_error.open = True
                page.update()
            else:

                    obj_user = Usuario(
                        nome=input_nome.value,
                        profissao=input_profissao.value,
                        salario=float(input_salario.value),
                    )

                    obj_user.save()
                    input_nome.value = ''
                    input_profissao.value = ''
                    input_salario.value = ''

                    page.overlay.append(msg_sucesso)  # overlay sob escreve a página
                    msg_sucesso.open = True
                    page.update()

        except ValueError:
            txt_erro.value = 'valor inserido invalido'
            print('ddddddddd')
            page.update()
            return




    # def exibir_lista(e):
    #     lv_usuario.controls.clear()
    #     lv_resultado = select(Usuario)
    #     resultado_usuario = db_session.execute(lv_resultado).scalars().all()
    #     for usuario in resultado_usuario:
    #         lv_usuario.controls.append(
    #             ft.Text(value='Nome: {usuario.nome}\n'
    #                            f'Profissão: {usuario.profissao}\n'
    #                            f'Salário: {usuario.salario}\n' )
    #         )
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
                    AppBar(title=Text('Usuário', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT, center_title=True),
                    input_nome,
                    input_profissao,
                    input_salario,
                    txt_erro,




                    ft.Button(
                        text="Salvar",
                        bgcolor=Colors.BLUE_ACCENT,
                        color=Colors.BLACK,

                        on_click=lambda _: salvar_usuarios(e),

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
            txt_erro.value = ""
            add_usuario_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Usuarios', font_family="Arial"), bgcolor=Colors.BLUE_ACCENT),
                        lv_usuario,

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

    input_profissao = ft.TextField(label="Profissao", col=4, hover_color=Colors.BLUE)
    input_salario = ft.TextField(label="Salario", col=4, hover_color=Colors.BLUE)
    input_nome = ft.TextField(label="Nome", col=4, hover_color=Colors.BLUE)
    txt_resultado = ft.Text('', font_family="Arial", size=20, color=Colors.BLACK)
    txt_erro = ft.Text('', font_family="Arial", size=20, color=Colors.RED)



    lv_usuario = ft.ListView(
        height = 700,
        spacing = 5,
        divider_thickness = 2
    )

def example():
    return ft.Column(
        controls=[
            ft.Text("Cupertino slider:"),
            ft.CupertinoSlider(),
            ft.Text("Material slider:"),
            ft.Slider(),
            ft.Text("Adaptive slider:"),
            ft.Slider(
                adaptive=True,
                tooltip=ft.Tooltip(
                    message="Adaptive Slider shows as CupertinoSlider on macOS and iOS and as Slider on other platforms",
                ),
            ),
        ],
    )


def example():
    return ft.Column(controls=[
        ft.Text("Slider with value:"),
        ft.Slider(value=0.3),
        ft.Text("Slider with a custom range and label:"),
        ft.Slider(min=0, max=100, divisions=10, label="{value}%")
    ]
    )

ft.app(main)
