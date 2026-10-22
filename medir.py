
import random
import time
import csv
import matplotlib.pyplot as plt

from ordenacao import quicksort_pura, quicksort_hibrida


TAMANHO = 20_000
CORTES = [1, 5, 10, 16, 20, 32, 50, 100, 200]
REPETICOES = 5

def medir_tempo(funcao, lista):
    inicio = time.perf_counter()
    funcao(lista)
    fim = time.perf_counter()

    return fim - inicio

def main():
    resultados = []

    random.seed(42)
    listas = [
        [random.randint(0, 100_000) for _ in range(TAMANHO)]
        for _ in range(REPETICOES)
    ]

    print(f"Tamanho das listas: {TAMANHO}")
    print(f"Repetições por configuração: {REPETICOES}")
    print()

    tempos_puros = []

    for lista in listas:
        tempo = medir_tempo(quicksort_pura, lista)
        tempos_puros.append(tempo)

    media_pura = sum(tempos_puros) / len(tempos_puros)

    print(f"Quick Sort puro: {media_pura:.6f} segundos")
    print()

    for corte in CORTES:
        tempos = []

        for lista in listas:
            tempo = medir_tempo(
                lambda valores: quicksort_hibrida(valores, corte),
                lista
            )
            tempos.append(tempo)

        media = sum(tempos) / len(tempos)

        ganho_percentual = (
            (media_pura - media) / media_pura
        ) * 100

        resultados.append({
            "corte": corte,
            "tempo_medio": media,
            "tempo_quicksort_puro": media_pura,
            "ganho_percentual": ganho_percentual
        })

        print(
            f"Corte {corte:3}: "
            f"{media:.6f} segundos | "
            f"Ganho: {ganho_percentual:.2f}%"
        )

    with open(
        "resultados.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        campos = [
            "corte",
            "tempo_medio",
            "tempo_quicksort_puro",
            "ganho_percentual"
        ]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )
        escritor.writeheader()
        escritor.writerows(resultados)

    cortes = [resultado["corte"] for resultado in resultados]
    tempos_hibridos = [
        resultado["tempo_medio"] for resultado in resultados
    ]

    plt.figure(figsize=(10, 6))

    plt.plot(
        cortes,
        tempos_hibridos,
        marker="o",
        label="Quick Sort híbrido"
    )

    plt.axhline(
        y=media_pura,
        linestyle="--",
        label="Quick Sort puro"
    )

    plt.xlabel("Valor do corte")
    plt.ylabel("Tempo médio (segundos)")
    plt.title("Quick Sort puro x Quick Sort híbrido")
    plt.xticks(CORTES)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    plt.savefig("grafico_cortes.png", dpi=150)
    plt.show()

    melhor = min(resultados, key=lambda resultado: resultado["tempo_medio"])

    print()
    print(f"Melhor corte: {melhor['corte']}")
    print(f"Tempo médio: {melhor['tempo_medio']:.6f} segundos")
    print(f"Tempo do Quick Sort puro: {media_pura:.6f} segundos")
    print(f"Ganho sobre o puro: {melhor['ganho_percentual']:.2f}%")

    print()
    print("Arquivos gerados:")
    print("- resultados.csv")
    print("- grafico_cortes.png")


if __name__ == "__main__":
    main()
