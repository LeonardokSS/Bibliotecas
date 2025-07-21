import pandas as pd

Dicionário = {
 "Nomes": ["Ana", "Bruno", "Carlos"],
 "Idades": [23, 34, 45],
}

#Leitura de um dicionário e conversão para DataFrame
di = pd.DataFrame(Dicionário)
print (di)

#Lê o arquivo Excel e carrega a tabela em um DataFrame
ex = pd.read_excel('cardapio_restaurante.xlsx', sheet_name='Cardápio')
print(ex)

#Leitura de arquivos em um banco de dados
Bc = pd.read_csv('funcionarios.csv')
print(Bc)

#Leitura de JSON e conversão para DataFrame
Js = pd.read_json('pratos.json')
print(Js)

# Leitura dos 5 primeiros e últimos registros de um DataFrame
#Isso tranforma o dicionário em um DataFrame
df = pd.DataFrame(Dicionário)

df.head()
df.tail()
