

#
# Emprestar livro
#
# pré-condições:
# existe um objeto Livro
# existe um objeto Biblioteca
# existe um objeto Leitor

biblioteca = Biblioteca()
um_livro = Livro()
um_leitor = Leitor()

# Início do empréstimo

um_emprestimo = biblioteca.emprestar(um_livro, um_leitor)
um_leitor.add_emprestimo(um_emprestimo)

# Fim
# pós-condições
print("Leitor tem livro emprestado consigo? (true)")
print(len(um_leitor.emprestimos) > 0)

print("Estado do livro é emprestado = True?")
print(um_emprestimo.livro.emprestado == True)

print("Emprestimo tem data de devolução concreta?")
print(um_emprestimo.data_devolucao)