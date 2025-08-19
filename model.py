class Biblioteca:

    def __init__(self):
        self.livros = dict()
        self.usuarios = dict()

    def cadastrar_livro(self, livro):
        self.livros[livro.cod] = livro

    def cadastrar_usuario(self, usuario):
        self.usuarios[usuario.cpf] = cpf 

    def emprestar(self, livro, usuario):
        data_de_devolucao = self.calcular_data_devolucao()
        livro.set_emprestado()
        return Emprestimo(livro, usuario, data_de_devolucao)

    def calcular_data_devolucao(self):
        import datetime
        hoje = datetime.date.today()
        tempo_de_emprestimo = datetime.timedelta(weeks = 1)
        return hoje + tempo_de_emprestimo

class Livro:
    def __init__(self):
        self.emprestado = False

    def set_emprestado(self):
        self.emprestado = True

class Usuario:
    def __init__(self):
        self.emprestimos = list()

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

class Emprestimo:

    def __init__(self, livro, usuario, data_devolucao):
        self.livro = livro
        self.usuario = usuario
        self.data_devolucao = data_devolucao

    def set_livro(self, livro):
        self.livro = livro

    def set_usuario(self, usuario):
        self.usuario = usuario

    def set_data_devolucao(self, data):
        self.data_devolucao = data

'''#
# Emprestar livro
#
# pré-condições:
# Existe um objeto Livro
# Existe um objeto Biblioteca
# Existe um objeto Usuario

biblioteca = Biblioteca()
um_livro = Livro()
um_usuario = Usuario()

# Início do empréstimo

um_emprestimo = biblioteca.emprestar(um_livro, um_usuario)
um_usuario.add_emprestimo(um_emprestimo)

# Fim
# pós-condições
print("Leitor tem um livro emprestado consigo? (True)")
print(len(um_usuario.emprestimos) > 0)

print("Estado do livro emprestado é emprestado = True?")
print(um_emprestimo.livro.emprestado == True)

print("Livro emprestado tem data de devolução concreta?")
print(um_emprestimo.data_devolucao)'''
