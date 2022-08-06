#! python
import csv
try:
    arquivo = open('alunos.csv')

    for line in arquivo:
        print('1) Nome do aluno: {},  Idade: {}'.format(
            *line.strip().split(',')))
finally:
    arquivo.close()


with open('alunos.csv') as arquivo2:
    with open('pessoas.txt', 'w') as saida:
        for line in arquivo2:
            pessoa = line.strip().split(',')
            print('2) Nome do aluno: {},  Idade: {}'.format(
                *pessoa), file=saida)


with open('alunos.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('3) Nome do aluno: {},  Idade: {}'.format(*pessoa))
