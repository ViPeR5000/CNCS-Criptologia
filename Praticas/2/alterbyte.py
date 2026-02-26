# Date and Time: Thursday, February 26, 2026 at 7:38:40 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

import sys

def alterbyte(in_file, out_file, ibytenumber):
    try:
        # Abre os ficheiros em modo de leitura e escrita binária ('rb' e 'wb')
        with open(in_file, 'rb') as fin, open(out_file, 'wb') as fout:
            # Lê todo o conteúdo do ficheiro de entrada para um bytearray (mutável)
            data = bytearray(fin.read())
            
            # O C usava um índice a começar em 1 (i=1). 
            # Em Python os arrays começam em 0, logo subtraímos 1 à posição.
            if 1 <= ibytenumber <= len(data):
                data[ibytenumber - 1] ^= 0x01
            else:
                print(f"Aviso: A posição {ibytenumber} excede o tamanho do ficheiro (tem {len(data)} bytes).")
            
            # Escreve o resultado alterado no ficheiro de saída
            fout.write(data)
            
    except FileNotFoundError:
        print(f"Problema: O ficheiro '{in_file}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Problem with file \nDetalhe do erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Verifica se foram passados os argumentos corretos na linha de comandos
    if len(sys.argv) < 4:
        print(f"Uso: python {sys.argv[0]} <ficheiro_entrada> <ficheiro_saida> <numero_do_byte>")
        sys.exit(1)
        
    ficheiro_in = sys.argv[1]
    ficheiro_out = sys.argv[2]
    num_byte = int(sys.argv[3])
    
    # Invoca a função principal
    alterbyte(ficheiro_in, ficheiro_out, num_byte)

#EOF