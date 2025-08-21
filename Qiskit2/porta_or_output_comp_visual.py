##########################################################
# Aplicação: Teste Esfera de Bloch comparar visualmente  #
# Elaboração: Prof. Marcel Stefan Wagner, PhD            #
# Versão: 1.2 - 2025                                     #
##########################################################

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace
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
    rho = partial_trace(state, [0, 1])  # DensityMatrix

    # Calcular vetor de Bloch da saída
    pauli_x = np.array([[0, 1], [1, 0]])
    pauli_y = np.array([[0, -1j], [1j, 0]])
    pauli_z = np.array([[1, 0], [0, -1]])

    x = np.real(np.trace(rho.data @ pauli_x))
    y = np.real(np.trace(rho.data @ pauli_y))
    z = np.real(np.trace(rho.data @ pauli_z))

    vetor_saida = [x, y, z]
    vetor_zero = [0, 0, 1]
    vetor_um   = [0, 0, -1]

    # Mostrar valores numéricos
    print(f"Entrada A={a}, B={b}")
    print(f"→ Bloch saída: {np.round(vetor_saida, 3)}")
    print(f"→ Referência |0⟩: {vetor_zero}")
    print(f"→ Referência |1⟩: {vetor_um}")

    # Criar subplots com 3 esferas de Bloch
    fig = plt.figure(figsize=(12, 4))

    ax1 = fig.add_subplot(131, projection='3d')
    plot_bloch_vector(vetor_saida, title="Saída OR", ax=ax1)

    ax2 = fig.add_subplot(132, projection='3d')
    plot_bloch_vector(vetor_zero, title="Estado |0⟩", ax=ax2)

    ax3 = fig.add_subplot(133, projection='3d')
    plot_bloch_vector(vetor_um, title="Estado |1⟩", ax=ax3)

    plt.tight_layout()
    plt.show()

# Testar todas as entradas
for a in [0, 1]:
    for b in [0, 1]:
        visualizar_saida_or_bloch(a, b)
