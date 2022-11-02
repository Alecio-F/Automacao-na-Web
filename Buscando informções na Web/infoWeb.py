import imp
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()

navegador.get('https://www.google.com.br')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotação_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

navegador.get('https://www.google.com.br')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotação_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotação_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')

cotação_ouro = cotação_ouro.replace(',', '.')

navegador.quit

tabela = pd.read_excel('Produtos.xlsx')

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(cotação_dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(cotação_euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(cotação_ouro)

tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

tabela.to_excel('Produtos N.xlsx', index=False)