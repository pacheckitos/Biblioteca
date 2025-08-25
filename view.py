from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Input, Button, TabbedContent, TabPane, Markdown
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
            case "button_menu_livros":
                self.app.switch_screen("menu_livros")
            case "button_menu_emprestimos":
                self.app.switch_screen("menu_emprestimos")

class TelaMenuLivros(Screen):
    def compose(self):
        yield Header(show_clock = True)
        with TabbedContent():
            
            with TabPane("Cadastrar livro", id="tab_cadastrar_livro"):
                yield Static("Informe o título do livro:")
                yield Input(placeholder = "Título")
                yield Static("Informe o códido de cadastro do livro:")
                yield Input(placeholder = "Código de cadastro")
                yield Button("Cadastrar livro", id = "button_cadastrar_livro")
            
            with TabPane("Excluir livro", id="tab_excluir_livro"):
                yield Static("Informe o código de cadastro do livro:")
                yield Input(placeholder = "Código de cadastro")
                yield Button("Excluir livro", id = "button_excluir_livro")
            
            with TabPane("Atualizar livro", id="tab_atualizar_livro"):
                yield Static("Informe o código de cadastro do livro:")
                yield Input(placeholder = "Código de cadastro")
                yield Button("Buscar")
        yield Footer()

class TelaMenuLeitores(Screen):
    def compose(self):
        yield Header(show_clock = True)
        with TabbedContent():

            with TabPane("Cadastrar leitor", id = "tab_cadastrar_leitor"):
                yield Static("Informe o nome do leitor:")
                yield Input(placeholder = "Nome completo", id="cadastro_nome_leitor")
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF", id = "cadastro_cpf_leitor")
                yield Button("Cadastrar leitor", id = "button_cadastrar_leitor")

            
            with TabPane("Excluir leitor", id = "tab_excluir_leitor"):
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF", id = "txt_excluir_leitor")
                yield Button("Excluir leitor", id = "button_excluir_leitor")
            
            with TabPane("Atualizar leitor", id = "tab_atualizar_leitor"):
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF", id = "txt_busca_leitor")
                yield Button("Buscar", id = "button_busca_atualiza_leitor")             
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "button_cadastrar_leitor":
                cpf = self.query_one("#cadastro_cpf_leitor").value
                nome = self.query_one("#cadastro_nome_leitor").value
                biblioteca.cadastrar_leitor(cpf, nome)
                self.notify(f"Cadastro realizado! \nNome: {nome} \nCPF: {cpf}")
        
            case "button_excluir_leitor":
                cpf = self.query_one("#txt_excluir_leitor").value
                if biblioteca.excluir_leitor(cpf):
                    self.notify(f"Cadastro excluído!\nCPF: {cpf}")

            case "button_busca_atualiza_leitor":
                cpf = self.query_one("#txt_busca_leitor").value
                if biblioteca.consultar_leitor(cpf) == False:
                    self.notify(f"Erro!\nLeitor não encontrado para o CPF {cpf}")
                else:
                    self.app.switch_screen("atualizacao_leitor")
                    cpf = self.query_one("#atualizacao_cpf_leitor")
                    nome = self.query_one("#atualizacao_nome_leitor")
                    biblioteca.atualizar_leitor(nome, cpf)
                    self.notify(f"Cadastro alterado! \nNome: {nome} \nCPF: {cpf}")

class TelaAtualizaLeitor(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Informe o novo nome do leitor:")
        yield Input(placeholder = "Nome completo", id="atualizacao_nome_leitor")
        yield Static("Informe o novo CPF do leitor:")
        yield Input(placeholder = "CPF", id = "atualizacao_cpf_leitor")
        yield Button("Atualizar leitor", id = "atualizacao_cadastrar_leitor")
        yield Footer()

    


class TelaMenuEmprestimos(Screen):
    def compose(self):
        yield Header(show_clock = True)
        with TabbedContent():
            
            with TabPane("Criar empréstimo", id = "tab_criar_emprestimo"):
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF")
                yield Static("Informe o código de cadastro do livro:")
                yield Input(placeholder = "Código de cadastro")
                yield Button("Criar empréstimo", id = "button_criar_emprestimo")
            
            with TabPane("Registrar devolução", id = "tab_registrar_devolucao"):
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF")
                yield Button("Buscar empréstimos do leitor", id = "button_buscar_emprestimos_1")

            with TabPane("Listar empréstimos", id = "tab_buscar_emprestimos"):
                yield Static("Informe o CPF do leitor:")
                yield Input(placeholder = "CPF")
                yield Button("Buscar empréstimos do leitor", id = "button_buscar_emprestimos_2")

class TelaCadastrarLeitores(Screen):
    def compose(self):
        yield Header(show_clock = True)
        yield Static("Informe o nome do leitor:")
        yield Input(placeholder = "Nome completo")
        yield Static("Informe o CPF do leitor:")
        yield Input(placeholder = "CPF")
        yield Button("Cadastrar leitor", id = "button_cadastrar_leitor")
        yield Footer()