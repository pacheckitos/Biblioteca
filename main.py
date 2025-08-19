from model import *

#
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
print(um_emprestimo.data_devolucao)