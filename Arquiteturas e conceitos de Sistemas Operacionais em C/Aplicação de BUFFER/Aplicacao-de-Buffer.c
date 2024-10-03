#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file; // FILE* é um ponteiro para uma estrutura que contém informações sobre o estado de um arquivo aberto
    char buffer[256]; // Buffer para armazenar dados lidos (array de caracteres)
    size_t bytesRead; // Quantidade de dados lidos

    // Abre o arquivo para leitura
    file = fopen("notasSistema.txt", "r");
    if (file == NULL) {
        return 1;
    }

    // Lê os dados do arquivo em blocos e armazena no BUFFER
    while ((bytesRead = fread(buffer, 1, sizeof(buffer) - 1, file)) > 0) {
        buffer[bytesRead] = '\0'; // Adiciona um caractere nulo para formar uma string
        printf("%s", buffer); // Mostra o buffer
    }

    // Fecha o arquivo que foi declarado no início
    fclose(file);

    return 0;
}
