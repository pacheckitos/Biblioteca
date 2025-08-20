class Biblioteca:

    def __init__(self):
        self.livros = dict()
        self.leitores = dict()

    def cadastrar_livro(self, cod, titulo):
        livro = Livro()
        livro.set_cod(cod)
        livro.set_titulo(titulo)

        self.livros[livro.cod] = livro

    def consultar_livro(self, cod):
        try:
            return self.livros[cod]
        except KeyError:
            return False
    
    def excluir_livro(self, cod):
        try:
            del self.livros[cod]
            return True
        except KeyError:
            return False

    def atualizar_livro(self, cod, titulo):
        # caso o código tenha mudado
        self.excluir_livro(cod)
        self.cadastrar_livro(cod, titulo)


    def cadastrar_leitor(self, leitor):
        self.leitores[leitor.cpf] = leitor

    def emprestar(self, livro, leitor):
        data_de_devolucao = self.calcular_data_devolucao()
        livro.set_emprestado()
        return Emprestimo(livro, leitor, data_de_devolucao)
        
    def calcular_data_devolucao(self):
        import datetime
        hoje = datetime.date.today()
        tempo_de_emprestimo = datetime.timedelta(weeks=1)
        # somamos 1 semana à data de emprestimo
        return hoje + tempo_de_emprestimo
        

class Livro:
    def __init__(self):
        self.emprestado = False

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_cod(self, cod):
        self.cod = cod

    def set_emprestado(self):
        self.emprestado = True
    

class Leitor:
    def __init__(self):
        self.emprestimos = list()

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

class Emprestimo:

    def __init__(self, livro, leitor, data_devolucao):
        self.livro = livro
        self.leitor = leitor
        self.data_devolucao = data_devolucao