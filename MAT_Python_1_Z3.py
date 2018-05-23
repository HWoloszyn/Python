# -*- coding: utf-8 -*-

name = str(input("Jak masz na imię? "))
lenName = len(name)
surname = str(input ("Jakie jest Twoje nazwisko? "))
lenSurname = len(surname)
if lenName == 0 and lenSurname == 0:
    print("Brak danych")
elif lenName == 0:
    print ("Nie wypełniono pola imię")
elif lenSurname == 0:
    print ("Nie wypełniono pola nazwisko")
else:
    print ("HELLO", name, surname)







