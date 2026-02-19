# Date and Time: Thursday, February 19, 2026 at 6:56:44 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

import string
import random
import subprocess
import sys

# ==========================================
# FUNÇÕES DE LÓGICA DAS CIFRAS
# ==========================================

def cesar_cifrar(texto, k):
    resultado = ""
    for char in texto:
        if char.isalpha(): 
            base = 65 if char.isupper() else 97
            resultado += chr((ord(char) - base + k) % 26 + base)
        else:
            resultado += char
    return resultado

def cesar_decifrar(criptograma, k):
    return cesar_cifrar(criptograma, -k)

def vigenere_cifrar(texto, chave):
    resultado = ""
    indice_chave = 0
    for char in texto:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            deslocamento = ord(chave[indice_chave % len(chave)].upper()) - 65
            resultado += chr((ord(char) - base + deslocamento) % 26 + base)
            indice_chave += 1
        else:
            resultado += char
    return resultado

def vigenere_decifrar(criptograma, chave):
    resultado = ""
    indice_chave = 0
    for char in criptograma:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            deslocamento = ord(chave[indice_chave % len(chave)].upper()) - 65
            resultado += chr((ord(char) - base - deslocamento) % 26 + base)
            indice_chave += 1
        else:
            resultado += char
    return resultado

def xor_strings(s1, s2):
    return "".join(str(int(a) ^ int(b)) for a, b in zip(s1, s2))

# ==========================================
# FUNÇÕES DE EXECUÇÃO DAS TAREFAS
# ==========================================

def executar_cesar():
    print("\n--- 1. A CIFRA DE CÉSAR ---")
    print("Tarefa 1 (Cifrar 'OLA' com k=3):", cesar_cifrar("OLA", 3))
    print("Tarefa 2 (Decifrar com k=10):", cesar_decifrar("LOXPSMKOYWKSYB", 10))
    
    criptograma_t3 = "J HVM NVGBVYJ, LPVIOJ YJ OZP NVG NVJ GVBMDHVN YZ KJMOPBVG!"
    print("Tarefa 3 (Decifrado com k=5 deduzido):", cesar_decifrar(criptograma_t3, 5))
    input("\nPrima ENTER para voltar ao menu...")

def executar_vigenere():
    print("\n--- 2. A CIFRA DE VIGENÈRE ---")
    texto_t4 = "TIO MANEL TINHA UMA QUINTA"
    chave_t4 = "AULA"
    print(f"Tarefa 4 (Cifrar com chave '{chave_t4}'):", vigenere_cifrar(texto_t4, chave_t4))

    criptograma_t5 = "JUWP G IBELM"
    chave_t5 = "BCD"
    print("Tarefa 5 (Decifrar com chave deduzida 'BCD'):", vigenere_decifrar(criptograma_t5, chave_t5))
    input("\nPrima ENTER para voltar ao menu...")

def executar_substituicao():
    print("\n--- 3. CIFRA DE SUBSTITUIÇÃO ---")
    alfabeto_original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chave_substituicao = "SQTUHJIBYKAVLCWEZNRMXGFPDO"

    def substituicao_cifrar_local(texto):
        tabela = str.maketrans(alfabeto_original, chave_substituicao)
        return texto.translate(tabela)

    def substituicao_decifrar_local(criptograma):
        tabela = str.maketrans(chave_substituicao, alfabeto_original)
        return criptograma.translate(tabela)

    texto_t6 = "OLACOMOESTA"
    cifrado_t6 = substituicao_cifrar_local(texto_t6)
    print("Tarefa 6 (Texto Limpo):", texto_t6)
    print("Tarefa 6 (Cifrado):", cifrado_t6)
    print("Tarefa 6 (Decifrado):", substituicao_decifrar_local(cifrado_t6))
    input("\nPrima ENTER para voltar ao menu...")

def executar_otp():
    print("\n--- 4. ONE TIME PAD ---")
    lancamentos = [str(random.choice([0, 1])) for _ in range(16)]
    otp_chave = "".join(lancamentos)
    print(f"Tarefa 7 (Chave OTP gerada aleatoriamente): {otp_chave}")

    mensagem_binaria = "0000000100000001"
    resultado_xor = xor_strings(mensagem_binaria, otp_chave)
    print(f"Tarefa 8 (Mensagem original): {mensagem_binaria}")
    print(f"Tarefa 8 (Resultado XOR):    {resultado_xor}")
    input("\nPrima ENTER para voltar ao menu...")

def executar_openssl():
    print("\n--- 5. EXPLORAÇÃO DO OPENSSL ---")
    print("Tarefa 10: A executar comando 'openssl rand -hex 10' no sistema...")
    try:
        resultado_openssl = subprocess.run(
            ['openssl', 'rand', '-hex', '10'], 
            capture_output=True, 
            text=True, 
            check=True
        )
        print(f"Resultado gerado pelo OpenSSL: {resultado_openssl.stdout.strip()}")
    except FileNotFoundError:
        print("Aviso: O OpenSSL não está instalado ou não foi encontrado nas variáveis de ambiente deste sistema.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar executar o OpenSSL: {e}")
    input("\nPrima ENTER para voltar ao menu...")

def mostrar_creditos():
    print("\n==========================================")
    print("               CRÉDITOS")
    print("==========================================")
    print("Resolução da Aula Prática 1 de Criptologia")
    print("Desenvolvido por: Rui Melo (ViPeR5000)")
    print("GitHub:           https://github.com/viper5000")
    print("==========================================")
    input("\nPrima ENTER para voltar ao menu...")

# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():
    while True:
        print("\n" + "="*40)
        print("   RESOLUÇÃO DE CRIPTOLOGIA - FICHA 1")
        print("="*40)
        print("1. A Cifra de César (Tarefas 1, 2 e 3)")
        print("2. A Cifra de Vigenère (Tarefas 4 e 5)")
        print("3. Cifra de Substituição (Tarefa 6)")
        print("4. One Time Pad - OTP (Tarefas 7 e 8)")
        print("5. Exploração do OpenSSL (Tarefa 10)")
        print("6. Créditos")
        print("0. Sair")
        print("="*40)
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            executar_cesar()
        elif escolha == '2':
            executar_vigenere()
        elif escolha == '3':
            executar_substituicao()
        elif escolha == '4':
            executar_otp()
        elif escolha == '5':
            executar_openssl()
        elif escolha == '6':
            mostrar_creditos()
        elif escolha == '0':
            print("\nA encerrar o programa. Continuação de bons estudos!\n")
            sys.exit()
        else:
            print("\nOpção inválida! Por favor, escolha um número de 0 a 6.")

if __name__ == "__main__":
    menu_principal()

#EOF