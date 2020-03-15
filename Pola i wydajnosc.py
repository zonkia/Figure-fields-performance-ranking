import definicje
import time
import sys
from enum import IntEnum
import math

def sumuj_do(b):
        suma = 0
        lista = range(1, b + 1)
        for liczby in lista:
                liczba = liczby
                suma = suma + liczba
        nazwa = "Sumowanie pętli:"
        return nazwa, suma

Menu_figury = IntEnum("Menu_figury", "PROSTOKĄT KOŁO TRÓJKĄT RÓWNOLEGŁOBOK TRAPEZ DELTOID SUMOWANIE")

print("Witaj w programie liczącym powierzchnie figur oraz sumującym wszystkie liczby od 1 do \"n\"")

while True:
    try:
        wybor = int(input("""Podaj jakiej figury powierzchnię chcesz policzyć lub wpisz \"7\" jeśli chcesz sprawdzić wydajność metod dodawania liczb od 1 do \"n\": 
1. PROSTOKĄT
2. KOŁO
3. TRÓJKĄT
4. RÓWNOLEGŁOBOK
5. TRAPEZ
6. DELTOID
7. Jeśli chcesz zsumować liczby od 1 do \"n\" i otrzymać ranking wydajności metod otrzymania wyniku
""").upper())
        if (wybor == 1) or (wybor == 2) or (wybor == 3) or (wybor == 4) or (wybor == 5) or (wybor == 6) or (wybor == 7):
            if (wybor == Menu_figury.PROSTOKĄT):
                a = int(input("Podaj bok A: "))
                b = int(input("Podaj bok B: "))
                if a == b:
                    print("Pole kwadratu wynosi:", definicje.prostokat(a, b))
                    print()
                    time.sleep(2)
                else:
                    print("Pole prostokąta wynosi:", definicje.prostokat(a, b))
                    print()
                    time.sleep(2)

            elif (wybor == Menu_figury.KOŁO):
                r = int(input("Podaj promień koła: "))
                print("Pole koła wynosi:", round(definicje.kolo(r), 2))
                time.sleep(2)
                print()

            elif (wybor == Menu_figury.TRÓJKĄT):
                a = int(input("Podaj podstawę trójkąta: "))
                h = int(input("Podaj wysokość trójkąta: "))
                print("Pole trójkąta wynosi:",definicje.trojkat(a, h))
                time.sleep(2)
                print()

            elif (wybor == Menu_figury.RÓWNOLEGŁOBOK):
                a = int(input("Podaj podstawę równoległoboku: "))
                b = int(input("Podaj wysokość równoległoboku: "))
                print("Pole równoległoboku wynosi:", definicje.prostokat(a, b))
                time.sleep(2)
                print()

            elif (wybor == Menu_figury.TRAPEZ):
                a = int(input("Podaj dolny bok trapezu: "))
                b = int(input("Podaj górny bok trapezu: "))
                h = int(input("Podaj wysokość trapezu: "))
                print("Pole trapezu wynosi:", definicje.trapez(a, b, h))
                time.sleep(2)
                print()

            elif (wybor == Menu_figury.DELTOID):
                d1 = int(input("Podaj pierwszą przekątną deltoidu: "))
                d2 = int(input("Podaj drugą przekątną deltoidu: "))
                print("Pole deltoidu wynosi:", definicje.deltoid(d1, d2))
                time.sleep(2)
                print()
            
            elif (wybor == Menu_figury.SUMOWANIE):
                b = int(input("Podaj do której liczby zrobić sumowanie: "))
                print()

                slownik_wynikow = {}

                czas = definicje.wydajnosc(definicje.sumuj_do, b)
                print("Wydajność [s]:", czas)
                slownik_wynikow["Sumowanie pętli"] = czas
                print("Rozmiar funkcji:", sys.getsizeof(definicje.sumuj_do(b)))
                print()

                czas = definicje.wydajnosc(definicje.sumuj_do2, b)
                print("Wydajność [s]:", czas)
                slownik_wynikow["Suma z generatora"] = czas
                print("Rozmiar funkcji:", sys.getsizeof(definicje.sumuj_do2(b)))
                print()

                czas = definicje.wydajnosc(definicje.sumuj_do3, b)
                print("Wydajność [s]:", czas)
                slownik_wynikow["Sumowanie listy"] = czas
                print("Rozmiar funkcji:", sys.getsizeof(definicje.sumuj_do3(b)))
                print()

                czas = definicje.wydajnosc(definicje.sumuj_do4, b)
                print("Wydajność [s]:", czas)
                slownik_wynikow["Sumowanie wzoru arytm"] = czas
                print("Rozmiar funkcji:", sys.getsizeof(definicje.sumuj_do4(b)))
                print()

                czas = definicje.wydajnosc(definicje.sumuj_do5, b)
                print("Wydajność [s]:", czas)
                slownik_wynikow["Sumowanie listy z pętli"] = czas
                print("Rozmiar funkcji:", sys.getsizeof(definicje.sumuj_do5(b)))
                print()

                same_wydajnosci = []

                for rodzaje in slownik_wynikow:
                    same_wydajnosci.append(slownik_wynikow[rodzaje])
                najszybszy = min(same_wydajnosci)
                najwolniejszy = max(same_wydajnosci)

                for rodzaje in slownik_wynikow:
                    if slownik_wynikow[rodzaje] == najszybszy:
                        print("Najszybsza metoda to:", rodzaje, "z czasem [s]:", slownik_wynikow[rodzaje])
                for rodzaje in slownik_wynikow:
                    if slownik_wynikow[rodzaje] == najwolniejszy:
                        print("Najwolniejsza metoda to:", rodzaje, "z czasem [s]:", slownik_wynikow[rodzaje])

                print()
                x = 0
                for rodzaje in sorted(slownik_wynikow, key = slownik_wynikow.get):
                    x += 1
                    print(x, "miejsce zajęła metoda:", rodzaje, "z czasem [s]:",slownik_wynikow[rodzaje])
                time.sleep(2)
                print()
                continue

        else:
            print()
            print("Nie ma takiej figury. Spróbuj ponownie")
            print()
            continue

    except:
        print("Nieprawidłowa komenda. Spróbuj ponownie")
        time.sleep(2)
        print()
        continue