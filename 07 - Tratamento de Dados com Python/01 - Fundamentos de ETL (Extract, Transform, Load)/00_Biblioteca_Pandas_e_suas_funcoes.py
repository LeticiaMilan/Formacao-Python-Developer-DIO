import pandas as pd
import matplotlib.pyplot as plt


'''

    Os dois principais objetos da biblioteca Pandas são as Series e os DataFrames:

'''

# Dados utilizados na Série
dados_serie = [10, 20, 30, 40, 50]

# Criando a Série
serie = pd.Series(dados_serie)

# Exibindo a Série
print(serie)
print("\n")


# Dados utilizados no DataFrame
dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Exibindo o DataFrame
print(df)
print("\n")


'''

    Para visualizar os 2 primeiros dados do nosso DataFrame:

'''

print(df.head(n=2))
print("\n")


'''

    Para visualizar a quantidade de linhas e colunas do nosso DataFrame:

'''

print(df.shape)
print("\n")



'''

    Para saber que formato se encontram os dados de cada coluna, além da quantidade de memória para ler esses dados:

'''

print(df.info())
print("\n")



'''

    Para verificar quais são as colunas existentes:

'''

print(df.columns)
print("\n")



'''

    Para verificar quantos dados faltantes existem:

'''

print(df.isnull().sum())
print("\n")




'''

    Para verificar quais os valores únicos existentes na coluna (EX: Cidade):

'''

print(df['Cidade'].unique())
print("\n")



'''

    Para visualizar dados estatísticos:

'''

print(df.describe())
print("\n")



'''

    Para visualizar agrupamentos simples com o auxilio da biblioteca Matplotlib, com o método plot:

'''

df['Cidade'].value_counts().plot(kind='bar')    # Agrupamento simples
plt.title('Contagem de Pessoas por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Contagem')
plt.show()  # Exibe o gráfico