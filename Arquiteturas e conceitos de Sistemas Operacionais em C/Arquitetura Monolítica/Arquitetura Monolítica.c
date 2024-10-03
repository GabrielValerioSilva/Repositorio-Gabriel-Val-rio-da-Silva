//SO é contido no núcleo (kernel) e pode se comunicar com qualquer outro
//componente diretamente. Essa intercomunicação direta permite rapidez na
//resposta de sistema operacional monolítico, entretanto, como núcleos
//monolíticos agrupam os componentes, é difícil identificar a origem de um
//determinado problema ou erro
//Unidade de Código Única: Todo o código-fonte é parte de um único projeto ou solução.
//único código-base e são implantados juntos como um único aplicativo.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estrutura para armazenar informações do produto
typedef struct {
    int id;
    char nome[50];
    float preco;
} Produto;

// Banco de dados de produtos (simulação em memória)
Produto produtos[100];
int total_produtos = 0;

// Função para adicionar um novo produto
void adicionarProduto(int id, const char *nome, float preco) {
    Produto novo_produto;
    novo_produto.id = id;
    strncpy(novo_produto.nome, nome, sizeof(novo_produto.nome));
    novo_produto.preco = preco;

    produtos[total_produtos++] = novo_produto;
    printf("Produto %s adicionado com sucesso!\n", nome);
}

// Função para listar todos os produtos
void listarProdutos() {
    printf("Lista de Produtos:\n");
    for (int i = 0; i < total_produtos; i++) {
        printf("ID: %d, Nome: %s, Preço: %.2f\n",
               produtos[i].id, produtos[i].nome, produtos[i].preco);
    }
}

int main() {
    int opcao;
    while (1) {
        printf("1. Adicionar Produto\n");
        printf("2. Listar Produtos\n");
        printf("3. Abrir Bloco de Notas com 'notas.txt'\n");
        printf("4. Abrir Link no Navegador\n");
        printf("5. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        if (opcao == 1) {
            int id;
            char nome[50];
            float preco;

            printf("Digite o ID do produto: ");
            scanf("%d", &id);
            printf("Digite o nome do produto: ");
            scanf("%s", nome);
            printf("Digite o preço do produto: ");
            scanf("%f", &preco);

          adicionarProduto(id, nome, preco);
        } else if (opcao == 2) {
            listarProdutos();
        } else if (opcao == 3) {
            // Abrir o arquivo 'notas.txt' no bloco de notas
            system("notepad notas.txt");
        } else if (opcao == 4) {
            // Abrir o link no navegador
            system("start https://pt.wikipedia.org/wiki/Aplica%C3%A7%C3%A3o_monol%C3%ADtica");
        } else if (opcao == 5) {
            break;
        } else {
            printf("Opção inválida.\n");
        }
    }

    return 0;
}