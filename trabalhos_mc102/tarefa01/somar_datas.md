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

**INÍCIO**
1. Receba os valores:
    - dd (dia)
    - mm (mês)
    - aa (ano)
    - n (quantidade de dias a somar)
2.  Enquanto n > 0, faça:
   2.1 Determine **Nl**:
        2.1.1 Se mm = 02, então Nl = 28
        2.1.2 Se mm = 4, 6, 9 ou 11, então Nl = 30
        2.1.3 Caso contrário Nl = 31
    2.2 Some **n** ao dia:
    dd = dd + n
    2.3 Se dd > Nl, então:
    dd = dd - Nl
    mm = mm + 1
    2.4 Se mm > 12, então:
    mm = 1
    aa = aa + 1
3. A nova data será **dd/mm/aa**

**FIM**

## **Exercício 1.c**
Problema: Somar qualquer número de dias úteis a uma data, no qual, irá originar uma nova data existente no calendário.

Entradas: conjunto de datas no modelo dd/mm/aa, em que:
- 01 <= dd <= 31
- 01 <= mm <= 12
- aa seja um número natural (conjunto N)
- 01 <= ds <= 05 (01 = segunda-feira e 05 = sexta-feira)
- E que o conjunto de dias que serão acrescentados seja N >= 0, sendo N um número natural.

Saídas: conjunto de novas datas existentes no calendário no formato dd/mm/aa, em que 01 <= dd <= 31, 01 <= mm <= 12 e aa seja um número natural (conjunto N).

Relação: A saída será a nova data gerada pelo acréscimo de N dias úteis à data adicionada anteriormente, seguindo o padrão:
- 01 <= dd <= 31
- 01 <= mm <= 12
- aa seja um número natural (conjunto N)
- E que o conjunto de dias que serão acrescentados seja N >= 0, sendo N um número natural
- A mudança do mês quando dd atingir o número limite de dias do mês (Nl)
- Considera-se que mm == 02 (fevereiro) tenha o Nl = 28.
- Considera-se que mm == 01 (janeiro), mm == 03 (março), mm == 05 (maio), mm == 07 (julho), mm == 08 (agosto), mm == 10 (outubro) ou mm == 12 (dezembro) tenha Nl = 31
- Considera-se que mm == 04 (abril), mm == 06 (junho), mm == 09 (setembro) ou mm == 11 (novembro) tenha Nl = 30
Porém, serão considerados na contagem como dias úteis apenas aqueles entre segunda-feira e sexta-feira. Se a contagem der sábado ou domingo, será passado para o próximo dia útil.

Diferença entre os problemas:
No original, **todos** os diass foram considerados. E no problema modificado, apenas os dias úteis são contabilizados, sendo necessário ter conhecimento do dia da semana da data inicial para identificar os dias que devem ser contabilizados.