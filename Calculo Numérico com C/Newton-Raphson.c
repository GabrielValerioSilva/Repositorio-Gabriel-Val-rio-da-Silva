#include <stdio.h>

#include <math.h>

int main() {

  float en, x0,xn;

  int i, numiter;

  en = 0.1;

  numiter=10; // Número máximo de interações

  x0=4;

   i = 0;

  xn=x0;

  do{

      x0=xn;

     if(i > numiter) { // Excedeu o limite de iterações.

        printf("Não convergiu em %d iterações!!!\n", numiter);

        printf("Provavelmente f'(x) está errada.\n");

        break;

     }

     xn = x0 - (pow(x0,2)-9)/(2*x0);

     i++;

  }while(  fabs(x0-xn)  > en) ;

  printf("X ~= %f ", xn);

  printf("\n Foram feitas %d iterações.\n",i);

}