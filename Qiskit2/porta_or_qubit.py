################################################
# Aplicação: Teste Básico de qubits            #
# Elaboração: Prof. Marcel Stefan Wagner, PhD  #
# Versão: 1.2 - 2025                           #
################################################

from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def simular_porta_or(a: int, b: int):
    # Criar circuito com 4 qubits e 1 bit clássico
    # Qubits: 0 = A, 1 = B, 2 = Resultado (OR), 3 = auxiliar para AND
    circuito = QuantumCircuit(4, 1)

    # Inicializar entradas
    if a == 1:
        circuito.x(0)
    if b == 1:
        circuito.x(1)

    # Implementar OR: A XOR B XOR (A AND B)
    circuito.cx(0, 2)       # A -> resultado (XOR)
    circuito.cx(1, 2)       # B -> resultado (XOR)
    circuito.ccx(0, 1, 3)   # Uso de Toffoli: A AND B -> auxiliar
    circuito.cx(3, 2)       # Auxiliar -> resultado (soma AND)

    # Medir o resultado do OR (qubit 2)
    circuito.measure(2, 0)

    # Simular
    simulador = QasmSimulator()
    resultado = simulador.run(circuito, shots=1000).result()
    contagens = resultado.get_counts()

    # Mostrar resultado
    print(f"Entradas: a={a}, b={b} -> Resultado OR (medido): {contagens}")
    circuito.draw(output="mpl")
    plt.show()
    plot_histogram(contagens)
    plt.show()

# Testes
simular_porta_or(0, 0)
simular_porta_or(0, 1)
simular_porta_or(1, 0)
simular_porta_or(1, 1)
