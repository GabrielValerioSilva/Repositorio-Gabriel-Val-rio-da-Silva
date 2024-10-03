#include "business.h"

void cadastrarCliente(char *nome, int idade) {
    // Validações e regras de negócio
    if (idade < 18) {
        printf("Cliente menor de idade.\n");
        return;
    }

    // Chamada para a camada de dados
    inserirCliente(nome, idade);
}

//Camada de Negócios (Business Logic): Contém a lógica do negócio, como validações, cálculos e regras de negócio.