###############################################################
# Aplicação: Aplicação de Porta OR quântica em Irrigação IoT  #
# Elaboração: Prof. Marcel Stefan Wagner, PhD                 #
# Versão: 1.2 - 2025                                          #
###############################################################

from qiskit import QuantumCircuit
from qiskit_aer import QasmSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def porta_or_quantica(a: int, b: int) -> int:
    """
    Simula a porta OR quântica com base nas entradas a (solo seco) e b (sem previsão de chuva)
    Retorna 1 se a irrigação deve ser ativada
    """
    circuito = QuantumCircuit(4, 1)  # A, B, resultado, auxiliar

    # Inicializar entradas
    if a == 1:
        circuito.x(0)  # solo seco
    if b == 1:
        circuito.x(1)  # sem chuva

    # OR(A, B) = A XOR B XOR (A AND B)
    circuito.cx(0, 2)
    circuito.cx(1, 2)
    circuito.ccx(0, 1, 3)
    circuito.cx(3, 2)

    # Medir qubit 2 (resultado)
    circuito.measure(2, 0)

    # Executar simulação
    simulador = QasmSimulator()
    resultado = simulador.run(circuito, shots=100).result().get_counts()
    saida = int(max(resultado, key=resultado.get))
    return saida

# Simulando sensores
def simular_sensores():
    """
    Simula leituras dos sensores:
    - solo_seco = 1 se o solo estiver seco
    - sem_chuva = 1 se não houver previsão de chuva
    """
    # Exemplo 1: Solo úmido, com chuva - Desativado (ideal)
    #return {'solo_seco': 0, 'sem_chuva': 0}

    # Exemplo 2: Solo úmido, sem previsão de chuva - Ativado (manter)
    return {'solo_seco': 0, 'sem_chuva': 1}

    # Exemplo 3: Solo seco, com chuva - Ativado (complemento)
    #return {'solo_seco': 1, 'sem_chuva': 0}

    # Exemplo 4: Solo seco, sem previsão de chuva - Ativado (extremo)
    #return {'solo_seco': 1, 'sem_chuva': 1}

# Aplicação IoT
def sistema_irrigacao():
    sensores = simular_sensores()
    solo = sensores['solo_seco']
    clima = sensores['sem_chuva']

    print(f"\n[Sensores] Solo seco: {solo}, Sem chuva: {clima}")

    acionar_irrigacao = porta_or_quantica(solo, clima)

    if acionar_irrigacao:
        print("🚿 Irrigação ATIVADA!\n")
    else:
        print("✅ Irrigação NÃO necessária.\n")

# Executar sistema
sistema_irrigacao()
