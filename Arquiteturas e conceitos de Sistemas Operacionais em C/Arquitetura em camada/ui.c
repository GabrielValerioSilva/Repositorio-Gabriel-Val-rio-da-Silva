#include <stdio.h>
#include "business.h"

int main() {
    char nome[50];
    int idade;

    printf("Digite o nome do cliente: ");
    scanf("%s", nome);
    printf("Digite a idade do cliente: ");
    scanf("%d", &idade);

    cadastrarCliente(nome, idade);

    return 0;
}

//Camada de Apresentação (UI): Interage diretamente com o usuário, solicitando dados e exibindo resultados.