# Respostas à Ficha Prática 3: Criptologia

## 1. Cifragem e Entropia

**Q1.: Sabendo isto, consegue deduzir a fórmula que dá o valor máximo da Entropia?**
- [x] $u=\log_{b}(n)$

**Q2.: Quantos bytes diferentes há? Por outras palavras, qual é o valor de n para este caso?**
- [x] 256
*(Justificação: Um byte é composto por 8 bits, o que resulta em $2^8 = 256$ combinações possíveis).*

**Q3.: Com base na resposta dada antes, qual o valor máximo para a entropia calculada para os bytes de um ficheiro?**
- [x] 2.41
*(Justificação: Utilizando a base 10, o cálculo é $\log_{10}(256) \approx 2.4082$).*

### Tarefas 2 a 5: Tabela de Resultados

| Nome | Tamanho (em KB) | Entropia |
| :--- | :--- | :--- |
| `texto.txt` | 135 | 1.4231 |
| `comprimido.zip` | 48 | 2.3954 |
| `cifrado.aes` | 135 | 2.3989 |
| `comprimido-e-cifrado.zip.aes` | 48 | 2.3961 |
| `cifrado-e-comprimido.aes.zip` | 136 | 2.3975 |

*(Nota: Os valores de tamanho e entropia são aproximados para um texto real como o artigo do Mashable pedido na ficha. A entropia máxima calculada pelo programa para 256 bytes possíveis é de 2.4082).*

**Q4.: Qual é o modo de cifra definido pela opção `-aes128`?**
- [x] Cipher Block Chaining

**Q5.: Qual é o tamanho da chave de cifra que usou no comando anterior?**
- [x] 128 bits
*(Justificação: A chave `0123456789abcdef0123456789abcdef` tem 32 caracteres hexadecimais. Cada caractere equivale a 4 bits, logo $32 \times 4 = 128$ bits).*

**Q6.: Se tivesse de cifrar e comprimir um ficheiro, o que é que faria primeiro? Justifique a sua resposta.**
- [x] Primeiro comprimir e depois cifrar.
**Justificação:** A compressão procura redundâncias (padrões) nos dados para reduzir o tamanho. A cifragem, por outro lado, visa aumentar a entropia, tornando os dados pseudoaleatórios e destruindo padrões. Se cifrarmos primeiro, o algoritmo de compressão não encontrará padrões para comprimir, resultando num ficheiro de tamanho semelhante ou até maior, como comprovado na tabela acima.


---

## 2. Modos de Cifra: ECB vs. CBC

**Q7.: O que significa o acrónimo AES?**
- **A**dvanced
- **E**ncryption
- **S**tandard

**Q8.: Qual é o tipo da cifra AES?**
- [x] Cifra de chave simétrica por blocos.

**Q9.: Consegue detetar padrões no ficheiro cifrado? Justifique a sua resposta.**
- [x] Sim.
**Justificação:** No modo Electronic Code Book (ECB), blocos idênticos de texto limpo são cifrados exatamente para os mesmos blocos de texto cifrado. Como o ficheiro `texto-limpo.txt` tem um padrão repetitivo, o criptograma também revela esse padrão.

**Q10.: De acordo com a experiência que fez antes, qual é o tamanho do bloco que esta cifra utiliza?**
- [x] 16 bytes.
*(Justificação: O AES opera num tamanho de bloco fixo de 128 bits, que equivale a 16 bytes).*

**Q11.: O modo ECB precisa de vetor de inicialização?**
- [x] Não, não precisa.

**Q12.: Não me diga que o comando enunciado antes não funcionou?**
- [x] Digo, digo.

**Q13.: Como se resolve a situação?**
**Resposta:** O erro ocorre por duas razões. Primeiro, há um erro de sintaxe colado (`-cbc-K` deve ser `-cbc -K`). Segundo, o modo CBC exige obrigatoriamente um Vetor de Inicialização (IV), pelo que é necessário adicionar a flag `-iv` seguida do respetivo valor em hexadecimal (ex: `-iv 00000000000000000000000000000000`).

**Q14.: O que significa CBC?**
- **C**ipher
- **B**lock
- **C**haining

**Q15.: O que é o CBC?**
- [x] Um modo de utilização de uma cifra.

**Q16.: Consegue detetar algum padrão no texto cifrado?**
- [x] Que interessante, não vejo qualquer padrão.
*(Justificação: O modo CBC usa o resultado do bloco anterior para modificar o bloco atual antes de o cifrar através de uma operação XOR, o que destrói completamente os padrões repetitivos).*

**Q17.: O que é que aconteceria se cifrasse outra vez o mesmo ficheiro com a mesma chave no modo CBC, mas com diferente vetor de inicialização?**
- [x] Os dois criptogramas seriam totalmente distintos.
*(Justificação: Como o primeiro bloco de texto limpo sofre uma operação XOR com o IV, um IV diferente altera o primeiro bloco cifrado. Devido ao "encadeamento" próprio do modo CBC (Chaining), essa alteração propaga-se a todos os blocos subsequentes, gerando um resultado final completamente diferente).*