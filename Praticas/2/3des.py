# Date and Time: Thursday, February 26, 2026 at 7:18:08 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def format_key(k):
    """Garante que cada chave tem exatamente 8 bytes (64 bits)"""
    k_bytes = k.encode('utf-8')
    if len(k_bytes) > 8:
        return k_bytes[:8]
    return k_bytes.ljust(8, b' ')

def testar_3des():
    print("=== TESTE DE CRIPTOGRAFIA 3DES (E-D-E MANUAL) ===")
    
    # Receber o texto original
    texto_original = input("Introduz o texto original: ")
    
    # Receber as 3 chaves
    print("\n[Nota: Cada chave deve ter idealmente 8 caracteres. Se for menor, será preenchida com espaços; se for maior, será cortada.]")
    k1 = input("Introduz a Chave 1: ")
    k2 = input("Introduz a Chave 2: ")
    k3 = input("Introduz a Chave 3: ")
    
    # Formatar as chaves
    k1_formatada = format_key(k1)
    k2_formatada = format_key(k2)
    k3_formatada = format_key(k3)
    
    print("\n--- RESUMO DAS CHAVES USADAS ---")
    print(f"K1 (8 bytes): {k1_formatada}")
    print(f"K2 (8 bytes): {k2_formatada}")
    print(f"K3 (8 bytes): {k3_formatada}")
    
    try:
        # Criar os 3 objetos DES individuais para simular o 3DES (modo ECB para demonstração)
        cifra1 = DES.new(k1_formatada, DES.MODE_ECB)
        cifra2 = DES.new(k2_formatada, DES.MODE_ECB)
        cifra3 = DES.new(k3_formatada, DES.MODE_ECB)
        
        # O DES é uma cifra de blocos (8 bytes), precisamos de preencher (pad) o texto
        texto_padded = pad(texto_original.encode('utf-8'), DES.block_size)
        
        # --- PROCESSO DE CIFRA (Encrypt - Decrypt - Encrypt) ---
        passo1_cifra = cifra1.encrypt(texto_padded)      # Encrypt com K1
        passo2_decifra = cifra2.decrypt(passo1_cifra)    # Decrypt com K2
        texto_cifrado = cifra3.encrypt(passo2_decifra)   # Encrypt com K3
        
        # Converter para Base64 para ser legível no ecrã
        cifrado_b64 = base64.b64encode(texto_cifrado).decode('utf-8')
        
        print("\n--- RESULTADO DA CIFRA ---")
        print(f"Texto Original:  {texto_original}")
        print(f"Texto Cifrado:   {cifrado_b64} (em Base64)")
        
        # --- PROCESSO DE DECIFRA (Inverso: Decrypt - Encrypt - Decrypt) ---
        dados_cifrados = base64.b64decode(cifrado_b64)
        
        passo1_reverso = cifra3.decrypt(dados_cifrados)  # Decrypt com K3
        passo2_reverso = cifra2.encrypt(passo1_reverso)  # Encrypt com K2
        texto_decifrado_padded = cifra1.decrypt(passo2_reverso) # Decrypt com K1
        
        # Remover o preenchimento (unpad)
        texto_decifrado = unpad(texto_decifrado_padded, DES.block_size).decode('utf-8')
        
        print("\n--- RESULTADO DA DECIFRA ---")
        print(f"Texto Decifrado: {texto_decifrado}")
        
    except Exception as e:
        print(f"\nOcorreu um erro durante a operação: {e}")

if __name__ == "__main__":
    testar_3des()

#EOF