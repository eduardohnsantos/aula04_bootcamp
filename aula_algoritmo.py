# Implementação do algoritmo de ordenação por seleção
lista_de_numeros = [40, 50, 60, 70, 0, -408593, 1, 50]
lista_de_numeros_02 = [40, 60, 70, 0, -408593, 1, 50]
lista_de_numeros_03 = [40, 60, 70, 0, 1, 50]


def ordernar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i + 1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = (
                    nova_lista_de_numeros[j],
                    nova_lista_de_numeros[i],
                )
    return nova_lista_de_numeros


nova_lista = ordernar_lista_de_numeros(lista_de_numeros)
nova_lista_2 = ordernar_lista_de_numeros(lista_de_numeros_02)
nova_lista_3 = ordernar_lista_de_numeros(lista_de_numeros_03)
# print(nova_lista)
# print(nova_lista_2)
# print(nova_lista_3)
