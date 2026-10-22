# Quick Sort Híbrido

## Sobre o projeto

Este projeto compara o desempenho do Quick Sort puro com uma versão híbrida que combina Quick Sort e Insertion Sort.

A proposta é identificar qual valor de corte apresenta o menor tempo de execução para ordenar uma lista com 20.000 elementos aleatórios.

## Objetivos

- Implementar o Quick Sort com pivô aleatório.
- Separar os elementos em menores, iguais e maiores que o pivô.
- Implementar uma versão híbrida que utiliza Insertion Sort para pedaços menores que o corte definido.
- Comparar os tempos de execução das duas versões.
- Avaliar os cortes 1, 5, 10, 16, 20, 32, 50, 100 e 200.
- Gerar um gráfico com os tempos médios.
- Identificar o melhor corte e calcular o ganho em relação ao Quick Sort puro.

## Estrutura do projeto

```text
QuickSortHibrido/
├── ordenacao.py
├── testes.py
├── medir.py
├── resultados.csv
├── grafico_cortes.png
├── RELATORIO.md
├── README.md
└── .gitignore
```

A pasta `.venv/`, utilizada para o ambiente virtual do Python, não precisa ser enviada ao Git.

## Tecnologias utilizadas

- Python 3
- Matplotlib
- Unittest
- Git e GitHub

## Requisitos

- Python instalado.
- Pip disponível no ambiente Python.

## Como executar

### 1. Criar o ambiente virtual

No terminal do VS Code, execute:

```powershell
py -m venv .venv
```

### 2. Instalar a biblioteca utilizada no gráfico

```powershell
.\.venv\Scripts\python.exe -m pip install matplotlib
```

### 3. Executar os testes

```powershell
.\.venv\Scripts\python.exe -m unittest -v testes.py
```

### 4. Executar as medições

```powershell
.\.venv\Scripts\python.exe medir.py
```

Após a execução, o programa gera:

- `resultados.csv`: resultados das medições e ganhos percentuais.
- `grafico_cortes.png`: gráfico comparativo dos tempos médios.

## Metodologia

O experimento utiliza listas de 20.000 números aleatórios e realiza cinco repetições por configuração.

Os mesmos conjuntos de dados são utilizados nas diferentes configurações para tornar a comparação mais consistente.

Os cortes testados são:

`1, 5, 10, 16, 20, 32, 50, 100 e 200`.

O tempo é medido com `time.perf_counter()`, e a média das execuções é utilizada para comparar os resultados.

## Resultados

De acordo com o experimento registrado no relatório, o melhor resultado foi obtido com **corte igual a 20**, com tempo médio de aproximadamente 0,016544 segundo e redução de aproximadamente 17,82% em relação ao Quick Sort puro.

Cortes elevados, como 100 e 200, apresentaram pior desempenho, pois aumentam o tamanho dos pedaços que podem ser ordenados pelo Insertion Sort.

O corte igual a 1 mantém a lógica do Quick Sort puro, pois não aciona o Insertion Sort para pedaços com elementos.

Os resultados completos e o gráfico estão disponíveis no arquivo `RELATORIO.md` e nos arquivos gerados pelo programa.

## Autor

Geraldo
