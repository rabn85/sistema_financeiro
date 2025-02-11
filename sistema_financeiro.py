from datetime import datetime
from tabulate import tabulate
import json
import os

class SistemaFinanceiro:
    def __init__(self):
        """
        Inicializa o sistema financeiro.
        Cria uma lista para armazenar transações e define o arquivo de dados.
        """
        self.transacoes = []
        self.arquivo_dados = 'transacoes.json'
        self.carregar_dados()

    def carregar_dados(self):
        """
        Carrega as transações salvas do arquivo JSON, se existir.
        """
        if os.path.exists(self.arquivo_dados):
            with open(self.arquivo_dados, 'r') as arquivo:
                self.transacoes = json.load(arquivo)

    def salvar_dados(self):
        """
        Salva as transações em um arquivo JSON.
        """
        with open(self.arquivo_dados, 'w') as arquivo:
            json.dump(self.transacoes, arquivo, indent=4)

    def adicionar_transacao(self, tipo, descricao, valor):
        """
        Adiciona uma nova transação ao sistema.
        
        Parâmetros:
        - tipo: 'receita' ou 'despesa'
        - descricao: descrição da transação
        - valor: valor da transação
        """
        transacao = {
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tipo': tipo,
            'descricao': descricao,
            'valor': float(valor)
        }
        self.transacoes.append(transacao)
        self.salvar_dados()
        print(f"\n{tipo.capitalize()} adicionada com sucesso!")

    def calcular_saldo(self):
        """
        Calcula o saldo atual considerando todas as transações.
        """
        receitas = sum(t['valor'] for t in self.transacoes if t['tipo'] == 'receita')
        despesas = sum(t['valor'] for t in self.transacoes if t['tipo'] == 'despesa')
        return receitas - despesas

    def exibir_relatorio(self):
        """
        Exibe um relatório completo das transações e saldo.
        """
        if not self.transacoes:
            print("\nNenhuma transação registrada.")
            return

        # Prepara os dados para exibição em tabela
        dados_tabela = [[t['data'], t['tipo'].capitalize(), t['descricao'], 
                        f"R$ {t['valor']:.2f}"] for t in self.transacoes]
        
        print("\n=== Relatório Financeiro ===")
        print(tabulate(dados_tabela, 
                      headers=['Data', 'Tipo', 'Descrição', 'Valor'],
                      tablefmt='grid'))
        
        saldo = self.calcular_saldo()
        print(f"\nSaldo atual: R$ {saldo:.2f}")

def menu():
    """
    Exibe o menu principal do sistema e gerencia as interações do usuário.
    """
    sistema = SistemaFinanceiro()
    
    while True:
        print("\n=== Sistema de Controle Financeiro ===")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Exibir Relatório")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            descricao = input("Descrição da receita: ")
            valor = float(input("Valor da receita: R$ "))
            sistema.adicionar_transacao('receita', descricao, valor)
        
        elif opcao == '2':
            descricao = input("Descrição da despesa: ")
            valor = float(input("Valor da despesa: R$ "))
            sistema.adicionar_transacao('despesa', descricao, valor)
        
        elif opcao == '3':
            sistema.exibir_relatorio()
        
        elif opcao == '4':
            print("\nSaindo do sistema...")
            break
        
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()
