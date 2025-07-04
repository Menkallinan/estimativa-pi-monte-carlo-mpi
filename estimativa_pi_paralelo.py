from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def estimar_pi(n_pontos: int) -> int:
    dentro = 0
    for _ in range(n_pontos):
        x, y = np.random.random(), np.random.random()
        if x*x + y*y <= 1.0:
            dentro += 1
    return dentro

if __name__ == "__main__":
    # 10 milhões de lançamentos
    total_pontos = 10000000
    # divide igualmente entre os ranks
    pontos_por_rank = total_pontos // size

    # sincroniza e registra o tempo inicial
    comm.Barrier()
    tempo_inicio = time.time()
    contagem_local = estimar_pi(pontos_por_rank)

    # agrega as contagens no rank 0
    contagem_total = comm.reduce(contagem_local, op=MPI.SUM, root=0)
    duracao = time.time() - tempo_inicio

    if rank == 0:
        pi = 4 * contagem_total / (pontos_por_rank * size)
        print(f"MPI ({size} ranks): Paralelo: π ≈ {pi:.6f} em {duracao:.2f}s")
