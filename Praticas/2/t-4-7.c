// Date and Time: Thursday, February 26, 2026 at 6:42:36 PM WET
// code by ViPeR5000(Rui Melo)
// https://github.com/viper5000

#include <stdio.h>
#include <stdlib.h>

// Procedimento pedido na Tarefa 5 e modificado na Tarefa 6
void encrypt(const char *in, const char *out, int ikey) {
    FILE *fIN = fopen(in, "rb");
    FILE *fOUT = fopen(out, "wb");
    
    if (fIN == NULL || fOUT == NULL) {
        fprintf(stderr, "Erro ao abrir ficheiros.\n");
        return;
    }

    // Tarefa 6: Inicializador do gerador dentro do procedimento
    srand(ikey);

    int b;
    b = fgetc(fIN);
    while (!feof(fIN)) {
        // Tarefa 6: XOR do output do gerador rand() com o byte lido
        b = b ^ rand();
        fputc(b, fOUT);
        b = fgetc(fIN);
    }

    fclose(fIN);
    fclose(fOUT);
}

int main() {
    // Tarefa 4: Testar o gerador pseudo-aleatório
    unsigned int ikey = 123456789;
    srand(ikey);
    
    printf("--- TAREFA 4 ---\n");
    printf("Primeiros 5 valores gerados (de 1000 pedidos):\n");
    for(int i = 0; i < 5; i++) {
        printf("%u\n", (unsigned int) rand());
    }

    // Tarefas 5 e 6: Cifrar o ficheiro
    printf("\n--- TAREFAS 5 e 6 ---\n");
    printf("A cifrar 'plaintext.txt' para 'ciphertext.txt'...\n");
    encrypt("plaintext.txt", "ciphertext.txt", 123456789);
    
    // Tarefa 7: Decifrar (a função é exatamente a mesma)
    printf("\n--- TAREFA 7 ---\n");
    printf("A decifrar 'ciphertext.txt' para 'plaintext-2.txt'...\n");
    encrypt("ciphertext.txt", "plaintext-2.txt", 123456789);
    
    printf("\nProcesso concluido! Verifica os ficheiros gerados.\n");
    return 0;
}
//EOF