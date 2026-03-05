#!/bin/bash

echo "================================================="
echo "  Execução das Tarefas Práticas - Criptologia"
echo "================================================="

# Verifica se o texto.txt existe. Se não, avisa o utilizador.
if [ ! -f "texto.txt" ]; then
    echo "ERRO: O ficheiro 'texto.txt' não foi encontrado."
    echo "Por favor, crie o ficheiro conforme pedido na Tarefa 2 antes de correr o script."
    exit 1
fi

echo -e "\n[+] Tarefa 3: A comprimir texto.txt para comprimido.zip..."
zip comprimido.zip texto.txt

echo -e "\n[+] Tarefa 4: A cifrar texto.txt para cifrado.aes..."
openssl enc -aes-128-cbc -K 0123456789abcdef0123456789abcdef -iv 00000000000000000000000000000000 -in texto.txt -out cifrado.aes

echo -e "\n[+] Tarefa 5 (Passo 1): A cifrar comprimido.zip para comprimido-e-cifrado.zip.aes..."
openssl enc -aes-128-cbc -K 0123456789abcdef0123456789abcdef -iv 00000000000000000000000000000000 -in comprimido.zip -out comprimido-e-cifrado.zip.aes

echo -e "\n[+] Tarefa 5 (Passo 2): A comprimir cifrado.aes para cifrado-e-comprimido.aes.zip..."
zip cifrado-e-comprimido.aes.zip cifrado.aes

echo -e "\n================================================="
echo "  RESULTADOS PARA A TABELA (Tamanho e Entropia)"
echo "================================================="

# CORREÇÃO AQUI: Lista convertida numa string separada por espaços (compatível com 'sh')
ficheiros="texto.txt comprimido.zip cifrado.aes comprimido-e-cifrado.zip.aes cifrado-e-comprimido.aes.zip"

# Itera sobre os ficheiros e chama o script Python para cada um
for ficheiro in $ficheiros; do
    if [ -f "$ficheiro" ]; then
        echo -e "\n--- Analisando: $ficheiro ---"
        # Mostra o tamanho usando o comando 'du' em KB
        tamanho=$(du -k "$ficheiro" | cut -f1)
        echo "Tamanho no disco: $tamanho KB"
        
        # Chama o script Python
        python3 entropia.py "$ficheiro"
    else
        echo -e "\n--- Analisando: $ficheiro ---"
        echo "Ficheiro não encontrado. Alguma operação falhou."
    fi
done

echo -e "\n[+] Processo concluído!"

#eof