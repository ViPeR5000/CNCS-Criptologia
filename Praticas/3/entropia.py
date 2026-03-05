import sys
import math
from collections import Counter

def calcular_entropia(caminho_ficheiro):
    try:
        # Lê o ficheiro em formato binário ('rb') para ler os bytes reais
        with open(caminho_ficheiro, 'rb') as f:
            dados = f.read()
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{caminho_ficheiro}' não foi encontrado.")
        return

    total_bytes = len(dados)
    if total_bytes == 0:
        print("O ficheiro está vazio. Entropia: 0")
        return

    # Conta a frequência de cada byte (0 a 255)
    contagem_bytes = Counter(dados)

    # Calcula a entropia usando a fórmula de Shannon (base 10)
    entropia = 0.0
    for contagem in contagem_bytes.values():
        probabilidade = contagem / total_bytes
        entropia -= probabilidade * math.log10(probabilidade)

    # Calcula a entropia máxima para 256 valores possíveis (n = 256)
    entropia_maxima = math.log10(256)

    print(f"--- Resultados para '{caminho_ficheiro}' ---")
    print(f"Tamanho do ficheiro: {total_bytes} bytes")
    print(f"Entropia calculada:  {entropia:.4f}")
    print(f"Entropia máxima:     {entropia_maxima:.4f}")

if __name__ == "__main__":
    # Verifica se o utilizador passou o nome do ficheiro como argumento
    if len(sys.argv) != 2:
        print("Uso correto: python entropia.py <nome_do_ficheiro>")
    else:
        calcular_entropia(sys.argv[1])