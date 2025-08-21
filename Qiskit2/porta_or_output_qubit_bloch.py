################################################
# Aplicação: Teste com a Esfera de Bloch       #
# Elaboração: Prof. Marcel Stefan Wagner, PhD  #
# Versão: 1.2 - 2025                           #
################################################

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace, DensityMatrix
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt
import numpy as np

def visualizar_saida_or_bloch(a: int, b: int):
    circuito = QuantumCircuit(3)

    if a == 1:
        circuito.x(0)
    if b == 1:
        circuito.x(1)

    # OR reversível: NOT(NOT A AND NOT B)
    circuito.x(0)
    circuito.x(1)
    circuito.ccx(0, 1, 2)
    circuito.x(2)
    circuito.x(0)
    circuito.x(1)

    # Obter o vetor de estado completo
    state = Statevector.from_instruction(circuito)

    # Obter a matriz densidade reduzida do qubit 2
    rho = partial_trace(state, [0, 1])  # retorna DensityMatrix

    # Calcular vetor de Bloch manualmente usando esperanças
    pauli_x = np.array([[0, 1], [1, 0]])
    pauli_y = np.array([[0, -1j], [1j, 0]])
    pauli_z = np.array([[1, 0], [0, -1]])

    x = np.real(np.trace(rho.data @ pauli_x))
    y = np.real(np.trace(rho.data @ pauli_y))
    z = np.real(np.trace(rho.data @ pauli_z))

    vetor_bloch = [x, y, z]

    print(f"Entrada A={a}, B={b} → Bloch vector: {vetor_bloch}")
    plot_bloch_vector(vetor_bloch, title=f"Saída OR(A={a}, B={b})")
    plt.show()

# Testar todas as entradas
for a in [0, 1]:
    for b in [0, 1]:
        visualizar_saida_or_bloch(a, b)
