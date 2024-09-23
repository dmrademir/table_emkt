import chardet
import fnmatch
import os
import pandas as pd

#os.remove('arquivo_utf8.csv')

directory = 'D:/ADEMIR 2-22/PYTHON/EMKT'

arquivo_csv = []

for arquivo in os.listdir(directory):
    if fnmatch.fnmatch(arquivo, '*.csv'):
        arquivo_csv.append(arquivo)



file_path = f'D:/ADEMIR 2-22/PYTHON/EMKT/{arquivo_csv[0]}'

#print(file_path)

with open(file_path, 'rb', ) as f:
    result = chardet.detect(f.read())
    original_encoding = result['encoding']



df = pd.read_csv(arquivo_csv[0], encoding=original_encoding, sep=';')
df.to_csv('arquivo_utf8.csv', index=False, encoding='utf-8')

df_utf8 = pd.read_csv('arquivo_utf8.csv', encoding='utf-8',sep=',',index_col=False, usecols=['Nome produto', 'Imagem principal','Endereço do Produto (URL Tray)','Preço venda','Preço promoção'])

# print(df_utf8)

nome_produto = []
img_produto = []
preco_produto = []
oferta_produto = []
url_produto = []


for k in df_utf8.values:
    nome_produto.append(k[0])
    img_produto.append(k[1])
    preco_produto.append(k[2])
    oferta_produto.append(k[3])
    url_produto.append(k[4])


print(nome_produto[0])
print(img_produto[0])
print(preco_produto[0])
print(oferta_produto[0])
print(url_produto[0])