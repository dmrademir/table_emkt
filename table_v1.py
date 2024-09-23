import codecs
import chardet
import fnmatch
import os
import pandas as pd
from Cores import colores, borders

os.remove('arquivo_utf8.csv')

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




# Cálculo para desconto dos produtos

desconto = []
base_desconto = 10 #valor condicional para mostrar o selo de desconto


for x in range(0,4): 
    if url_produto[0][11:15] == '.ruv':
        desconto.append(x)
    else:
        desconto.append(int(round(float((preco_produto[0]-oferta_produto[0])/(preco_produto[0])*100))))
        desconto.append(int(round(float((preco_produto[1]-oferta_produto[1])/(preco_produto[1])*100))))
        desconto.append(int(round(float((preco_produto[2]-oferta_produto[2])/(preco_produto[2])*100))))
        desconto.append(int(round(float((preco_produto[3]-oferta_produto[3])/(preco_produto[3])*100))))


# Variáveis para converter ponto em vírgula
p1_p = f'{preco_produto[0]:.2f}'
p1_o = f'{oferta_produto[0]:.2f}'
p2_p = f'{preco_produto[1]:.2f}'
p2_o = f'{oferta_produto[1]:.2f}'
p3_p = f'{preco_produto[2]:.2f}'
p3_o = f'{oferta_produto[2]:.2f}'
p4_p = f'{preco_produto[3]:.2f}'
p4_o = f'{oferta_produto[3]:.2f}'





# print(desconto[2])
# print(desconto[3])
        

#Estilos para os PRODUTOS

print(url_produto[0][11:15])



# Estilos para os PRODUTOS definido para o MEUCOPO
campanha = 'vermelho' #fds, madrugada, verde, vermelho, amarelo, azul,preto, gamer


if url_produto[0][11:15] == '.meu':
    if campanha == 'madrugada':
        bg_tabela = colores['sem_cor']
        bg_produto = colores['azul_madruga']  
        bg_txt = colores['branco']
        bg_botao = colores['amarelo']  
        bt_texto_cor = colores['preto']
        bordas = 'none','10px','15px'
        bg_txt = colores['branco']      
        bg_preço = colores['branco_op2']       
        bg_oferta = colores['branco']        
        bg_botao = colores['amarelo']         
        bt_texto_cor = colores['preto'] 
        bg_tag_txt_desc = colores['branco']
        bg_tag_desc = colores['azul2']
        bg_btn_whatsapp = colores['sem_cor']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['branco_fino']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓'

    if campanha == 'preto':
        bg_tabela = colores['cinza4']
        bg_produto = colores['branco']  
        bg_txt = colores['preto']
        bordas = 'none','10px','15px' 
        bg_preço = colores['cinza']       
        bg_oferta = colores['preto']        
        bg_botao = colores['preto']         
        bt_texto_cor = colores['branco'] 
        bg_tag_txt_desc = colores['branco']
        bg_tag_desc = colores['preto']
        bg_btn_whatsapp = colores['cinza']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['branco_fino']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓'
    if campanha == 'azul':
            bg_tabela = colores['sem_cor']
            bg_produto = colores['branco']  
            bg_txt = colores['azul_esc_copo']
            bt_texto_cor = colores['preto']
            bordas = 'none','10px','15px'
            bg_txt = colores['azul_esc_copo']      
            bg_preço = colores['cinza']       
            bg_oferta = colores['azul_esc_copo']        
            bg_botao = colores['azul6']         
            bt_texto_cor = colores['azul5'] 
            bg_tag_txt_desc = colores['azul5']
            bg_tag_desc = colores['azul6']
            bg_btn_whatsapp = colores['cinza2']
            # Bordas
            border = borders['cinza_red']
            border_btn_whatsapp = borders['sem_borda']
            img_border = '10px','10px','10px'
            font_size = ['18px','20px']
            # Decorador de Desconto
            decor_descont = '↓'
    if campanha == 'gamer':
            bg_tabela = colores['sem_cor']
            bg_produto = colores['branco']  
            bg_txt = colores['azul_esc_copo']
            bt_texto_cor = colores['preto']
            bordas = 'none','10px','15px'
            bg_txt = colores['azul_esc_copo']      
            bg_preço = colores['cinza']       
            bg_oferta = colores['azul_esc_copo']        
            bg_botao = colores['azul7']         
            bt_texto_cor = colores['branco'] 
            bg_tag_txt_desc = colores['branco']
            bg_tag_desc = colores['azul7']
            bg_btn_whatsapp = colores['rosa2']
            # Bordas
            border = borders['cinza_red']
            border_btn_whatsapp = borders['sem_borda']
            img_border = '10px','10px','10px'
            font_size = ['18px','20px']
            # Decorador de Desconto
            decor_descont = '↓'

    if campanha == 'verde':
        bg_tabela = colores['sem_cor']
        bg_produto = colores['branco']  
        bg_txt = colores['branco']
        bg_botao = colores['amarelo']  
        bt_texto_cor = colores['verde_escuro']
        bordas = 'none','10px','15px'
        bg_txt = colores['verde_escuro']      
        bg_preço = colores['cinza2']       
        bg_oferta = colores['verde_escuro']        
        bg_botao = colores['verde_escuro']         
        bt_texto_cor = colores['branco'] 
        bg_tag_txt_desc = colores['branco']
        bg_tag_desc = colores['verde_escuro']
        bg_btn_whatsapp = colores['cinza2']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['sem_borda']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓' 

    if campanha == 'amarelo':
        bg_tabela = colores['sem_cor']
        bg_produto = colores['branco']  
        bg_txt = colores['branco']
        bg_botao = colores['amarelo']  
        bt_texto_cor = colores['preto']
        bordas = 'none','10px','15px'
        bg_txt = colores['preto']      
        bg_preço = colores['amarelo']       
        bg_oferta = colores['preto']        
        bg_botao = colores['vermelho1']         
        bt_texto_cor = colores['branco'] 
        bg_tag_txt_desc = colores['preto']
        bg_tag_desc = colores['amarelo']
        bg_btn_whatsapp = colores['amarelo']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['branco']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓'  

    if campanha == 'vermelho':
        bg_tabela = colores['sem_cor']
        bg_produto = colores['branco']  
        bg_txt = colores['cinza']
        bg_botao = colores['amarelo']  
        bt_texto_cor = colores['verde_escuro']
        bordas = 'none','10px','15px'      
        bg_preço = colores['vermelho2']       
        bg_oferta = colores['cinza']        
        bg_botao = colores['vermelho4']         
        bt_texto_cor = colores['branco'] 
        bg_tag_txt_desc = colores['branco']
        bg_tag_desc = colores['vermelho4']
        bg_btn_whatsapp = colores['cinza2']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['sem_borda']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓'   

    if campanha == 'fds':
        bg_tabela = colores['laranja']
        bg_produto = colores['branco']  
        bg_txt = colores['vermelho1']
        bg_botao = colores['amarelo']  
        bt_texto_cor = colores['branco']
        bordas = 'none','10px','15px'   
        bg_preço = colores['cinza']       
        bg_oferta = colores['vermelho1']        
        bg_botao = colores['vermelho1']         
        bt_texto_cor = colores['branco'] 
        bg_tag_txt_desc = colores['branco']
        bg_tag_desc = colores['vermelho1']
        bg_btn_whatsapp = colores['cinza2']
        # Bordas
        border = borders['sem_borda']
        border_btn_whatsapp = borders['sem_borda']
        img_border = '10px','10px','10px'
        font_size = ['18px','20px']
        # Decorador de Desconto
        decor_descont = '↓'   
else:
    bg_tabela = colores['sem_cor']
    bg_produto = colores['branco']  
    bordas = 'none','10px','15px'
    bg_txt = colores['preto']      
    bg_preço = colores['cinza']       
    bg_oferta = colores['preto']        
    bg_botao = colores['azul2']         
    bt_texto_cor = colores['branco'] 
    bg_tag_txt_desc = colores['branco']
    bg_tag_desc = colores['azul2']
    # Bordas
    img_border = '10px','10px','10px'
    font_size = ['18px','20px']
    # Decorador de Desconto
    decor_descont = '↓'


# Estilos para os PRODUTOS definido para o COPO FÁCIL
campanha_cp = 'copo' #consumidor, none, ruvolo, copo
if url_produto[0][11:15] =='.ruv':
    bg_tabela = colores['azul_esc_copo']
    bg_produto = colores['azul_esc_copo']
    bordas = 'none','10px','15px'
    bg_txt = colores['branco'] 
    bg_preço = colores['azul_claro']       
    bg_oferta = colores['branco']
    bg_botao = colores['tiff']
    bg_tag_desc = colores['sem_cor']
    bg_tag_txt_desc = colores['branco']
    bt_texto_cor = colores['azul_esc_copo']
    bg_btn_whatsapp = colores['cinza2']
    # Bordas
    border = borders['branco']
    border_btn_whatsapp = borders['branco_fino']
    img_border = '10px','10px','10px'
    font_size = ['18px','20px']
    decor_descont = '-'


# Estilos para os PRODUTOS definido para o RUVOLO LOJA
campanha_rvl = 'ruvolo'

if url_produto[0][11:15] == 'a.ru': 
    bg_tabela = colores['sem_cor']
    bg_produto = colores['branco']
    bordas = 'none','10px','15px'
    bg_txt = colores['azul_esc_copo'] 
    bg_preço = colores['preto_op2']       
    bg_oferta = colores['tiff']
    bg_botao = colores['azul_ruvolo']
    bg_tag_desc = colores['tiff']
    bg_tag_txt_desc = colores['branco']
    bt_texto_cor = colores['branco']
    bg_btn_whatsapp = colores['sem_cor']
    # Bordas
    border = borders['sem_borda']
    border_btn_whatsapp = borders['branco_fino']
    img_border = '10px','10px','10px'
    font_size = ['18px','20px']
    # Decorador de Desconto
    decor_descont = '↓'




# Decorador de Descontos Altos
if desconto[0] > 35:
    decor_descont = '🔥'
if desconto[1] > 35:
    decor_descont = '🔥'
if desconto[2] > 35:
    decor_descont = '🔥'
if desconto[3] > 35:
    decor_descont = '🔥'

# Estilos para Botão de Desconto
estilos = [
           f"background-color: red;font-size: 16px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;border:{border};border-radius: 5px;padding: 2px 8px;display: none;",
           f"background-color: {bg_tag_desc};color:{bg_tag_txt_desc};font-size: 16px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;font-weight: bolder;border:{border};border-radius: 5px;padding: 2px 8px;",
           f"background-color: {bg_tag_desc};color:{bg_tag_txt_desc};font-weight: bolder;font-size: 16px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;border:{border};border-radius: 5px;padding: 2px 8px;",
           f"background-color: {bg_tag_desc};color:{bg_tag_txt_desc};font-size: 16px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;border:{border};border-radius: 5px;padding: 2px 8px;"
           ]



# Estilos para os Botões de descontos
sp0 = estilos[0]
sp1 = estilos[0] 
sp2 = estilos[0] 
sp3 = estilos[0]

# Ativar/Desativar botão de desconto    
if desconto[0] > base_desconto:
    sp0 = estilos[1]
if desconto[1] > base_desconto:
    sp1 = estilos[1]
if desconto[2] > base_desconto:
    sp2 = estilos[1]
if desconto[3] > base_desconto:
    sp3 = estilos[1]

# Estilo botão de desconto definido para o MEUCOPO
if url_produto[0][11:15] == '.meu':
    if desconto[0] > base_desconto:
        sp0 = estilos[2]
    if desconto[1] > base_desconto:
        sp1 = estilos[2]
    if desconto[2] > base_desconto:
        sp2 = estilos[2]
    if desconto[3] > base_desconto:
        sp3 = estilos[2]

# Estilo botão de desconto definido para COPOFÁCIL
if url_produto[0][11:15] =='.ruv':
    if desconto[0] > base_desconto:
        sp0 = estilos[3]
    if desconto[1] > base_desconto:
        sp1 = estilos[3]
    if desconto[2] > base_desconto:
        sp2 = estilos[3]
    if desconto[3] > base_desconto:
        sp3 = estilos[3]




# Ativa/Desativa o "conjunto unitário" aos Preços de Oferta do COPOFÁCIL
conjunto = ["","/un"]
quantitario = conjunto[1]

if url_produto[0][11:15] =='.ruv':
    quantitario = conjunto[1]
else:
    quantitario = conjunto[0]



# Controle dos Botões "COMPRAR"
botao = ''
bt_texto = ''

texto_botao = 'eu quero','comprar', 'confira' # itens aqui

# Meu copo
botao_produto1 = f'''
            text-decoration:none;
            margin: 12px;
            font-weight: bolder;
            font-size: 16px;
            font-family: Arial, Helvetica, sans-serif;
            text-transform: uppercase;
            background-color: {bg_botao};
            border-radius: 3px;
            padding: 8px 30px;
            color: {bt_texto_cor};
'''
# Copo Fácil
botao_produto2 = f'''
            text-decoration:none;
            margin: 12px;
            font-size: 16px;
            font-weight: bolder;
            font-family: Arial, Helvetica, sans-serif;
            text-transform: uppercase;
            background-color:{bg_botao};
            border-radius: 5px;
            padding: 8px 30px;
            color: {bt_texto_cor};
'''
#Ruvolo
botao_produto3 = f'''
            text-decoration:none;
            margin: 12px;
            font-size: 16px;
            font-weight: bolder;
            font-family: Arial, Helvetica, sans-serif;
            text-transform: uppercase;
            background-color:{bg_botao};
            border-radius: 5px;
            padding: 8px 30px;
            color: {bt_texto_cor};
'''
bt_whatsapp = f'''
            <!-- BOTÃO DE COMPARTILHAR DO WHASTAPP -->    
        <tr style="text-align: center";>
            <td style="padding-top: 7px;">        
                <a href="https://api.whatsapp.com/send?&text={url_produto[0].replace("http:","https:")}" target="_blank" rel="noopener noreferrer"
                style="background-color: {bg_btn_whatsapp};
                border:{border_btn_whatsapp};
                border-radius: 5px;
                color: white;
                font-size: 12px;
                text-align: center;
                text-decoration: none;
                text-transform: uppercase;
                padding: 5px 10px;
                "><img src="https://d335luupugsy2.cloudfront.net/cms/files/68653/1708634017/$rh70gruwjfc" alt="compartilhar whatsapp" srcset="" style="width: 20px; vertical-align: middle;"> compartilhe</a>
            </td>
            <td></td>
            <td style="padding-top: 7px;">        
                <a href="https://api.whatsapp.com/send?&text={url_produto[1].replace("http:","https:")}" target="_blank" rel="noopener noreferrer"
                style="background-color: {bg_btn_whatsapp};
                border:{border_btn_whatsapp};
                border-radius: 5px;
                color: white;
                font-size: 12px;
                text-align: center;
                text-decoration: none;
                text-transform: uppercase;
                padding: 5px 10px;
                "><img src="https://d335luupugsy2.cloudfront.net/cms/files/68653/1708634017/$rh70gruwjfc" alt="compartilhar whatsapp" srcset="" style="width: 20px; vertical-align: middle;"> compartilhe</a>
            </td>
            <td></td>
            <td style="padding-top: 7px;">        
                <a href="https://api.whatsapp.com/send?&text={url_produto[2].replace("http:","https:")}" target="_blank" rel="noopener noreferrer"
                style="background-color: {bg_btn_whatsapp};
                border:{border_btn_whatsapp};
                border-radius: 5px;
                color: white;
                font-size: 12px;
                text-align: center;
                text-decoration: none;
                text-transform: uppercase;
                padding: 5px 10px;
                "><img src="https://d335luupugsy2.cloudfront.net/cms/files/68653/1708634017/$rh70gruwjfc" alt="compartilhar whatsapp" srcset="" style="width: 20px; vertical-align: middle;"> compartilhe</a>
            </td>
        </tr>
            <!-- BOTÃO DE COMPARTILHAR DO WHASTAPP --> 


'''

# modifica o texto e propriedades de cor do botão de compra de acordo com o url/site
if url_produto[0][11:15] == '.meu':
    bt_texto = texto_botao[0]
    botao = botao_produto1
elif url_produto[0][11:15] == 'a.ru':
    bt_texto = texto_botao[1]
    botao = botao_produto3
elif url_produto[0][11:15] =='.ruv':
    bt_texto = texto_botao[1]
    botao = botao_produto2
else:
    bt_texto = texto_botao[2]
    botao = botao_produto1

# print("Este é o site:", end='')
# print(url_produto[0][11:15])




header = f'''
<table style="height: 255px; 
margin-left: auto; 
border-collapse: collapse;
font-family: 'Arial Narrow', Arial, sans-serif;
background-color: {bg_tabela};
margin-right: auto;"
 width="100%">
    <tbody>
   
    <!-- TABELA DE PRODUTOS -->

'''

header_2 = f'''
<table style="height: 255px; 
margin-left: auto; 
border-collapse: collapse;
font-family: 'Arial Narrow', Arial, sans-serif;
background-color: {bg_tabela};
margin-right: auto;"
 width="90%">
    <tbody>
    <tr style="height: 0px;">
    <tr style="height: 26px;">
    
    <!-- TEXTO CHAMADA SOBRE PRODUTOS 
    <td style="width: 209.641px; 
    text-align: center;
    font-weight: none;
    padding: 5px 100x;
    color: black;
    height: 60px;" colspan="5">
    <p style="
    font-family:Arial, Helvetica, sans-serif, Courier, monospace;
    font-size: 1.1em;
    background-color: none;
    border: 1px solid black;
    padding: 20px; 
    text-transform: uppercase;">
        
         
    </p></td> -->
    <!-- TEXTO PARA DESCONTO 
    <tr >
        <td style="height: 26px;
        color: black; 
        width: 209.641px; 
        text-transform: uppercase;
        text-align: center; 
        height: 60px;" colspan="5">
            <p style="
            font-size: 20px;
            font-family: 'Courier New', Courier, monospace;
            padding: 20px;
            border: none;
            ">

               aproveite opções especiais de frete**

            </p>
        </td>
    </tr>
    <!-- TABELA DE PRODUTOS -->

'''

footer = f'''
    </tbody>
</table>


'''



#2 produtos
#tabela com preços e oferta
tabela2_preco_oferta = f'''
        
    <!-- VALOR DE DESCONTO1 -->
    <tr style="height: 30px;text-align: right;">
    <td style="
    color: white;
    padding-right: 4px; 
    width: 32%;"><span style="{sp0}">
        {decor_descont}{desconto[0]}%
    </span>   
    </td>
    
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="
    color: white;
    padding-right: 4px;
    width: 32%; "><span style="{sp1}">
        {decor_descont}{desconto[1]}%
    </span> 
    </td>
    <!-- VALOR DE DESCONTO1 -->
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="200" height="200" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}
        
        " alt="" width="200" height="200" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL  1 -->
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p1_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p2_o.replace('.',',')}{quantitario}
    </span></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color:{bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>
<tr>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>

</tr>

'''

#tabela sem preços e oferta
tabela2_sem_preco_oferta = f'''
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}
        
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL 
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p1_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p2_o.replace('.',',')}{quantitario}
    </span></td> -->
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color:white; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>
       
'''

#tabela sem preços e oferta
tabela2_preco = f'''
<!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}
        
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL 
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>-->
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p1_p.replace('.',',')}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p2_p.replace('.',',')}
    </span></td> 
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color:white; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>

'''

#3 produtos
#tabela com preços e oferta
tabela3_preco_oferta = f'''
    
    <!-- VALOR DE DESCONTO -->
    <tr style="height: 30px;text-align: right;">
    <td style="
    color: white;
    padding-right: 4px; 
    width: 32%;"><span style="{sp0}">
        {decor_descont}{desconto[0]}%
    </span>   
    </td>
    
    <td style="width: 209.641px;"> </td>
    <td style="
    color: white;
    padding-right: 4px;
    width: 32%; "><span style="{sp1}">
        {decor_descont}{desconto[1]}%
    </span> 
    </td>
    <td style="width: 209.641px;"> </td>
    <td style="
    color: white;
    padding-right: 4px;
    width: 32%;"><span style="{sp2}">
        {decor_descont}{desconto[2]}%
    </span> 
    </td>
    </tr>

    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[2].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[2]}
        
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};
    letter-spacing: 2px;
    font-size: 1em;
    line-height: 110%; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};
    letter-spacing: 2px;
    font-size: 1em;
    line-height: 110%;   
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};
    letter-spacing: 2px;
    font-size: 1em;
    line-height: 110%;   
    text-align: center; 
    height: 44px;">
        {nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL  1 -->
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p3_p.replace('.',',')}
    </s></td>
    <!-- PREÇO PROMOCIONAL 2 -->
    <!-- PREÇO REAL 1 -->
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p1_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p2_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p3_o.replace('.',',')}{quantitario}
    </span></td>
    <!-- PREÇO REAL 2 -->
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        " target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        " target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[2].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>
  
'''
#tabela sem preços e oferta
tabela3_sem_preco_oferta = f'''
</tr>
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[2].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[2]}
        
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL 1
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p3_p.replace('.',',')}
    </s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p1_p.replace('.',',')}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p2_p.replace('.',',')}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p3_p.replace('.',',')}
    </span></td>
    -->
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[2].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>

'''
#tabela sem preços e oferta
tabela3_preco = f'''
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}

        
        " alt="" width="170" height="170" border="0px" /></a></td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 32%; 
    height: 170px;"><a href="

        {url_produto[2].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[2]}
        
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL 1
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p3_p.replace('.',',')}
    </s></td>
    -->
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p1_p.replace('.',',')}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p2_p.replace('.',',')}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        R${p3_p.replace('.',',')}
    </span></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[2].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>

'''

#4 produtos
#tabela com preços e oferta
tabela4_preco_oferta = f'''
        
    <!-- VALOR DE DESCONTO1 -->
    <tr style="height: 30px;text-align: right;">
    <td style="
    color: white;
    padding-right: 4px; 
    width: 32%;"><span style="{sp0}">
        {decor_descont}{desconto[0]}%
    </span>   
    </td>
    
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="
    color: white;
    padding-right: 4px;
    width: 32%; "><span style="{sp1}">
        {decor_descont}{desconto[1]}%
    </span> 
    </td>
    <!-- VALOR DE DESCONTO1 -->
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #1 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[0].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[0]}

        
        " alt="" width="200" height="200" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
        <!--PRODUTO #3 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[1].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[1]}
        
        " alt="" width="200" height="200" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL  1 -->
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p1_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p2_p.replace('.',',')}
    </s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p1_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p2_o.replace('.',',')}{quantitario}
    </span></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color:{bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[0].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[1].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>
<tr>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>

</tr>

<!-- LINHA 2 DE PRODUTOS -->

        
    <!-- VALOR DE DESCONTO1 -->
    <tr style="height: 30px;text-align: right;">
    <td style="
    color: white;
    padding-right: 4px; 
    width: 32%;"><span style="{sp0}">
        {decor_descont}{desconto[0]}%
    </span>   
    </td>
    
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="width: 209.641px;"> </td>
    <td style="
    color: white;
    padding-right: 4px;
    width: 32%; "><span style="{sp1}">
        {decor_descont}{desconto[1]}%
    </span> 
    </td>
    <!-- VALOR DE DESCONTO1 -->
    <!--PRODUTOS -->
    <tr style="height: 180px;">
        <!--PRODUTO #3 -->
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[2].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[2]}

        
        " alt="" width="200" height="200" border="0px" /></a></td>
        <!--PRODUTO #2 -->
    <td style="width: 209.641px; text-align: center; vertical-align: middle; height: 170px;" scope="col"><span style="color: #ffffff; font-size: 24px;"></span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
        <!--PRODUTO #4 -->
    <td style="width: 209.641px; height: 170px;"><span style="color: #ffffff; font-size: 20px;"></span></td>
    <td style="
    background-color: {bg_produto};
    border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]};
    width: 45%; 
    height: 170px;"><a href="

        {url_produto[3].replace("http:","https:")}
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src=
        "
        {img_produto[3]}
        
        " alt="" width="200" height="200" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto}; 
    text-align: center; 
    height: 44px;">
        {nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; text-align: center; height: 44px;"> </td>
    <td style="
    
    width: 209.641px;
    padding: 10px;
    color: {bg_txt};
    background-color: {bg_produto};  
    text-align: center; 
    height: 44px;">
        {nome_produto[3].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}

    </td>
    </tr>
    <!-- PREÇO PROMOCIONAL  1 -->
   
    <tr style="height: 22px;">
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p3_p.replace('.',',')}
    </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="
                width: 209.641px;
        color: {bg_preço};
        font-size: {font_size[0]};
        background-color: {bg_produto};  
        text-align: center; 
        height: 22px;">de <s>R$
        {p4_p.replace('.',',')}
    </s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="
    width: 209.641px; 
    text-align: center; 
    height: 10px;
    background-color: {bg_produto}; 
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p3_o.replace('.',',')}{quantitario}
    </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="
    width: 209.641px; 
    text-align: center;
    background-color: {bg_produto};  
    height: 10px;
    "><span style="font-size: 20px; 
    margin: auto;
    font-family: 'arial black', sans-serif;color:{bg_oferta}">
        por R${p4_o.replace('.',',')}{quantitario}
    </span></td>
    </tr>
    <tr style="height: 44px;">
    <td style="
    background-color:{bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[2].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a>
    
    
    </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 35px;"> </td>
    <td style="
    background-color: {bg_produto}; 
    border-bottom-left-radius: {bordas[1]};
    border-bottom-right-radius: {bordas[1]};
    width: 209.641px; 
    text-align: center; 
    height: 24px;">
        <a href="
        
        {url_produto[3].replace("http:","https:")}

        "; target="_blank" rel="noopener" 
        style="{botao}">
        {bt_texto}
        </a></td>
<tr>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>

</tr>

'''


tabela4_sem_preco_oferta = f'''
    
    <tr style="height: 180px;"><!--PRODUTO #1 -->
    <td style="background-color: {bg_produto}; border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]}; border-right: 1px solid #c2c2c2; h: 40%; height: 170px;"><a href="
        {url_produto[0].replace('http:','https:')} 
        
        " target="_blank" rel="noopener"> <img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
        {img_produto[0]}
        " alt="" width="170" height="170" border="0px" /> </a></td>
    <!--PRODUTO #2 -->
    <td style="width: 209.641px; 
    text-align: center; vertical-align: middle; height: 170px;" scope="col"> </td>
    <!--PRODUTO #3 -->
    <td style="background-color: {bg_produto}; border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]}; border-right: 1px solid #c2c2c2; h: 40%; height: 170px;"><a href="
        {url_produto[1].replace('http:','https:')} 
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
        {img_produto[1]}
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; background-color: {bg_produto}; 
    text-align: center; height: 44px;">{nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    <td style="width: 209.641px; 
    text-align: center; height: 44px;"> </td>
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; background-color: {bg_produto}; 
    text-align: center; height: 44px;">{nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    </tr>
    <!-- PREÇO PROMOCIONAL
    <tr style="height: 22px;">
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; color: {bg_preço}; font-size: {font_size[0]}; background-color: {bg_produto}; 
    text-align: center; height: 22px;">de <s> R${p1_p.replace('.',',')} </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; color: {bg_preço}; font-size: {font_size[0]}; background-color: {bg_produto}; 
    text-align: center; height: 22px;">de <s> R${p2_p.replace('.',',')}</s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="width: 209.641px; 
    text-align: center; height: 10px; background-color: {bg_produto}; border-right: 1px solid #c2c2c2; an style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}"> por R${p1_o.replace('.',',')}{quantitario} </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; 
    text-align: center; background-color: {bg_produto}; height: 10px; border-right: 1px solid #c2c2c2; an style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}">por R${p2_o.replace('.',',')}{quantitario}</span></td>
    -->  
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[0].replace('http:','https:')} 
    
   " target="_blank" rel="noopener"> {bt_texto} </a></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[1].replace('http:','https:')} 
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    </tr>
    
    <tr style="height: 44px;">
    <td style="background-color: none; border-right: none; border-left: none; border-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: none; border-right: none; border-left: none; border-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"> </td>
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><a href="
    {url_produto[2].replace('http:','https:')} 
    
    " target="_blank" rel="noopener"> <img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
    {img_produto[2]}" alt
    ="" width="170" height="170" border="0px" /> </a></td>
    <td style="width: 209.641px; height: 170px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><a href="
    {nome_produto[3].replace('http:','https:')} 
    
    " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
    {img_produto[3]}" alt
    ="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">{nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">{nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    </tr>
    <!-- PREÇO PROMOCIONAL
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">de <s> R${p3_p.replace('.',',')} </s></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">de <s> R${p4_p.replace('.',',')}</s></td>
    
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><span style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}"> por R${p3_o.replace('.',',')}{quantitario} </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><span style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}">por R${p4_o.replace('.',',')}{quantitario}</span></td>
    -->
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[2].replace('http:','https:')} 
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {nome_produto[3].replace('http:','https:')}  
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    </tr>
     
'''

tabela4_preco = f'''
    
    <tr style="height: 180px;"><!--PRODUTO #1 -->
    <td style="background-color: {bg_produto}; border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]}; border-right: 1px solid #c2c2c2; h: 40%; height: 170px;"><a href="
        {url_produto[0].replace('http:','https:')} 
        
        " target="_blank" rel="noopener"> <img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
        {img_produto[0]}
        " alt="" width="170" height="170" border="0px" /> </a></td>
    <!--PRODUTO #2 -->
    <td style="width: 209.641px; 
    text-align: center; vertical-align: middle; height: 170px;" scope="col"> </td>
    <!--PRODUTO #3 -->
    <td style="background-color: {bg_produto}; border-top-right-radius: {bordas[1]};
    border-top-left-radius: {bordas[1]}; border-right: 1px solid #c2c2c2; h: 40%; height: 170px;"><a href="
        {url_produto[1].replace('http:','https:')} 
        
        " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
        {img_produto[1]}
        " alt="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; background-color: {bg_produto}; 
    text-align: center; height: 44px;">{nome_produto[0].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    <td style="width: 209.641px; 
    text-align: center; height: 44px;"> </td>
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; background-color: {bg_produto}; 
    text-align: center; height: 44px;">{nome_produto[1].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    </tr>
    <!-- PREÇO PROMOCIONAL
    <tr style="height: 22px;">
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; color: {bg_preço}; font-size: {font_size[0]}; background-color: {bg_produto}; 
    text-align: center; height: 22px;">de <s> R${p1_p.replace('.',',')} </s></td>
    <td style="width: 209.641px; height: 22px;"> </td>
    <td style="border-right: 1px solid #c2c2c2; h: 209.641px; color: {bg_preço}; font-size: {font_size[0]}; background-color: {bg_produto}; 
    text-align: center; height: 22px;">de <s> R${p2_p.replace('.',',')}</s></td>
    --> 
    </tr>
    <tr style="height: 44px;">
    <td style="width: 209.641px; 
    text-align: center; height: 10px; background-color: {bg_produto}; border-right: 1px solid #c2c2c2; an style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}">  R${p1_p.replace('.',',')} </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="width: 209.641px; 
    text-align: center; background-color: {bg_produto}; height: 10px; border-right: 1px solid #c2c2c2; an style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}"> R${p2_p.replace('.',',')}</span></td>
     
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[0].replace('http:','https:')} 
    
   " target="_blank" rel="noopener"> {bt_texto} </a></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[1].replace('http:','https:')} 
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    </tr>
    
    <tr style="height: 44px;">
    <td style="background-color: none; border-right: none; border-left: none; border-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"> </td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: none; border-right: none; border-left: none; border-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"> </td>
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><a href="
    {url_produto[2].replace('http:','https:')} 
    
    " target="_blank" rel="noopener"> <img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
    {img_produto[2]}" alt
    ="" width="170" height="170" border="0px" /> </a></td>
    <td style="width: 209.641px; height: 170px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><a href="
    {nome_produto[3].replace('http:','https:')} 
    
    " target="_blank" rel="noopener"><img style="border: 0px; display: block;border-radius:{img_border[1]} ;margin-left: auto; margin-right: auto;" src="
    {img_produto[3]}" alt
    ="" width="170" height="170" border="0px" /></a></td>
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">{nome_produto[2].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">{nome_produto[3].replace('REF','Ref').replace('Ref.','Ref.:').replace('Ref.:','<br>Ref.:').replace('peças','Pcs').replace('Peças',' Pcs').replace('pçs','Pcs').replace('4Pcs','4 Pcs').replace('4 Pcs','<br>4 Pcs').replace('pçs','Pcs').replace('2Pcs','2 Pcs').replace('2 Pcs','<br>2 Pcs').replace('6Pcs','6 Pcs').replace('6 Pcs','<br>6 Pcs').replace('|',' ').replace('CAIXA COM','<br>CAIXA COM').title().replace('De ', 'de ').replace('Do ','do ').replace('Para ', 'para ').replace('E ', 'e ').replace('Com ', 'com ').replace('Em ', 'em ')}</td>
    </tr>
    <!-- PREÇO PROMOCIONAL
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">de <s> R${p3_p.replace('.',',')} </s></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;">de <s> R${p4_p.replace('.',',')}</s></td>
    --> 
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><span style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}">  R${p3_p.replace('.',',')} </span></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: none; width: 209.641px; 
    text-align: center; height: 24px;"><span style="font-size: 20px; margin: auto; font-family: 'arial black', sans-serif;color:{bg_oferta}"> R${p4_p.replace('.',',')}</span></td>
    </tr>
    <tr style="height: 44px;">
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {url_produto[2].replace('http:','https:')} 
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    <td style="width: 209.641px; height: 24px;"> </td>
    <td style="background-color: {bg_produto}; border-right: 1px solid #c2c2c2; er-bottom: 1px solid #c2c2c2; width: 209.641px; 
    text-align: center; height: 24px;"><a style="{botao}" href="
    
    
    {nome_produto[3].replace('http:','https:')}  
    
    " target="_blank" rel="noopener">{bt_texto}</a></td>
    </tr>
     
'''




# Montagem do HTML
# Para 2 Produtos
with codecs.open('temp_base2.html','w', 'utf-8') as f:
    f.write(header_2)
    if (preco_produto[0] == 0.0 and oferta_produto[0] == 0.0): 
        f.write(tabela2_sem_preco_oferta) #sem preço e oferta 1 e 2
    elif oferta_produto[0] == 0.0: 
        f.write(tabela2_preco) #não tem oferta 2
    else:
        f.write(tabela2_preco_oferta)
    f.write(footer)


# Para 3 Produtos
with codecs.open('temp_base3.html','w', 'utf-8') as f:
    f.write(header)
    if (preco_produto[0] == 0.0 and  oferta_produto[0] == 0.0):#sem preço e oferta 1 e 2 ajustar para "== 0.0" default mode
        f.write(tabela3_sem_preco_oferta)
    elif oferta_produto[0] == 0.0: #não tem oferta 2
        f.write(tabela3_preco)
    else:
        f.write(tabela3_preco_oferta)
    if url_produto[0][11:15] == '.meu':
        f.write(bt_whatsapp)
    f.write(footer)
        
# Para 4 Produtos
with codecs.open('temp_base4.html','w', 'utf-8') as f:
 f.write(header_2)
 if (preco_produto[0] == 0.0 and  oferta_produto[0] == 0.0): #sem preço e oferta 1 e 2
     f.write(tabela4_sem_preco_oferta)
 elif oferta_produto[0] == 0.0: #não tem oferta 2
     f.write(tabela4_preco)
 else:
     f.write(tabela4_preco_oferta)
 f.write(footer)
