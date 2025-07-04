
# Estimativa de $\\pi$ por Método de Monte Carlo (Serial vs. Paralelo)

Este repositório apresenta duas implementações em Python para estimar o valor de $\\pi$ utilizando o **Método de Monte Carlo**: uma versão serial e outra paralela, aproveitando a computação distribuída com MPI. O projeto visa demonstrar e comparar o desempenho de ambas as abordagens.

-----

## 🎲 Sobre o Método de Monte Carlo para $\\pi$

O método consiste em gerar uma grande quantidade de pontos aleatórios dentro de um quadrado unitário (com lados de tamanho 1). Dentro desse quadrado, um quarto de círculo é inscrito com raio 1. A proporção de pontos que caem dentro do quarto de círculo em relação ao total de pontos gerados se aproxima da proporção da área do quarto de círculo em relação à área do quadrado. Como a área do quarto de círculo é $\\frac{\\pi r^2}{4}$ (onde $r=1$) e a área do quadrado é $1^2$, essa proporção nos permite estimar $\\pi$.

Para uma visualização clara, consulte o diagrama: [`assets/monte_carlo_diagram.png`](https://www.google.com/search?q=assets/monte_carlo_diagram.png)

-----

## 📁 Estrutura do Repositório

  * `estimativa_pi_serial.py`: Implementação **serial** para estimar $\\pi$. Gera `N` pontos aleatórios e conta quantos caem dentro do quarto de círculo.
  * `estimativa_pi_paralelo.py`: Implementação **paralela** para estimar $\\pi$. Distribui a geração de pontos entre múltiplos processos usando `mpi4py` e agrega os resultados no rank 0.
  * `tempos_estimativas.txt`: Arquivo contendo os tempos de execução registrados para diferentes números de processos nas execuções.
  * `grafico_desempenho.png`: Gráfico comparativo visual do desempenho entre as versões serial e paralela.
  * `relatorio_SD_4.pdf`: Relatório técnico completo detalhando o projeto, metodologia, resultados e análises.
  * `assets/monte_carlo_diagram.png`: Diagrama ilustrativo do método de Monte Carlo para estimar $\\pi$.
  * `LICENSE`: Arquivo contendo os detalhes da licença MIT.

-----

## 🚀 Pré-requisitos

Para rodar as implementações, você precisará ter o seguinte instalado:

  * **Python 3.8+**
  * **MPI** (Message Passing Interface): Recomenda-se OpenMPI ou MPICH.
  * **Bibliotecas Python**: `numpy`, `mpi4py`, `matplotlib`

Você pode instalar as bibliotecas Python usando `pip`:

```bash
pip install numpy mpi4py matplotlib
```

-----

## 🛠️ Uso

### Versão Serial

Para executar a versão serial, basta rodar o script diretamente:

```bash
python estimativa_pi_serial.py
```

**Nota**: Você pode ajustar o valor de `N` (o número de pontos a serem gerados) diretamente no topo do script `estimativa_pi_serial.py` para controlar a precisão da estimativa.

### Versão Paralela

Para executar a versão paralela, você precisará usar o comando `mpiexec` (ou `mpirun`), especificando o número de processos (`-n <num_processos>`) que deseja utilizar:

```bash
mpiexec -n <num_processos> python estimativa_pi_paralelo.py
```

**Exemplo**: Para rodar com 4 processos:

```bash
mpiexec -n 4 python estimativa_pi_paralelo.py
```

-----

## 📈 Resultados

Os resultados detalhados e as análises de desempenho estão disponíveis nos seguintes arquivos:

  * **Tempos de Execução**: Consulte [`tempos_estimativas.txt`](https://www.google.com/search?q=tempos_estimativas.txt) para ver os dados brutos de tempo.
  * **Gráfico Comparativo**: O desempenho comparativo entre as versões serial e paralela está visualizado em [`grafico_desempenho.png`](https://www.google.com/search?q=grafico_desempenho.png).
  * **Relatório Completo**: Para uma análise aprofundada, abra [`relatorio_SD_4.pdf`](https://www.google.com/search?q=relatorio_SD_4.pdf).

-----

## 🤝 Contribuições

Contribuições são muito bem-vindas\! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para:

  * Abrir uma [Issue](https://www.google.com/search?q=https://github.com/seu-usuario/seu-repositorio/issues)
  * Enviar um [Pull Request](https://www.google.com/search?q=https://github.com/seu-usuario/seu-repositorio/pulls)

-----
