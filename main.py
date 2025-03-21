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
        txt_resultado.value = input_nome.value
        page.update()


    # Criação de componentes
    input_nome = ft.TextField(label='Nome', hint_text='Digite seu nome', col=4)
    input_email = ft.TextField(label='E-mail', hint_text='Digite seu e-mail', col=4)
    # submit_button = ft.TextButton(text='Confirmar')
    btn_enviar = ft.FilledButton(text='Enviar', width=page.window.width, on_click=exibir_nome)

    txt_resultado = ft.Text(value='')

    # Construir o layout
    page.add(
         ft.Column(
              [
                 input_nome,
                 btn_enviar,
                 txt_resultado,
              ],
         )
    )
    # page.add(ft.TextField (label = 'digite aq'))


ft.app(main)