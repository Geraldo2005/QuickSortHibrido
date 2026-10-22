
import random


def insercao(lista):
    valores = lista.copy()

    for i in range(1, len(valores)):
        chave = valores[i]
        j = i - 1

        while j >= 0 and valores[j] > chave:
            valores[j + 1] = valores[j]
            j -= 1

        valores[j + 1] = chave

    return valores


def quicksort_pura(lista):
    if len(lista) <= 1:
        return lista.copy()

    pivo = random.choice(lista)

    menores = []
    iguais = []
    maiores = []

    for valor in lista:
        if valor < pivo:
            menores.append(valor)
        elif valor > pivo:
            maiores.append(valor)
        else:
            iguais.append(valor)

    return (
        quicksort_pura(menores)
        + iguais
        + quicksort_pura(maiores)
    )


def quicksort_hibrida(lista, corte):
    if len(lista) <= 1:
        return lista.copy()

    if len(lista) < corte:
        return insercao(lista)

    pivo = random.choice(lista)

    menores = []
    iguais = []
    maiores = []

    for valor in lista:
        if valor < pivo:
            menores.append(valor)
        elif valor > pivo:
            maiores.append(valor)
        else:
            iguais.append(valor)

    return (
        quicksort_hibrida(menores, corte)
        + iguais
        + quicksort_hibrida(maiores, corte)
    )
