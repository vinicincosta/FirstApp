import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Page

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
        for user in lista:
            lv_livros.controls.append(
                ft.Text(value=f'{user.titulo} - {user.descricao} - {user.autor} - {user.categoria}', )
            )
        page.update()


    def gerecia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Livro'), bgcolor=Colors.PRIMARY_CONTAINER),
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
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text('Informações'), bgcolor=Colors.RED),
                       lv_livros,
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
    msg_sucesso = ft.SnackBar(

        content=ft.Text("campos salvo com sucesso"),
        bgcolor=Colors.GREEN
    )

    msg_error = ft.SnackBar(
        content=ft.Text('campos não podem estar vazios'),
        bgcolor=Colors.RED
    )

    input_titulo = ft.TextField(label='Titulo', hint_text='insira titulo', col=4)
    input_descricao = ft.TextField(label='Descrição', hint_text='insira descrição', col=4)
    input_categoria = ft.TextField(label='Categoria', hint_text='insira categoriaa', col=4)
    input_autor = ft.TextField(label='Autor', hint_text='insira autor', col=4)

    lv_livros = ft.ListView(
        height=500
    )

ft.app(main)
