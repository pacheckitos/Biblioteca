from textual.app import App, SystemCommand
from textual.binding import Binding
from view import TelaInicial, TelaCadastrarLivros, TelaCadastrarLeitores, TelaMenuLeitores

class AppBiblioteca(App):

    BINDINGS = [
        Binding("escape", "ir_para_inicial", "Início"),
        Binding("ctrl+n", "cadastrar_livros", "Cadastrar novo livro"),
        Binding("ctrl+l", "cadastrar_leitores", "Cadastrar novo leitor"),
    ]

    SCREENS = {
        "inicial" : TelaInicial,
        "cadastrar_livros" : TelaCadastrarLivros,
        "menu_leitores" : TelaMenuLeitores,
        "cadastrar_leitores" : TelaCadastrarLeitores
    }

    def on_mount(self):
        self.push_screen("inicial")    

    def action_cadastrar_livros(self):
        self.switch_screen("cadastrar_livros")

    def action_ir_para_inicial(self):
        self.switch_screen("inicial")

    def action_cadastrar_leitores(self):
        self.switch_screen("cadastrar_leitores")

    def get_system_commands(self, screen):
        yield from super().get_system_commands(screen)
        yield SystemCommand("Bell", "Ring the bell", self.action_cadastrar_livros)

if __name__ == "__main__":
    AppBiblioteca().run()