import pandas as pd
import plotly.express as px

# Passo 1: Importar a base de dados
tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Visualizar base de dados
# - Entender as informções que temos
# print(tabela)
# - Descobrir 'cagadas' e corrigi-las
tabela = tabela.drop('Unnamed: 0', axis=1)


# Passo 3: Tratamento de dados
# print(tabela.info())
# - valores reconhecidos de forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# - valores vazios
# Colunas complentamente vazias
tabela = tabela.dropna(how='all', axis=1)
# linhas com pelo menos 1 valor vazio
tabela = tabela.dropna(how='any', axis=0)
# print(tabela.info())

# Passo 4: Análise inicial do problema a ser resolvido
print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Passo 5: Análise completa entendendo o motivo do cancelamento
# como cada coluna impacto no cancelamento
for c in tabela.columns:
    grafico = px.histogram(tabela, x=c, color='Churn', text_auto=True)
    grafico.show() 

