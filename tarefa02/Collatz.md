# O problema 3*n + 1
## Algoritmo - Sequência de Collatz

1. Receba um número inteiro positivo N
2. Inicie a variável x com valor 0
3. Verifique se N = 1.
    - Se N = 1, devolva o valor da variável x e encerre o algoritmo.
    - Senão, verifique se N é um número par.
4. Se N for um número par:
    - Faça a operação N/2
    - Some 1 à variável x
5. Caso N não seja um número par:    
    - Faça a operação 3*N + 1
    - Some 1 à variável x
6. Retorne para o comando 3, (verificação N = 1)
7. Repita o processo até que N = 1

## Estruturas de controle utilizadas

- Estrutura de repetição (interação condicional)
    - O algoritmo repete o processo enquanto N for diferente de 0

- Estrutura condicional
    - Há uma verificação para saber se N = 1
    - Há também uma estrutura condicional para verificar se N é par ou não.