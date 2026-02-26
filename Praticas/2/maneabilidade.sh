#!/bin/bash
# Date and Time: Thursday, February 26, 2026 at 6:42:36 PM WET
# code by ViPeR5000(Rui Melo)
# https://github.com/viper5000

echo "=== DEMONSTRAÇÃO DE MANEABILIDADE ==="

# Preparar o ficheiro inicial
MENSAGEM="Enviar 2 euros para o Bob"
echo -n "$MENSAGEM" > texto-limpo.txt
echo "Criado ficheiro 'texto-limpo.txt' com: $MENSAGEM"

# Compilar o programa alterbyte (Tarefa 9)
cat << 'EOF_C' > alterbyte.c
#include <stdio.h>
#include <stdlib.h>

void alterbyte(char *in, char *out, int ibytenumber) {
    FILE *fIN = fopen(in, "rb");
    FILE *fOUT = fopen(out, "wb");
    if ((fIN == NULL) || (fOUT == NULL)) {
        fprintf(stderr, "Problem with file \n");
        exit(1);
    }
    int b, i = 1;
    b = fgetc(fIN);
    while (!feof(fIN)) {
        if (i == ibytenumber)
            b = b ^ 0x01; // Altera o byte
        fputc(b, fOUT);
        b = fgetc(fIN);
        i++;
    }
    fclose(fIN);
    fclose(fOUT);
}

int main(int argc, char **argv) {
    if (argc < 4) return 1;
    alterbyte(argv[1], argv[2], atoi(argv[3]));
    return 0;
}
EOF_C

gcc alterbyte.c -o alterbyte
echo "Programa 'alterbyte' compilado."

# --- Tarefas 8 e 9: Cifra por Blocos (AES128) ---
echo -e "\n--- Tarefas 8 e 9: AES128 (Cifra de Blocos) ---"
openssl enc -aes-128-cbc -K 0123456789abcdef0123456789abcdef -in texto-limpo.txt -out cifrado.aes -iv 00000000000000000000000000000000
./alterbyte cifrado.aes cifrado-2.aes 8
# Ao tentar decifrar um bloco AES corrompido, o OpenSSL normalmente dá erro de "bad decrypt"
openssl enc -d -aes-128-cbc -K 0123456789abcdef0123456789abcdef -in cifrado-2.aes -out texto-limpo-2.txt -iv 00000000000000000000000000000000 2>/dev/null

echo "Resultado AES após alteração:"
cat texto-limpo-2.txt || echo "(Ficheiro ilegível/Erro de padding)"
echo ""

# --- Tarefas 10 e 11: Cifra Contínua (ChaCha20) ---
echo -e "\n--- Tarefas 10 e 11: ChaCha20 (Cifra Contínua) ---"
openssl enc -chacha20 -K 0123456789abcdef000000000000000000000000000000000000000000000000 -in texto-limpo.txt -out cifrado.cc20 -iv 00000000000000000000000000000000
./alterbyte cifrado.cc20 cifrado-2.cc20 8
openssl enc -d -chacha20 -K 0123456789abcdef000000000000000000000000000000000000000000000000 -in cifrado-2.cc20 -out texto-limpo-3.txt -iv 00000000000000000000000000000000

echo "Resultado ChaCha20 após alteração:"
cat texto-limpo-3.txt
echo ""

# Limpeza
rm alterbyte.c alterbyte
echo -e "\nDemonstração concluída!"
#EOF