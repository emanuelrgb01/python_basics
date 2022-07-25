#! python
from math import pi
import sys
import errno

ERRO = '\033[91m'  # cor vermelha a ser adicionada no terminal
NORMAL = '\033[0m'  # retorna à cor normal do terminal


def help():
    print("Cuidado! É necessário informar o raio")
    print(f"Sintaxe: {sys.argv[0]} <raio>")


def circulo(raio):
    return pi * float(raio)**2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(ERRO + "O raio deve ser um número" + NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print(f"Área do círculo de raio {raio} é {area}")
