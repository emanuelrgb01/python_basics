#! python
try:
    arquivo = open('alunos.csv')

    for line in arquivo:
        print('Nome do aluno: {},  Idade: {}'.format(*line.strip().split(',')))
finally:
    arquivo.close()


with open('alunos.csv') as arquivo2:
    for line in arquivo2:
        print('Nome do aluno: {},  Idade: {}'.format(*line.strip().split(',')))
