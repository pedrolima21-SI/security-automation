# Revisão de CSV local

`review_csv.py` verifica um CSV local sem fazer requisições de rede, editar o arquivo ou imprimir valores das células. Informa apenas contagens agregadas e nomes de colunas obrigatórias ausentes.

## Requisitos

- Python 3.10+
- apenas biblioteca padrão

## Uso

Na raiz do repositório:

```bash
python scripts/review_csv.py examples/sample.csv --required-column record_id --required-column status
```

## Resultados esperados

- **Código 0**: CSV válido e com preenchimento obrigatório correto.
- **Código 1**: CSV com coluna obrigatória ausente ou valor obrigatório vazio.
- **Código 2**: arquivo não encontrado, inválido ou não legível.

## Exemplos de contexto

- dados sintéticos de laboratório local
- exportação de uma planilha com dados próprios
- conjunto de dados autorizado para processamento local

## Limitações

- A ferramenta valida estrutura e preenchimento, mas não interpreta conteúdo semântico.
- Use somente arquivos próprios ou com autorização explícita.
- Não substitui controles de acesso, auditoria ou revisão de negócio.
