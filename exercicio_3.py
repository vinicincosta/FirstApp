import flet as ft
from flet.core import page


def main(page: ft.Page,):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # Definição  de funções

    def somar(e):
        try:
            soma = int(input_num1.value) + int(input_num2.value)
            text_resultado.value = f'O Resultado é {soma}'
            page.update()
        except ValueError:
            text_resultado.value = 'Valor invalido'
            print('valor invalido')
            page.update()


    def subtrair(e):
        try:
            sub = int(input_num1.value) - int(input_num2.value)
            text_resultado.value = f' O Resultado é{sub}'
            page.update()
        except ValueError:
            text_resultado.value = 'Valor invalido'
            print('valor invalido')
            page.update()

    def multiplicar(e):
        try:
            multip = int(input_num1.value) * int(input_num2.value)
            text_resultado.value = f' O Resultado é {multip}'
            page.update()
        except ValueError:
            text_resultado.value = 'Valor invalido'
            print('valor invalido')
            page.update()

    def dividir(e):
        try:
            divi = int(input_num1.value) / int(input_num2.value)
            text_resultado.value = f' O Resultado é {divi}'
            page.update()
        except ValueError:
            text_resultado.value = 'Valor invalido'
            print('valor invalido')
            page.update()

    # Criação de componentes
    input_num1 = ft.TextField(label='Digite um numero')
    input_num2 = ft.TextField(label='Digite outro numero')
    text_resultado = ft.TextField(label='Resultado', value='')

    submit_button_soma = ft.TextButton(
        text='Somar',
        on_click=somar,
    )
    submit_button_sub = ft.TextButton(
        text='Subtrair',
        on_click=subtrair,
    )

    submit_button_multi = ft.TextButton(
        text='Multiplicar',
        on_click=multiplicar,
    )

    submit_button_divi = ft.TextButton(
        text='Dividir',
        on_click=dividir,
    )


    # Construir o layout
    page.add(
        ft.Column(
            [
                input_num1,
                input_num2,
                submit_button_soma,
                submit_button_sub,
                submit_button_multi,
                submit_button_divi,
                text_resultado
            ],
        )
    )
ft.app(main)