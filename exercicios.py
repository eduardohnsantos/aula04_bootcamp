# Exercícios de Listas e Dicionários

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro_01: dict = {"Titulo": "Game Of Thrones", "Autor": "Estagiario", "Ano": "2005"}

livro_02: Dict[str, Any] = {
    "Titulo": "Game Of Throne2",
    "Autor": "Estagiario",
    "Ano": "2007",
}

lista_de_livros = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

print(lista_de_livros)


# lista_de_elementos: list = livro_01.items()
# for elemento in lsita_de_elementos:
#    print(elemento)


# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
