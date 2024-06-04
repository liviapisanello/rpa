import requests
from bs4 import BeautifulSoup #pacote para extrair dados HTML
import pyautogui
import time
import psycopg2

url = 'https://www.google.com/finance/quote/USD-BRL?sa=X&sqi=2&ved=2ahUKEwi3u-ayweyEAxXcLrkGHSLSAU0QmY0JegQIDhAv'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
valor_dolar_element = soup.find('div', class_='YMlKec fxKbKc')
valor_dolar = valor_dolar_element.text.strip()

data_hora_element = soup.find('div', class_='ygUjEc')
data_hora = data_hora_element.text.strip()

# colocar o valor do dolar no excel

# pyautogui.press('winleft')
# time.sleep(2)
# pyautogui.write('excel')
# time.sleep(2)
# pyautogui.press('enter')
# time.sleep(1)
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.write('exercicioanalisedados')
# time.sleep(2)
# pyautogui.press('enter')
# time.sleep(2)
# pyautogui.write(data_hora)
# pyautogui.press('tab')
# pyautogui.write(valor_dolar)
# pyautogui.press('enter')
# time.sleep(3)
# pyautogui.hotkey('alt', 'f4')


#colocar o valor do dolar no pgadmin

hostname = 'pg-3efc18e7-liviapisanello.e.aivencloud.com'
database = 'defaultdb'
username = 'avnadmin'
port = 11379
password = 'AVNS_srxRSEGf6st6cHH9DC1'

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    port=port,
    password=password
)
cursor = conn.cursor()

cursor.execute(f"CALL inserir_cotacao_dolar({valor_dolar})")
conn.commit()

cursor.close()
conn.close()
