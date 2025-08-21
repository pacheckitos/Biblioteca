from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from model import biblioteca

class TelaInicial(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Bem-vindo à biblioteca")
        yield Footer()

class TelaCadastrarLivros(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Cadastro de livros")
        yield Footer()

class TelaCadastrarLeitores(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Cadastro de leitores")
        yield Footer()