# -*- coding: utf-8 -*-

import random

print("Wprowadź liczbę:")

liczba1 = int(input())
liczba2 = random.randint(0,100)
dzialanie = ["+","-","*","/"]


def typDzialania():
# losuje działanie z listy
    dzial = random.randint(0,len(dzialanie)-1)
    return dzial

def dodawanie():
# funkcja dodawania
    wynik = liczba1 + liczba2
    print(str(liczba1) + " + " + str(liczba2) + " = " + str(wynik))

def odejmowanie():
# funkcja odejmowania
    wynik = liczba1 - liczba2
    print(str(liczba1) + " - " + str(liczba2) + " = " + str(wynik))

def mnozenie():
# funkcja mnożenia
    wynik = liczba1 * liczba2
    print(str(liczba1) + " * " + str(liczba2) + " = " + str(wynik))

def dzielenie():
# funkcja dzielenia
    wynik = float(liczba1) / float(liczba2)
    print(str(liczba1) + " / " + str(liczba2) + " = " + str(wynik))


def wzor():
# funkcja wzoru, zależna od wylosowanego działania
    typ = typDzialania()
    if typ == 0:
        dodawanie()
    elif typ == 1:
        odejmowanie()
    elif typ == 2:
        mnozenie()
    elif typ == 3:
        dzielenie()
    else:
        "Error!"


wzor()