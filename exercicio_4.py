import flet as ft
from datetime import datetime
from flet.core import page


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Minha aplicação Flet'
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções
    def exibir_ano(e):
        try:
            tempo = datetime.now()
            input_formatado = datetime.strptime(input_ano.value, '%d/%m/%Y')

            # diferenca_dias = abs((tempo - input_formatado).days)
            # diferenca_anos = diferenca_dias // 365

            teste_data = tempo.year - input_formatado.year
            teste_mes = tempo.month > input_formatado.month

            if tempo.month == input_formatado.month and tempo.day >= input_formatado.day:
                idade = teste_data
            else:
                idade = teste_data - 1

            if idade < 18:
                txt_resultado_ano.value = 'Você é menor de idade'
                txt_resultado_idade.value = f'Sua idade é {idade} ano(s)'
            else:
                txt_resultado_ano.value = 'Você é maior de idade'
                txt_resultado_idade.value = f'Sua idade é {idade} ano(s)'
            page.update()
        except ValueError:
            print("Valor inválido, tente novamente")



    # Criação de componentes
    input_ano = ft.TextField(label='Digite o ano de nascimento')
    btn_enviar = ft.FilledButton(text='Enviar', width=page.window.width, on_click=exibir_ano)
    txt_resultado_ano = ft.TextField(value='')
    txt_resultado_idade = ft.TextField(value='')

    # Construir o layout
    page.add(
        ft.Column(
            [
                input_ano,
                btn_enviar,
                txt_resultado_ano,
                txt_resultado_idade,


            ],
        )
    )
    # page.add(ft.TextField (label = 'digite aq'))


ft.app(main)
