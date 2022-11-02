from pyautogui import hotkey, press, write, click, PAUSE
from pyperclip import copy
from time import sleep
import pandas as pd

press('win')
sleep(1)
write('chrome')
sleep(1)
press('enter')
sleep(1)
copy('https://drive.google.com/drive/folders/1PRcY2w0cRwTe2iEoZ_kiBXzjEcTVwIvA?usp=sharing') # Colocar o link onde irá pegar os arquivos.
sleep(1)
hotkey('ctrl', 'v')
sleep(1)
press('enter')
sleep(5)
click(x=349, y=302, clicks=2)
sleep(3)
click(button='right', interval=1.5) 
click(x=532, y=776, clicks=1)
sleep(5)


dados = pd.read_excel(r'C:\Users\cicer\Downloads\Vendas - Dez.xlsx') # Local onde pegará o conteúdo dentro do arquivo baixado.
faturamento = dados['Valor Final'].sum() # Especificando a coluna dos valores finais e somando tudo com o sum().
quantidade = dados['Quantidade'].sum()  # O mesmo aqui.
sleep(1)
hotkey('ctrl', 't') 
sleep(1)
write('https://gmail.com/') # Irá abrir o gmail, óbvio.
press('enter')
sleep(4)
click(x=143, y=198, clicks=1)
sleep(1.5)
write('aqui') # colocar o e-mail para quem será enviado o texto.
sleep(1.5)
press('tab')
sleep(1.5)
press('tab')
sleep(1.5)
write('Relatório de Vendas')
sleep(1.5)
press('tab')
sleep(1)
txt = f''' Olá, aqui está o resumo das vendas. 
 Faturamento: R${faturamento:,.2f}
 Quantidade de produtos vendidos: {quantidade:,}

 Rápido e prático.
    Automação na web com Python.
''' # Texto a ser enviado.
sleep(1)

copy(txt)
hotkey('ctrl', 'v')
sleep(1)
hotkey('ctrl', 'enter')
sleep(1)