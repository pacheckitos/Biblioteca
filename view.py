from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Input, Button, TabbedContent
from model import biblioteca

class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Bem-vindo à biblioteca. Selecione um menu para realizar operações.")
        yield Button("Menu de leitores", id = "button_menu_leitores")
        yield Button("Menu de livros", id = "button_menu_livros")
        yield Button("Empréstimos", id = "button_menu_emprestimos") 
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "button_menu_leitores":
                self.app.switch_screen("menu_leitores")



class TelaCadastrarLivros(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Cadastro de livros")
        yield Footer()

class TelaMenuLeitores(Screen):
    def compose(self):
        yield Header(show_clock = True)
        with TabbedContent(initial="jessica"):
            with TabPane("Leto", id="leto"):
                yield Markdown(LETO)
            with TabPane("Jessica", id="jessica"):
                yield Markdown(JESSICA)
            with TabPane("Paul", id="paul"):
                yield Markdown(PAUL)
        '''with TabbedContent():
            with TabPane("Cadastrar de Leitor", id = "cadastro_leitores"):
                yield Markdown(CADASTRO)
            with TabPane("Deletar Leitor"):
                pass'''
        yield Footer()
        

class TelaCadastrarLeitores(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Informe o nome do leitor:")
        yield Input(placeholder = "Nome completo")
        yield Static("Informe o CPF do leitor:")
        yield Input(placeholder = "CPF")
        yield Button("Cadastrar leitor", id = "button_cadastrar_leitor")
        yield Footer()