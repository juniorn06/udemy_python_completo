#!/usr/bin/python3
#import math
from math import pi
import sys


def circulo(raio):
    return pi * pow(float(raio), 2)


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do circulo:', area)
