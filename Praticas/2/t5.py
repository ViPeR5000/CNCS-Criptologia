# Date and Time: Thursday, February 26, 2026 at 7:58:33 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

import os

def encrypt(in_file, out_file, ikey):
    """
    Implementação da Tarefa 5.
    Para já, a função apenas abre o ficheiro de entrada para leitura
    e copia o seu conteúdo para o ficheiro de saída, byte a byte.
    O parâmetro 'ikey' é declarado mas ainda não tem efeito na cópia.
    """
    try:
        # Abre os ficheiros em modo binário ('rb' para ler, 'wb' para escrever)
        with open(in_file, 'rb') as fin, open(out_file, 'wb') as fout:
            # Lê o primeiro byte
            b = fin.read(1)
            # Continua a ler e a escrever até o ficheiro chegar ao fim
            while b:
                fout.write(b)
                b = fin.read(1)
                
        print(f"Sucesso: Os bytes de '{in_file}' foram copiados para '{out_file}'.")
        
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{in_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um problema ao processar os ficheiros: {e}")

if __name__ == "__main__":
    # O poema de Luís de Camões sugerido no guião
    poema = (
        "As armas e os barões assinalados,\n"
        "Que da ocidental praia Lusitana,\n"
        "Por mares nunca de antes navegados,\n"
        "Passaram ainda além da Taprobana,\n"
        "Em perigos e guerras esforçados,\n"
        "Mais do que prometia a força humana,\n"
        "E entre gente remota edificaram\n"
        "Novo Reino, que tanto sublimaram;\n"
        "(...)\n"
    )
    
    # Criar o ficheiro plaintext.txt para efeitos de teste
    if not os.path.exists("plaintextx.txt"):
        print("A preparar o ambiente: a criar 'plaintext.txt' com o poema...")
        with open("plaintextx.txt", "w", encoding="utf-8") as f:
            f.write(poema)

    # Invocação da função com os parâmetros exatos pedidos na Tarefa 5
    print("\n--- A EXECUTAR TAREFA 5 ---")
    encrypt("plaintextx.txt", "ciphertext.txt", 123456789)
    print("Verifica o conteúdo do ficheiro 'ciphertext.txt'. Verás que é idêntico ao original!")

#EOF