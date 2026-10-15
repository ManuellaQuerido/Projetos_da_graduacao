# Projetos da graduação

Repositório pessoal para organizar exercícios, estudos e trabalhos desenvolvidos durante a graduação em Engenharia de Computação na Unicamp.

Este espaço funciona como arquivo acadêmico e registro de aprendizagem. Os códigos podem estar incompletos ou em desenvolvimento; confira as instruções de cada atividade antes de executar qualquer arquivo.

## Disciplina: MC102 — Algoritmos e Programação de Computadores

As pastas `tarefa00` a `tarefa10`, além de `tarefa91` e `tarefa92`, agrupam atividades, soluções em desenvolvimento e arquivos de apoio da disciplina.

Dependendo da tarefa, você poderá encontrar:

- programas e scripts;
- enunciados e anotações em Markdown;
- arquivos de entrada e saídas esperadas para testes;
- scripts de teste e outros materiais de apoio.

### Como navegar

1. Abra a pasta da tarefa desejada.
2. Leia os enunciados ou arquivos `.md`, quando existirem.
3. Confira os comentários e as entradas esperadas pelo programa.
4. Execute os testes somente conforme as instruções da atividade.

## Executar programas

Alguns exercícios usam Python 3. Quando um programa não depender de arquivos ou de uma entrada específica, ele pode ser executado com:

```bash
python3 caminho/do/arquivo.py
```

Por exemplo, para um arquivo chamado `bomdia.py` na pasta `tarefa00`:

```bash
python3 tarefa00/bomdia.py
```

Esse comando é apenas um exemplo: alguns exercícios leem dados pela entrada padrão ou exigem arquivos de entrada. Verifique o enunciado e o código antes de executar.

## Estrutura atual

```text
Projetos_da_graduacao/
├── tarefa00/
├── tarefa01/
├── tarefa02/
├── tarefa03/
├── ...
├── tarefa10/
├── tarefa91/
├── tarefa92/
├── trabalhos_mc102/  # referência Git aninhada; revisar separadamente
├── .gitignore
└── README.md
```

A pasta `trabalhos_mc102` está registrada como uma referência Git aninhada (submódulo), e não como uma pasta comum navegável. Ela precisa ser revisada antes de qualquer alteração estrutural, para preservar os arquivos e o histórico existentes.

## Boas práticas

- Mantenha cada atividade na pasta correspondente.
- Prefira nomes de arquivos descritivos e consistentes.
- Não versione senhas, tokens, arquivos `.env` ou dados pessoais.
- Evite incluir caches, arquivos temporários e resultados gerados automaticamente, salvo quando fizerem parte dos testes da atividade.
- Faça commits pequenos, com mensagens que expliquem a alteração.

## Uso acadêmico

Este repositório registra meu processo de aprendizagem. Caso você também esteja cursando uma disciplina, use os materiais de forma responsável e siga as regras de colaboração e entrega definidas pela equipe docente.
