// Date and Time: Thursday, February 26, 2026 at 6:47:39 PM WET
// code by ViPeR5000(Rui Melo)
// https://github.com/viper5000

#include <stdio.h>
#include <stdlib.h>

void alterbyte(char *in, char *out, int ibytenumber) {
    FILE *fIN = fopen(in, "rb");
    FILE *fOUT = fopen(out, "wb");
    
    if ((fIN == NULL) || (fOUT == NULL)) {
        fprintf(stderr, "Problem with file \n");
        exit(1);
    }
    
    int b;
    int i = 1;
    
    b = fgetc(fIN);
    while (!feof(fIN)) {
        if (i == ibytenumber) {
            b = b ^ 0x01; // Altera um bit do byte escolhido
        }
        fputc(b, fOUT);
        b = fgetc(fIN);
        i++;
    }
    
    fclose(fIN);
    fclose(fOUT);
}

int main(int argc, char **argv) {
    // Verifica se foram passados os argumentos necessários (in, out, byte_number)
    if (argc < 4) {
        fprintf(stderr, "Uso: %s <ficheiro_entrada> <ficheiro_saida> <numero_do_byte>\n", argv[0]);
        return 1;
    }
    
    // argv[1] = in, argv[2] = out, argv[3] = ibytenumber (convertido de string para inteiro com atoi)
    alterbyte(argv[1], argv[2], atoi(argv[3]));
    
    return 0;
}
//EOF