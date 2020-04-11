import time
import sys
from enum import IntEnum
import math

def prostokat(a, b):
    return a * b

def trojkat(a, h):
    return a * h / 2

def kolo(r):
    return math.pi * r ** 2

def trapez (a, b, h):
    return (a + b) * h / 2

def deltoid (d1, d2):
    return d1 * d2 / 2

def sumuj_do(b):
        suma = 0
        lista = range(1, b + 1)
        for liczby in lista:
                liczba = liczby
                suma = suma + liczba
        nazwa = "Sumowanie pętli:"
        return nazwa, suma

def sumuj_do2(b):
        suma = sum(liczby 
                for liczby in range(1, b + 1)
                )
        nazwa = "Sumowanie z generatora:"
        return nazwa, suma

def sumuj_do3(b):
        lista2 = range(1, b + 1)
        suma = sum(lista2)
        nazwa = "Sumowanie listy:"
        return nazwa, suma

def sumuj_do4(b):
        suma = (1 + b) / 2 * b
        nazwa = "Sumowanie wzoru arytm.:"
        return nazwa, suma

def sumuj_do5(b):
        lista = [liczby 
                for liczby in range(1, b + 1)
                ]
        suma = sum(lista)
        nazwa = "Sumowanie listy z pętli.:"
        return nazwa, suma

def wydajnosc(func, b, ilosc_razy):
        start = time.perf_counter()
        for _ in range(0, ilosc_razy):
            print(func(b))
        end = time.perf_counter()
        return end - start