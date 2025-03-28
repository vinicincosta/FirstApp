import flet as ft
from flet.core import page


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição  de funções
    def exibir_nome(e):
        txt_resultado.value = input_nome.value + ' ' + input_sobrenome.value

        page.update()

    # Criação de componentes
    input_nome = ft.TextField(label='Nome', hint_text='Digite seu nome', col=4)
    input_sobrenome = ft.TextField(label='Sobrenome', hint_text='Digite seu nome', col=4)
    btn_enviar = ft.FilledButton(text='Enviar', width=page.window.width, on_click=exibir_nome)
    txt_resultado = ft.TextField(label='Seu nome será', hint_text='Digite seu nome', col=4, value='')

    # Construir o layout

    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,

            ],
        )
    )
ft.app(main)