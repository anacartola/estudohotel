#Importando Biblis 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
from scipy import stats
from scipy.stats import pearsonr

###1. Definição do Problema

##Notas da limpeza dos quartos caindo e cada vez mais moradores reclamando. Querem contratar mais faxineiras para resolver este problema.
##Preocupado com os custos, o time de finanças pediu a análise para entender se essa contratação é necessária.

###2. Coleta dos dados + Tratamento dos dados

# Primeira aba, notas
notas = pd.read_excel("Estudo Case Hotelaria.xlsx", sheet_name=0)
print(notas)
# Alterando valores da Primeira Aba (Notas) para normalizar com outra aba
notas.rename(columns={"Mês": "Mes"}, inplace=True)
notas['Mes'].replace({'2020-01-01': '1', '2020-02-01': '2','2020-03-01':'3','2020-04-01':'4','2020-05-01':'5', '2020-06-01':'6', '2020-07-01':'7', '2020-08-01':'8','2020-09-01':'9','2020-10-01':'10','2020-11-01':'11','2020-12-01':'12'}, inplace=True)
notas
#Segunda aba, registro de pagamentos
valores = pd.read_excel("Estudo Case Hotelaria.xlsx", sheet_name=1)
valores.head(5)
#Descobrir tipos e valores de pagamento
pagamentos = valores["Descrição"].value_counts().to_frame().reset_index()
pagamentos

#3. Análise Exploratória
#Descobrir total de faxinas feitas em cada mês
filtro = valores["Descrição"] == "Valor Faxina Quarto"
totallimpeza = valores[filtro]["Mes"].value_counts().to_frame().reset_index()
totallimpeza.columns = ["Mes", "Total Faxinas"]
totallimpeza = totallimpeza.sort_values(by="Mes", ascending=True)
totallimpeza["Mes"] = totallimpeza["Mes"].astype(object)
totallimpeza
## Crirar DF para Total Limpeza por Quarto
totaldelimpeza = pd.DataFrame(list(zip(notas['Mes'], totallimpeza['Total Faxinas'])), columns=['Mes', 'Limpezas Feitas'])
totaldelimpeza
#Porcentagem de Ocupação
## Subentende-se que apenas quartos ocupados recebem nota, logo a taxa de ocupação é o indicador que faz mais sentido para medir patrimônio
porcentagem_ocupacao = (notas['Moradores']/ notas["Quartos Totais"])*100
##Criar um DF para Ocupacao, incluindo o mês equivalente
ocupacao= pd.DataFrame(list(zip(notas['Mes'], porcentagem_ocupacao)), columns=['Mes', '% Ocupação'])
ocupacao
#Média de Limpeza de Quartos por Mês
## Subentende-se o total de moradores representa os quartos ocupados, ou seja, os quartos que são limpos
media_limpezaquarto = (totaldelimpeza['Limpezas Feitas']/notas['Moradores'])
media_lq = pd.DataFrame(list(zip(notas['Mes'], media_limpezaquarto)), columns=['Mes', 'Média Limpezas Realizadas'])
media_lq
#MergeDFNotas das novas colunas
df_notas = pd.merge(notas, totaldelimpeza, on= "Mes")
df_notas = pd.merge(df_notas, media_lq, on= "Mes")
df_notas = pd.merge(df_notas, ocupacao, on= "Mes").round(1)
df_notas
#Custo 
# Descobrir qual Custos/Mês por tipo de gastos
custo = valores[["Mes", "Descrição", "Valor"]]
custo = custo.groupby(["Mes","Descrição"])["Valor"].sum().reset_index(name="Custos")
custo
#Criar um DF para ordernar os custos de cada mês
## De acordo com a última análise, subentende-se que "Valor Faxina Quarto" é o custo da limpeza por quarto.
customensal = custo.pivot(index='Mes', columns='Descrição', values='Custos').reset_index()
customensal.columns.name = None
customensal.columns = ['Mes', 'Fixo Mensal', 'Custo p/ Quarto']
customensal
# Descobrir quantidade de faxineiros/mês
filtroquarto = valores["Descrição"] == "Fixo Mensal" #Filtro Quantidade Pagamentos Fixos
faxineiros = valores[filtroquarto][["Mes", "Faxineiro"]]
faxineiros = faxineiros.groupby(["Mes"])["Faxineiro"].nunique().reset_index(name="Faxineiros")
faxineiros
# Descobrir quantos quartos/faxineiro
filtroquarto = valores["Descrição"] == "Valor Faxina Quarto" #Filtro Quantidade Quartos
df = valores[["Mes", "Faxineiro","Descrição"]][filtroquarto]
df = df.groupby(["Mes","Faxineiro"])["Descrição"].size().reset_index(name="Quartos Faxinados no Mês")
df
# Descobrir quantos dias cada faxineiro trabalhou no mês
valores['Data'] = pd.to_datetime(valores['Data'])
df_faxina = valores[valores['Descrição'] == 'Valor Faxina Quarto']

## Agrupar por mês e faxineiro, contando os dias únicos
df_diaspmes = df_faxina.groupby(['Mes', 'Faxineiro'])['Data'].nunique().reset_index(name='Dias Trabalhados')

## Reordenar o DataFrame para priorizar a ordem do mês
meses_ordenados = df_diaspmes['Mes'].unique()  # Obter a ordem única dos meses
df_diaspmes['Mes'] = pd.Categorical(df_diaspmes['Mes'], categories=meses_ordenados, ordered=True)
df_diaspmes = df_diaspmes.sort_values(by=['Mes', 'Faxineiro']).reset_index(drop=True)
df_diaspmes
# Média de Limpezas/dia de cada faxineiro
## Média
media_limpezadia = pd.DataFrame(df["Quartos Faxinados no Mês"]/df_diaspmes['Dias Trabalhados'])
media_limpezadia
## Trnasformar em um novo df, incluindo mês correspondente
media_lf = pd.DataFrame({'Mes':df_diaspmes['Mes'], 'Faxineiro': df_diaspmes['Faxineiro'], 'Média Faxinas/Dia': media_limpezadia.values.ravel()})
media_lf
#MergeDFFaxinas das novas colunas
df_diaspmes = df_diaspmes.sort_values(by=['Mes', 'Faxineiro']).reset_index(drop=True)
df = df.sort_values(by='Faxineiro').reset_index(drop=True)
df_faxina = pd.merge(df_diaspmes, df, on=['Mes', 'Faxineiro'])
df_faxina = pd.merge(df_faxina, media_lf, on=['Mes', 'Faxineiro'])
df_faxina.round(2)
#Fazer uma Média de quantas faxinas são realizadas por dia em cada Mês
media_por_mes = df_faxina.groupby('Mes')['Média Faxinas/Dia'].mean().reset_index().round(2)
media_por_mes
#Fazer uma Média da capacidade de faxinas por dia de cada Funcionário
media_por_funcionario = df_faxina.groupby('Faxineiro')['Média Faxinas/Dia'].mean().reset_index().round(2)
media_por_funcionario
## Entender as estatísticas dos valores
media_por_funcionario.describe()
df_notas.describe().round(1)
df_faxina.describe().round()
## Transformar meses em colunas
faxinames = pd.crosstab(df["Faxineiro"], df['Mes'], values=df['Quartos Faxinados no Mês'], aggfunc='sum', margins=True, margins_name='Total')
faxinames.fillna(0)


# Descobrir mínimo de faxineiros necessários com o mínimo de esforço para voltando a ter uma boa nota (3 limpezas/mês)
## Dados fornecidos
salario_fixo = 1200
pagamento_quarto = 75
qntd_quartos = 182
qntd_limpezaideal= 3
faxineiros_contratados = 11
max_diastrabalhados = 24
max_faxinaspordia = 2

## Calcular quantidade total para a limpeza de quartos ideal
total_limpezaideal = qntd_quartos * qntd_limpezaideal

## Calcular capacidade máxima de limpeza de cada faxineiro
max_faxineiro = max_diastrabalhados * max_faxinaspordia

## Calcular o número mínimo de faxineiros necessários
numero_minimo_faxineiros = total_limpezaideal / max_faxineiro

## Verificar se é necessário contratar mais faxineiros
if numero_minimo_faxineiros > faxineiros_contratados:
    print(f"É necessário contratar pelo menos {round(numero_minimo_faxineiros)} faxineiros.")
else:
    print("A equipe atual é suficiente.")

## Calcular o custo total mensal
custo_fixo_min = (numero_minimo_faxineiros * salario_fixo)
custo_relativo_min = (total_limpezaideal * pagamento_quarto)
custo_total_mensal_min = custo_fixo_min +custo_relativo_min
print(f"Custo total mensal: R$ {custo_total_mensal_min:.2f}")

# Descobrir mínimo de faxineiros necessários com um maior investimento para melhorias da nota (4 limpezas/mês)
## Dados fornecidos
salario_fixo = 1200
pagamento_quarto = 75
qntd_quartos = 182
qntd_limpezaideal= 4
faxineiros_contratados = 11
max_diastrabalhados = 24
max_faxinaspordia = 2

## Calcular quantidade total para a limpeza de quartos ideal
total_limpezaideal = qntd_quartos * qntd_limpezaideal

## Calcular capacidade máxima de limpeza de cada faxineiro
max_faxineiro = max_diastrabalhados * max_faxinaspordia

## Calcular o número mínimo de faxineiros necessários
numero_minimo_faxineiros = total_limpezaideal / max_faxineiro

## Verificar se é necessário contratar mais faxineiros
if numero_minimo_faxineiros > faxineiros_contratados:
    print(f"É necessário contratar pelo menos {round(numero_minimo_faxineiros)} faxineiros.")
else:
    print("A equipe atual é suficiente.")

## Calcular o custo total mensal
custo_fixo_investido = (numero_minimo_faxineiros * salario_fixo)
custo_relativo_investido = (total_limpezaideal * pagamento_quarto)
custo_total_mensal_investido = custo_fixo_investido +custo_relativo_investido
print(f"Custo total mensal: R$ {custo_total_mensal_investido:.2f}")

###4. Visualizações
#Relacionando dados mensais de Notas e Limpezas por Quarto
fig, ax1 = plt.subplots()

color = 'tab:green'
ax1.set_xlabel('Mes')
ax1.set_ylabel('Nota Limpeza', color=color)
ax1.plot(df_notas['Mes'], df_notas['Nota Limpeza'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Instanciar um segundo eixo y compartilhando o mesmo eixo x

color = 'tab:blue'
ax2.set_ylabel('Media Limpezas Realizadas', color=color)
ax2.plot(df_notas['Mes'], df_notas['Média Limpezas Realizadas'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Dados Mensais: Notas e Média de Limpezas por Quarto')
plt.show()

#Compreender a correlação entre os elementos de notas
correlation_matrix = df_notas.corr().round(2)
plt.figure(figsize=(10, 8))
plot = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Como nossos dados mensais se relacionam?")
plt.show()

#Compreender a correlação entre as propriedades de faxineiros
corr_mat = df_faxina.corr().round(2)
plt.figure(figsize=(10, 8))
plot = sns.heatmap(corr_mat, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()

#Estatística de Dias Trabalhados pelos faxineiros
ax = df_faxina.boxplot(column=['Dias Trabalhados'])
mean_value = df_faxina['Dias Trabalhados'].mean()
ax.axhline(mean_value, color='green', linestyle='dashed', linewidth=2, label=f'Média Dias Trabalhados')

plt.title('Estatística de Dias Trabalhados')
plt.show()

#Estatística de faxinas/dia realizadas em média pelos faxineiros

ax = media_por_funcionario.boxplot()
mean_value = media_por_funcionario['Média Faxinas/Dia'].mean()
ax.axhline(mean_value, color='green', linestyle='dashed', linewidth=2, label=f'Média Faxinas por dia')

plt.title('Estatística de Média de Faxinas por dia')
plt.show()

#Comparação entre as opções de investimento de custos de faxina
categorias = ['Opção 1 (Custo Mínimo)', 'Opção Extra (Custo Ideal)']
custo_fixo = [custo_fixo_min, custo_fixo_investido]
custo_relativo = [custo_relativo_min, custo_relativo_investido]

fig, ax = plt.subplots()
ax.bar(categorias, custo_fixo, label='Custo Fixo Faxineiro', color='green')
ax.bar(categorias, custo_relativo, bottom=custo_fixo, label='Custo Relativo a Quartos', color='blue')
customensal = customensal.rename(columns={'Fixo Mensal': 'Custo Fixo', 'Custo p/ Quarto': 'Custo Relativo'})

plt.ylabel('Custo Total Mensal')
plt.title('Comparação entre as opções de custos de faxina')
plt.legend()
plt.show()