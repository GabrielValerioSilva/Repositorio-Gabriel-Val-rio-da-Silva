#include<stdio.h>

#define linhas 3

#define colunas 4

int main(int argc, char** argv){

           float matriz[linhas][4]={

           {3,2,3,3},

           {1,3,1,-6},

           {5,1,3,12}

           };

           float x[linhas],soma;

           int j,i,k;

           float divisao;

            //imprime a matriz

           printf("\n");

           for(i=0;i<=(linhas-1);i++){

                       printf("|\t");

                       for(j=0;j<=linhas;j++){

                                   printf("%.2f\t",matriz[i][j]);

                       }

                       printf("|\t\n");

           }

           printf("\n\n");

           for(j=0;j<=linhas;j++){

                       for(i=0; i<=(linhas-1); i++){

                                   if(i>j){

                                              divisao=matriz[i][j]/matriz[j][j];

                                              for(k=0;k<=linhas;k++){

                                                                      matriz[i][k]=matriz[i][k]-divisao*matriz[j][k];

                                              }

                                   }

                       }

           }

           for(i=linhas-1;i>=0;i--){

                       soma=0;

                       for(j=i+1;j<=linhas-1;j++){

                                   soma=soma+matriz[i][j]*x[j];

                       }

                       x[i]=(matriz[i][linhas]-soma)/matriz[i][i];

           }

           for(i=0; i<=linhas-1; i++){

                       printf("x%d =\t%.2f\n",i+1,x[i]);

           }

           return 0;

}