# Sistema de Controle Financeiro

Um sistema simples para controle financeiro desenvolvido em Python.

## Funcionalidades

- Adicionar receitas
- Adicionar despesas
- Visualizar relatório financeiro com saldo atual
- Salvar dados em arquivo JSON

## Como usar

1. Primeiro, instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

2. Execute o programa:
```bash
python sistema_financeiro.py
```

3. Use o menu interativo para:
   - Adicionar receitas
   - Adicionar despesas
   - Visualizar relatório
   - Sair do sistema

## Estrutura do Código

O sistema foi desenvolvido de forma organizada e comentada para facilitar o aprendizado:

- `SistemaFinanceiro`: Classe principal que gerencia todas as operações
- Funções principais:
  - `adicionar_transacao()`: Registra receitas e despesas
  - `calcular_saldo()`: Calcula o saldo atual
  - `exibir_relatorio()`: Mostra todas as transações em formato tabular
  - `salvar_dados()`: Persiste os dados em arquivo JSON

## Observações

- Os dados são salvos automaticamente após cada transação
- O relatório mostra todas as transações em ordem cronológica
- O saldo é calculado considerando receitas (positivo) e despesas (negativo)
