#include <stdio.h>
#include <math.h>

//Método da bisseção-função: f(x)= x-2^-x

int main(){

   double a=0, b=1, m, precisao = 0.00001, p; //Aqui, três variáveis do tipo `double` são declaradas e inicializadas. `a` e `b` representam os extremos esquerdo e direito do intervalo inicial, respectivamente. `m` será o ponto médio do intervalo. `precisao` é a precisão desejada para a solução.

   int i=1;  //Declara e inicializa um contador `i` que será usado para acompanhar o número de iterações do método.

   printf("\n ITERACOES:  Int.   A1        B1      M     F(m)    "); //Esta linha imprime um cabeçalho para os dados que serão impressos durante as iterações do método.



   do{//Esta é uma estrutura de repetição do-while que executa o bloco de código entre as chaves `{}` pelo menos uma vez e continua repetindo enquanto a diferença entre `a` e `b` for maior que a precisão desejada.

       m = (a+b)/2; //ponto médio(Pxn)

       printf("\n Iteracao: %5d   %.5f   %.5f  %.5f  %.5f", i, a, b, m,(m - pow(2,-m)));

       if( ( a - pow(2,-a))* (m - pow(2,-m)) < 0){// `pow` é uma função em C (e em muitas outras linguagens de programação) que calcula a potência de um número.
        //verificar se o produto das diferenças \( (a - 2^{-a}) \times (m - 2^{-m}) \) é positivo ou negativo para determinar em qual metade do intervalo a raiz está localizada.
           b = m;

       }else{

           a = m;

       }

      i++;
//Este trecho de código está determinando em qual metade do intervalo [a, b] a raiz da função \( f(x) = x - 2^{-x} \) se encontra, conforme o método da bisseção.
// A condição `(a - pow(2, -a)) * (m - pow(2, -m)) < 0` verifica se o produto das diferenças entre \(a - 2^{-a}\) e \(m - 2^{-m}\) é negativo. Se for, isso significa que os sinais dessas diferenças são opostos, o que indica que a raiz está entre `a` e `m`, então atualizamos `b = m`.
//Caso contrário, se o produto for maior ou igual a zero, os sinais são iguais, o que significa que a raiz está entre `m` e `b`, então atualizamos `a = m`.

//`i++` incrementa o contador de iterações.

    }while(fabs(a-b)>precisao);

   return 0;

 }