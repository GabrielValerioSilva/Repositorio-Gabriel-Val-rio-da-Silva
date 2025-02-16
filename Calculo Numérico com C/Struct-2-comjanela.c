#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

struct GPU {
   char Nvidia[8]; 
   uint16_t launch_Date; 
   double teraflops;
   float launch_price;
};

int main() {
    struct GPU video_card;
    strncpy(video_card.Nvidia, "RTX4090", sizeof(video_card.Nvidia)); 
    video_card.launch_Date = 2022;
    video_card.teraflops = 82.58;
    video_card.launch_price = 1600.0f; 

    printf("\nOlá! pressione ENTER para ver as informações.");
   

    char cmd[200];
   
    sprintf(cmd, "start cmd.exe /k echo Nome da GPU: %s, Endereço de memória da variável video_card: %p, Ano de lançamento: %d", video_card.Nvidia, (void *)&video_card, video_card.launch_Date);
    

    
    system(cmd);
    
    

    while (getchar() != '\n');

    printf("Nome da GPU: %s\n", video_card.Nvidia); // Impressão do nome da GPU
    printf("Ano de lançamento: %d\n", video_card.launch_Date); // Impressão do ano de lançamento
    printf("Endereço de memória da variável video_card: %p\n", (void *)&video_card);
  

    return 0;
}
