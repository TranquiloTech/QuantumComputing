################################################
# Aplicação: Teste com Tabela da Verdade OR    #
# Elaboração: Prof. Marcel Stefan Wagner, PhD  #
# Versão: 1.2 - 2025                           #
################################################

from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator

def simular_or(a: int, b: int) -> int:
    # 3 qubits (A, B, saída), 1 bit clássico para medir
    circuito = QuantumCircuit(3, 1)

    # Inicializa A (q0) e B (q1)
    if a == 1:
        circuito.x(0)  # qubit A
    if b == 1:
        circuito.x(1)  # qubit B

    # Usar De Morgan: OR = NOT(NOT A AND NOT B)
    circuito.x(0)            # NOT A
    circuito.x(1)            # NOT B
    circuito.ccx(0, 1, 2)    # AND(NOT A, NOT B) → q2
    circuito.x(2)            # NOT do resultado → OR(A, B)
    circuito.x(0)            # restaurar A
    circuito.x(1)            # restaurar B

    # Medir saída (q2)
    circuito.measure(2, 0)

    # Simulação
    simulador = QasmSimulator()
    job = simulador.run(circuito, shots=1)
    resultado = job.result().get_counts()

    # Retornar o valor binário medido (como inteiro)
    return int(max(resultado, key=resultado.get))

# Gerar tabela verdade
print("\nTabela Verdade - Porta OR (Simulada com Qiskit)\n")
print("| A | B | OR |")
print("|---|---|----|")

for a in [0, 1]:
    for b in [0, 1]:
        resultado = simular_or(a, b)
        print(f"| {a} | {b} | {resultado}  |")

print("|---|---|----|\n")
