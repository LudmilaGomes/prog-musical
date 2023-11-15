#include <stdio.h>
#include "z_libpd.h"

/*
a pasta que armazena os arquivos questao1.c, questao1.pd e Makefile
foi colocada dentro da pasta 'libpd'; por isso, no Makefile:
LIBPD_DIR = ../
*/

/*
Faça um patch simples que possua dois fluxos: um para multiplicar um número 
recebido por dois e outro para dividir um número recebido por dois. Faça um 
programa em C que solicite um número do usuário e, caso ele seja par envie 
para o patch de tal forma que o número seja dividido por dois; caso seja ímpar
envie para o patch de tal forma que ele seja multiplicado por dois. Exiba o 
resultado recebido do Puredata e finalize o programa.
*/

int var_global;

// tudo que é enviado para o 'send' do puredata é exibido por essa função
void pddouble(const char *s, double x) 
{
  var_global = x; // guardamos o valor recebido do puredata em uma variável global do programa
  // assim, se necessário, o valor recebido pode ser usado no programa
  printf("double: %.12f\n", x); // exibe mensagem do puredata
}

int main()
{
  // variáveis usadas
  char *str_inlet;
  int numero;
  printf("Digite um valor inteiro: ");
  scanf("%d", &numero); // armazena valor de entrada do usuário
  // se número é par: valor é enviado para inlet [r par] do puredata
  if (numero % 2 == 0)
    str_inlet = "par";
  else // se número é ímpar: valor é enviado para inlet [r impar] do puredata
    str_inlet = "impar";

  libpd_set_doublehook(pddouble); // uso da função definida acima
  libpd_init(); // inicializa libpd
  libpd_bind("res"); // define de onde as mensagens são recebidas do puredata

 // abre patch .pd
  void *point_hand = libpd_openfile("questao1.pd", ".");
  if (!point_hand) // se houver erro, retorna -1
    return -1;
  
  libpd_start_message(1); // indica tamanho máximo de elementos da mensagem enviada para pd
  libpd_float(str_inlet, numero); // valor recebido vai para receive 'par' ou 'impar' do pd

  libpd_closefile(point_hand); // fecha arquivo
  
  printf("Valor recebido do Pd (int): %d\n", var_global);
  printf("Fim do programa.\n");
  return 0;
}