import time
import numpy as np

def estimatar_pi(n_points: int) -> float:
    # Contador para os pontos que caírem dentro do círculo
    dentro = 0

    # Gerando 'n_points' pontos aleatórios no quadrado [0,1)x[0,1)
    for _ in range(n_points):
        # Coordenadas aleatórias x e y no intervalo [0,1)
        x, y = np.random.random(), np.random.random()
        
        # Verifica se o ponto (x, y) está dentro do círculo de raio 1
        if x*x + y*y <= 1.0:
            dentro += 1  # incrementa o contador se estiver dentro

    # Calcula e retorna a estimativa de π
    # Razão dos pontos dentro do círculo pelo total, multiplicado por 4 (área do círculo completa)
    return 4 * dentro / n_points

if __name__ == "__main__":
    N = 10000000  # Número total de pontos a serem gerados para estimar π

    t0 = time.time()  # Tempo inicial antes do cálculo
    pi = estimatar_pi(N)  # Chama a função para calcular π com N pontos
    dt = time.time() - t0  # Calcula tempo total decorrido

    # Exibe o valor estimado de π e o tempo gasto na execução
    print(f"Serial: π ≈ {pi:.6f} Tempo: t = {dt:.2f}s")
    
   
