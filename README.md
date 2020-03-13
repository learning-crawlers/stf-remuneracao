[![HitCount](http://hits.dwyl.com/learning-crawlers/stf-remuneracao.svg)](http://hits.dwyl.com/learning-crawlers/stf-remuneracao)

# STF Remuneração de Servidores

Extração de dados com Beautiful Soup para listar a remuneração de Servidores ativos do STF

## Instalação

```
pip install requests beautifulsoup4 
```

## Modo de usar

Procure o path do python instalado no Windows:

```
/mnt/c/Users/alexb/AppData/Local/Programs/Python/Python37-32/python.exe listar.py
```

## Resultado

**Header**

Nome, Cargo, FC/CJ, Bruto (R$), Líquido (R$)

**Dados**

```
{'nome': 'ADÃO PAULO MARTINS DE OLIVEIRA', 'cargo': '', 'fc_cj': 'CJ-3', 'bruto': '20.760,07', 'liquido': '17.484,25'}
{'nome': 'ADAUTO CIDREIRA NETO', 'cargo': 'ANALISTA JUDICIÁRIO', 'fc_cj': 'CJ-2', 'bruto': '41.171,06', 'liquido': '33.074,08'}
{'nome': 'ADISSON TAVEIRA ROCHA LEAL', 'cargo': '', 'fc_cj': 'CJ-3', 'bruto': '21.039,73', 'liquido': '17.377,71'}
{'nome': 'ADRIANA ARAGÃO CRAVEIRO LEITE', 'cargo': '', 'fc_cj': 'FC-06', 'bruto': '7.833,98', 'liquido': '5.355,26'}
{'nome': 'ADRIANA AUGUSTA DA SILVA LUCENA', 'cargo': 'ANALISTA JUDICIÁRIO', 'fc_cj': '', 'bruto': '30.499,11', 'liquido': '22.235,05'}
```