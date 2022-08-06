#! python
import csv

with open('desafio-ibge.csv', encoding='latin1') as arquivo_dados:
    with open('ibge.txt', 'w') as saida:
        dados = arquivo_dados.read()
        for cidade in csv.reader(dados.splitlines()):
            print(f'9: {cidade[8]}, 4: {cidade[3]}', file=saida)
