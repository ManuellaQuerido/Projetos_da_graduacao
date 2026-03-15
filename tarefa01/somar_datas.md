# somar datas.md 1 

## **Exercício 1.a**

Problema: Somar qualquer número de dias a uma data, no qual, irá originar uma nova data existente no calendário.

Entradas: conjunto de datas no modelo dd/mm/aa, em que:
- 01 <= dd <= 31
- 01 <= mm <= 12 
- aa seja um número natural (conjunto N)
- E que o conjunto de dias que serão acrescentados seja N >= 0, sendo N um número natural.

Saídas: conjunto de novas datas existentes no calendário no formato dd/mm/aa, em que 01 <= dd <= 31, 01 <= mm <= 12 e aa seja um número natural (conjunto N).

Relação: A saída será a nova data gerada pelo acréscimo de N dias sucessivos à data adicionada anteriormente, seguindo o padrão:
- 01 <= dd <= 31
- 01 <= mm <= 12 
- aa seja um número natural (conjunto N)
- E que o conjunto de dias que serão acrescentados seja N >= 0, sendo N um número natural
- A mudança do mês quando dd atingir o número limite de dias do mês (Nl)
- Considera-se que mm == 02 (fevereiro) tenha o Nl = 28.
- Considera-se que mm == 01 (janeiro), mm == 03 (março), mm == 05 (maio), mm == 07 (julho), mm == 08 (agosto), mm == 10 (outubro) ou mm == 12 (dezembro) tenha Nl = 31
- Considera-se que mm == 04 (abril), mm == 06 (junho), mm == 09 (setembro) ou mm == 11 (novembro) tenha Nl = 30

## **Exercício 1.b**

### Instruções elementares:
- Ler os valores colocados na entrada
- Realizar a operação de soma com números inteiros
- Fazer comparações de valores
- Repetir as intruções, se necessário

### Algoritmo:
Início
- Entrada de dados
    (1) Escreva ("Digite o dia da data escolhida:")
        (1.1) Leia o valor em dd
    (2) Escreva ("Digite o mês da data escolhida:")
        (2.1) Leia o valor em mm
    (3) Escreva ("Digite o ano da data escolhida:")
        (3.1) Leia o valor em aa
    (4) Escreva dd/mm/aa
    (5) Escreva ("Digite o número para somar a data escolhida":)
        (5.1) Leia o valor em n
    
## **Exercício 1.c**