#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void calcular_entropia(const char *caminho_ficheiro) {
    // Abre o ficheiro em modo binário de leitura ("rb")
    FILE *ficheiro = fopen(caminho_ficheiro, "rb");
    if (ficheiro == NULL) {
        printf("Erro: O ficheiro '%s' não foi encontrado ou não pode ser lido.\n", caminho_ficheiro);
        return;
    }

    // Array para contar a frequência de cada byte (0 a 255)
    long contagem_bytes[256] = {0};
    long total_bytes = 0;
    int byte;

    // Lê o ficheiro byte a byte até chegar ao fim (EOF)
    while ((byte = fgetc(ficheiro)) != EOF) {
        contagem_bytes[byte]++;
        total_bytes++;
    }

    fclose(ficheiro);

    // Verifica se o ficheiro está vazio
    if (total_bytes == 0) {
        printf("O ficheiro está vazio. Entropia: 0\n");
        return;
    }

    // Calcula a entropia usando a fórmula de Shannon (base 10)
    double entropia = 0.0;
    for (int i = 0; i < 256; i++) {
        if (contagem_bytes[i] > 0) {
            double probabilidade = (double)contagem_bytes[i] / total_bytes;
            entropia -= probabilidade * log10(probabilidade);
        }
    }

    // Calcula a entropia máxima para 256 valores possíveis (n = 256)
    double entropia_maxima = log10(256.0);

    // Imprime os resultados
    printf("--- Resultados para '%s' ---\n", caminho_ficheiro);
    printf("Tamanho do ficheiro: %ld bytes\n", total_bytes);
    printf("Entropia calculada:  %.4f\n", entropia);
    printf("Entropia máxima:     %.4f\n", entropia_maxima);
}

int main(int argc, char *argv[]) {
    // Verifica se o utilizador passou o nome do ficheiro como argumento
    if (argc != 2) {
        printf("Uso correto: ./entropia <nome_do_ficheiro>\n");
        return 1;
    }

    calcular_entropia(argv[1]);
    return 0;
}