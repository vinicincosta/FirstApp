import flet as ft
from flet import AppBar, Text, View
from flet.auth import user
from flet.core.colors import Colors

class User():
    def __init__(self, salario, nome, profissao):
        self.nome = nome
        self.salario = salario
        self.profissao = profissao

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_profissao(e):
        if input_profissao.value == '' or input_salario.value == '' or input_nome.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            obj_user = User(
                profissao=input_profissao.value,
                salario=input_salario.value,
                nome=input_nome.value
            )

            lista.append(obj_user)
            input_profissao.value = ''
            input_salario.value = ''
            input_nome.value = ''
            page.overlay.append(msg_sucesso)  # overlay sob escreve a página
            msg_sucesso.open = True
            page.update()

            # lista.append(input_profissao.value and input_salario.value)
            # input_profissao.value = ''
            # input_salario.value = ''
            # page.overlay.append(msg_sucesso)  # overlay sob escreve a página
            # msg_sucesso.open = True
            # page.update()


    def exibir_lista(e):
        lv_profissao.controls.clear()

        for user in lista:
            lv_profissao.controls.append(
                ft.Text(value=f'{user.profissao} - {user.salario} - {user.nome}',)
            )
        page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_nome,
                    input_profissao,
                    input_salario,

                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_profissao(e)
                    ),
                    ft.Button(
                        text="Exibir Lista",
                        on_click=lambda _: page.go('/segunda')
                    )

                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)

            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Exibir informações"), bgcolor=Colors.SECONDARY_CONTAINER),
                        
                        lv_profissao,

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = ft.SnackBar(

        content=ft.Text("campos salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text('campos não podem estar vazios'),
        bgcolor=Colors.RED
    )

    input_profissao = ft.TextField(label="Profissao")
    input_salario = ft.TextField(label="Salario")
    input_nome = ft.TextField(label="Nome")

    lv_profissao = ft.ListView(
        height=500
    )


    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)