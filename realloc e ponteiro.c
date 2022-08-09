/*Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

- use a função realloc;
- use a função sizeof;
- que tenha tamanho 22 de vetor;
- depois libere o bloco utilizando a função free.*/



int*ptr;

ptr = (int) malloc(10* sizeof(int));

ptr = (int*) realloc(ptr, 22* sizeof(int));

int ptr[22]

free():void free(void*ptr);
