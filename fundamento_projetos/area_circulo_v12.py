#!/usr/bin/python3
# import math
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * pow(float(raio), 2)


def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        
        print(TerminalColor.ERRO +
              'O raio deve ser um valor numérico' +
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo:', area)
