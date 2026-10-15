# Projetos da graduação

Repositório pessoal para organizar exercícios, estudos e trabalhos desenvolvidos durante a graduação em Engenharia de Computação na Unicamp.

Este espaço funciona como arquivo acadêmico e registro de aprendizagem. Os códigos podem estar incompletos ou em desenvolvimento; confira os enunciados e as instruções de cada atividade antes de executar qualquer arquivo.

## Disciplina: MC102 — Algoritmos e Programação de Computadores

Os materiais da disciplina estão reunidos na pasta **[`trabalhos_mc102/`](trabalhos_mc102/)**. As atividades estão organizadas por pasta, de acordo com a numeração das tarefas.

### Atividades disponíveis

- `tarefa00` a `tarefa10`
- `tarefa91`
- `tarefa92`

Conforme a atividade, as pastas podem conter:

- programas e scripts em Python;
- enunciados e anotações em Markdown;
- arquivos de apoio necessários para executar os exercícios.

### Como navegar

1. Abra a pasta [`trabalhos_mc102/`](trabalhos_mc102/).
2. Escolha a pasta da tarefa desejada.
3. Leia o enunciado e as instruções disponíveis antes de executar o código.
4. Verifique se o programa precisa de entrada pelo terminal ou de arquivos específicos.

### Executar um programa

Os exercícios que utilizam Python 3 podem ser executados pelo terminal com:

```bash
python3 trabalhos_mc102/tarefa00/bomdia.py
```

O caminho acima é apenas um exemplo. O arquivo e a forma de execução variam conforme a atividade; consulte o enunciado e o código antes de executar.

## Outros projetos da graduação

Além dos exercícios de MC102, este repositório reúne projetos de programação e sistemas embarcados desenvolvidos durante a graduação.

### [Processo_Trainee-Conpec](projetos/Processo_Trainee-Conpec/)

Projeto relacionado ao processo trainee da Conpec, com uma entrega em TypeScript e arquivos para uma interface web.

### [LoRaWAN](projetos/LoRaWAN/)

Projeto de comunicação LoRaWAN com ESP32, utilizando ESP-IDF e RadioLib, com foco na ativação OTAA.

### [LW](projetos/LW/)

Outra versão do projeto LoRaWAN com ESP32 e RadioLib. Mantida separadamente para preservar as diferenças entre as versões.

### [LoRa_SmartCampus](projetos/LoRa_SmartCampus/)

Projeto Smart Campus da Unicamp voltado à estimativa de distância até um gateway LoRa, utilizando informações de RSSI e filtragem dos valores medidos.

Consulte o README e os arquivos de configuração de cada projeto antes de compilar ou executar o código. Os projetos LoRaWAN podem exigir configurações específicas de hardware, região de frequência e rede.

## Estrutura do repositório

```text
Projetos_da_graduacao/
├── trabalhos_mc102/
│   ├── tarefa00/
│   ├── tarefa01/
│   ├── tarefa02/
│   ├── ...
│   ├── tarefa10/
│   ├── tarefa91/
│   ├── tarefa92/
│   └── README.md
├── projetos/
│   ├── Processo_Trainee-Conpec/
│   ├── LoRaWAN/
│   ├── LW/
│   └── LoRa_SmartCampus/
├── .gitignore
└── README.md
```

A pasta `trabalhos_mc102/` concentra os arquivos da disciplina, evitando manter cópias das tarefas diretamente na raiz do repositório. Os projetos em `projetos/` ficam em diretórios separados; seus históricos Git originais não são incorporados ao histórico deste repositório.


## Uso acadêmico

Este repositório registra meu processo de aprendizagem. Os materiais são destinados ao estudo pessoal; respeite as regras de colaboração, autoria e entrega estabelecidas pela equipe docente.
