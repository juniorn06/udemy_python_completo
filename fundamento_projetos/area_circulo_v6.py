#!/usr/bin/python3
#import math
from math import pi


def circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do circulo:', area)
