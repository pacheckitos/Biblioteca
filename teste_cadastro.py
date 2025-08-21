from model import (Biblioteca, Livro)

#
# Cadastrar empréstimo
#
# pré-condições: 
# - existe uma Biblioteca
# - existe um livro
# - existe um leitor 

biblioteca = Biblioteca()
'''Aqui bombou'''

# Início do cadastro

biblioteca.cadastrar_livro("a01", "Viagem ao centro da terra")
'''aqui foi também'''

biblioteca.cadastrar_leitor("03232584098", "Matheus Pacheco Nunes")

# - Existe um novo_livro : Livro
# - Existe um novo_leitor : Leitor

novo_livro = biblioteca.consultar_livro("a01")
novo_leitor = biblioteca.consultar_leitor("03232584098")

print(f"{novo_livro.titulo}")
print(f"{novo_leitor.nome}")

# - Cria o cadastro com o leitor e o livro

biblioteca.emprestar(novo_livro, novo_leitor)

um_emprestimo = biblioteca.consultar_emprestimo("a01")

print(um_emprestimo.livro.titulo)

if biblioteca.devolver(um_emprestimo):
    print(f"Livro {um_emprestimo.livro.titulo} devolvido com sucesso!")


# pós-condições
# - existe um livro_novo:Livro
# - livro_novo está em Biblioteca.livros

# Testando pós-condições

# Consulta de livros
#
# Pré-condições:
# existe uma biblioteca

# pós-condições
# nenhuma em especial

'''um_leitor = biblioteca.consultar_leitor("03232584098")
print(um_leitor.nome)
Aqui também foi'''

# Excluir livro
# pré-condições:
# exite uma bilioteca

'''if biblioteca.excluir_leitor("03232584098"):
    print(f"{um_leitor.nome} excluído")
pegou'''


# pós-condições:
# biblioteca.livros não contém o livro excluído

'''if livro := biblioteca.consultar_livro("a01"):
    print(livro.titulo)
'''
#
# Alteração do cadastro de um livro
#
# pré-condições
# existe uma biblioteca
# existe o livro que vai ser alterado

'''biblioteca.atualizar_leitor("03232584098", "Matheus Canez Pacheco")
print(biblioteca.consultar_leitor("03232584098").nome)
Aqui foi também'''

# pós-condições
# o livro está em Biblioteca.livros com os dados alterados