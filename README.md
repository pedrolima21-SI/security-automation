# Security Automation

## Objetivo

Repositório dedicado a ferramentas, utilitários e práticas de automação em Python para apoio a tarefas repetitivas, organização de dados e documentação técnica.

## Estado

**Em desenvolvimento.**

A estrutura inicial já inclui documentação e organização de exemplos. A primeira ferramenta em execução está focada em revisão local e segura de arquivos CSV, sem expor conteúdo sensível.

## Ferramenta atual

- [`scripts/review_csv.py`](scripts/review_csv.py): valida estrutura de CSV local, checa colunas obrigatórias, conta linhas de dados e identifica campos vazios sem imprimir valores das células.
- [`docs/review-csv.md`](docs/review-csv.md): documentação da ferramenta e exemplos de uso.
- [`examples/sample.csv`](examples/sample.csv): arquivo sintético para testes seguros.

## Estrutura

```text
.
├── docs/
│   ├── review-csv.md
│   └── tool-guidelines.md
├── examples/
│   ├── README.md
│   └── sample.csv
├── scripts/
│   ├── README.md
│   └── review_csv.py
├── tests/
│   └── test_review_csv.py
├── README.md
├── LICENSE
└── .gitignore
```

## Como usar

1. Revise os requisitos em [`docs/review-csv.md`](docs/review-csv.md).
2. Use somente dados próprios, públicos ou com autorização explícita.
3. Para validar a ferramenta localmente:

```bash
python scripts/review_csv.py examples/sample.csv --required-column record_id --required-column status
```

## Princípios

- clareza antes de execução
- validação de entrada
- previsibilidade e controle
- uso responsável
- documentação mínima obrigatória

## Licença

MIT. Consulte [`LICENSE`](LICENSE).

## Contato

[LinkedIn](https://www.linkedin.com/in/pedro-lima-sec) · [E-mail](mailto:pedrovitor.lima211@gmail.com)
