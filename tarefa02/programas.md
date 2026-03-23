# Linguagens de programação

## Exercício 2.a
Primeiro programa:
+ lista: tipo list (lista de inteiros)
+ mínimo: tipo int
+ valor: tipo int (variável do laço *for*)
Segundo programa:
+ senha: tipo str
+ senha_digitada: tipo str
+ tentativas: tipo int

## Exercício 2.b
### Estruturas identificadas:
Primeiro programa:
    + **Estruturas identificadas**
      - for (interação limitada)
      - if (execução condicional)
    + **Sintaxe**
        - for <variável> in <lista>:
              <comandos>
        - if <condição>:
             <comandos>
Segundo Programa:
    + **Estruturas identificadas**
      - while (interação condicional)
      - if/else (execução condicional)
    + **Sintaxe**
        - while <condição>
              <comandos>
        - if <condição>:
             <comandos>
          else:
             <comandos>

## Exercício 2.c
- Apenas no segundo programa (rotina de verificação de senha) foi utilizada interação condicional, porque não tem como saber quantas vezes o usuário vai tentar inserir a senha até acertar.
- É possivel reescrever p primeiro programa utilizando o comando *while* para percorrer a lista, mas o comando *for* é melhor por percorrer todos os elementos. Já o segundo programa poderia ser reescrito com o comando *for* apenas se tivesse um limite de tentativas pré-definidas, porém haveria uma modificação do programa, uma vez que o comando *while* executa a repetição até que a senha correta seja digitada.