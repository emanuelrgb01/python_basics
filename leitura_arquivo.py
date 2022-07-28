#! python
try:
    arquivo = open('alunos.csv')

    for line in arquivo:
        print('Nome do aluno: {},  Idade: {}'.format(*line.strip().split(',')))
finally:
    arquivo.close()
