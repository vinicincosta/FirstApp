import flet as ft
from flet.core import page


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição  de funções
    def exebir_numero (e):
        if int(input_numero.value) % 2 == 0:
            txt_resultado_numero.value = 'par'
        else:
            txt_resultado_numero.value = 'impar'

        page.update()

    # Criação de componentes
    input_numero = ft.TextField(label ='digite um numero')
    btn_enviar = ft.FilledButton(text='Enviar', width=page.window.width, on_click=exebir_numero)
    txt_resultado_numero = ft.TextField(value='')
    # Criação de componentes

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero,
                btn_enviar,
                txt_resultado_numero,
            ],
        )
    )








ft.app(main)