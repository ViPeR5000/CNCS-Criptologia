# Date and Time: Thursday, February 26, 2026 at 6:50:01 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

import random
import os

def encrypt(in_file, out_file, ikey):
    # Tarefa 6: Inicializador do gerador dentro do procedimento 
    random.seed(ikey)
    
    try:
        # Abre os ficheiros em modo de leitura e escrita binária
        with open(in_file, 'rb') as fin, open(out_file, 'wb') as fout:
            # Lê o conteúdo todo para um bytearray (mutável)
            data = bytearray(fin.read())
            
            # Tarefa 6: XOR do output do gerador rand() com os bytes lidos
            for i in range(len(data)):
                # No Python, geramos diretamente um byte aleatório (0 a 255)
                # para simular o comportamento do C onde o XOR trunca o int para byte.
                data[i] ^= random.randint(0, 255)
            
            # Escreve os bytes resultantes no ficheiro de saída 
            fout.write(data)
            
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{in_file}' não foi encontrado. Por favor cria-o primeiro.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    ikey = 123456789
    
    # Tarefa 4: Testar o gerador pseudo-aleatório do Python 
    random.seed(ikey)
    print("--- TAREFA 4 ---")
    print("Primeiros 5 valores gerados com a semente 123456789:")
    for _ in range(5):
        # Simulamos a impressão de números grandes à semelhança do rand() em C
        print(random.randint(0, 2147483647))
        
    # Verificar se o plaintext.txt existe para evitar erros
    if not os.path.exists("plaintext.txt"):
        print("\nAviso: O ficheiro 'plaintext.txt' não existe. A criar um com um texto de exemplo...")
        with open("plaintext.txt", "w") as f:
            f.write("As armas e os baroes assinalados,\nQue da ocidental praia Lusitana,\n")

    # Tarefas 5 e 6: Cifrar o ficheiro 
    print("\n--- TAREFAS 5 e 6 ---")
    print("A cifrar 'plaintext.txt' para 'ciphertext.txt'...")
    encrypt("plaintext.txt", "ciphertext.txt", 123456789)
    
    # Tarefa 7: Decifrar (nas cifras simétricas contínuas, a função de decifra é igual à de cifra) 
    print("\n--- TAREFA 7 ---")
    print("A decifrar 'ciphertext.txt' para 'plaintext-2.txt'...")
    encrypt("ciphertext.txt", "plaintext-2.txt", 123456789)
    
    print("\nProcesso concluido! Podes verificar o conteudo de 'ciphertext.txt' e 'plaintext-2.txt'.")

#EOF