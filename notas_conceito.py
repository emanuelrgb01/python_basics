#! python
def conceito(nota):
    if nota > 10 or nota < 0:
        return 'inválido'
    elif nota >= 9.5:
        return 'L'
    elif nota >= 8.5:
        return 'MB'
    elif nota >= 7.5:
        return 'B'
    elif nota >= 6.5:
        return 'R'
    elif nota >= 5.0:
        return 'D'
    else:
        return 'I'


if __name__ == '__main__':
    nota = input('Insira a nota-de-disciplina: ')
    nota = float(nota)
    conceito_nota = conceito(nota)
    print(f'Seu conceito foi {conceito_nota}')
