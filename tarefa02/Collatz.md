# Algoritmo - Sequência de Collatz

1. Receba um número inteiro positivo N
2. Inicie a variável x com valor 0
3. Verifique se N é igual a 1.
    - Se N = 1, devolva o valor da variável x e encerre o algoritmo.
    - Senão, verifique se N é um número par.
4. Se N for um número par:
    - Faça a operação N/2
    - Some 1 à variável x
5. Caso N não seja um número par:    
    - Faça a operação 3*N + 1
    - Some 1 à variável x
6. Retorne para o comando 3, ""verificação N = 1""
