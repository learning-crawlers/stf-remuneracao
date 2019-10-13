#######################################
##  STF Remuneração 
##    Lista de remuneração de servidores ativos do stf com nome, cargo, fc/cj, bruto (R$), líquido (R$)
##
##    Author: Alex Benincasa Santos 
##    Mail: alexbenincasa@ymail.com
##    2019
#######################################

import os
import requests
from bs4 import BeautifulSoup

lista = []

# periodo=012019
# ano=2019
# mes=01
# folha=1 Tipo da folha 1=Normal
result = requests.get('http://www.stf.jus.br/portal/remuneracao/listarRemuneracao.asp?periodo=012019&ano=2019&mes=01&folha=1')

# BeautifulSoup faz o parser no result colocando as tags
soup = BeautifulSoup(result.text, features='html.parser')

for tr in soup.select('table#servidores_ativos tbody tr'):
    td = tr.findAll('td')
    nome = td[0].text
    cargo = td[1].text
    fc_cj = td[2].text
    bruto = td[3].text
    liquido = td[4].text

    lista.append({ 'nome': nome, 'cargo': cargo, 'fc_cj': fc_cj, 'bruto': bruto, 'liquido': liquido })

for servidor in lista:
    print(servidor)
