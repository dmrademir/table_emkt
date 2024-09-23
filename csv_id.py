import codecs
import os
import fnmatch
import pandas as pd



file_path = 'D:/ADEMIR 2-22/PYTHON/EMKT'

arquivo_csv = []

for arquivo in os.listdir(file_path):
    if fnmatch.fnmatch(arquivo,'*.csv'):
        arquivo_csv.append(arquivo)




df = pd.read_csv(arquivo_csv[0], encoding='cp850', sep=';', names=['Nome produto'])
#df.head()

#colunas = pd.DataFrame(df, columns=['Nome produto','Endereþo do Produto (URL Tray)','Preþo venda','Preþo promoþÒo'])


#print(df.head())


for k in df.values:
    print(k)

# print(arquivo_csv)