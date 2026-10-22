
import unittest

from ordenacao import insercao, quicksort_pura, quicksort_hibrida


class TestesOrdenacao(unittest.TestCase):

    def testar_lista_vazia(self):
        self.assertEqual(quicksort_pura([]), [])
        self.assertEqual(quicksort_hibrida([], 5), [])

    def testar_um_elemento(self):
        self.assertEqual(quicksort_pura([7]), [7])
        self.assertEqual(quicksort_hibrida([7], 5), [7])

    def testar_lista_ordenada(self):
        lista = [1, 2, 3, 4, 5]

        self.assertEqual(quicksort_pura(lista), lista)
        self.assertEqual(quicksort_hibrida(lista, 3), lista)

    def testar_lista_invertida(self):
        lista = [5, 4, 3, 2, 1]
        esperada = [1, 2, 3, 4, 5]

        self.assertEqual(quicksort_pura(lista), esperada)
        self.assertEqual(quicksort_hibrida(lista, 3), esperada)

    def testar_valores_repetidos(self):
        lista = [4, 2, 4, 1, 2, 4]
        esperada = [1, 2, 2, 4, 4, 4]

        self.assertEqual(quicksort_pura(lista), esperada)
        self.assertEqual(quicksort_hibrida(lista, 3), esperada)

    def testar_lista_negativa(self):
        lista = [0, -5, 3, -2, 1]
        esperada = [-5, -2, 0, 1, 3]

        self.assertEqual(quicksort_pura(lista), esperada)
        self.assertEqual(quicksort_hibrida(lista, 3), esperada)

    def testar_insercao(self):
        lista = [5, 3, 1, 4, 2]

        self.assertEqual(insercao(lista), [1, 2, 3, 4, 5])

    def testar_corte_um(self):
        lista = [8, 3, 5, 3, 1, 9, 2]

        pura = quicksort_pura(lista)
        hibrida = quicksort_hibrida(lista, 1)

        self.assertEqual(hibrida, pura)

    def testar_lista_original_preservada(self):
        lista = [5, 2, 4, 1]
        original = lista.copy()

        quicksort_pura(lista)
        quicksort_hibrida(lista, 3)
        insercao(lista)

        self.assertEqual(lista, original)


if __name__ == "__main__":
    unittest.main(verbosity=2)
