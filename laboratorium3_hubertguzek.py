# Zadanie 1
print("Zad. 1")

paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Pozostałe paliwo: {paliwo} litrów (Czas: {czas} s)")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1
print("Koniec lotu.")
print()

# Zadanie 2
print("Zad. 2")

licznik = 0
liczba = 2
liczby_pierwsze = []

while licznik < 10:
    for i in range(2, liczba):
        if liczba % i == 0:
            break
    else:
        liczby_pierwsze.append(str(liczba))
        licznik += 1
    liczba += 1

print(",".join(liczby_pierwsze))
print()

# Zadanie 3
print("Zad. 3")

ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]
numery = [1, 2, 3, 4, 5]
mieszkania = ["/1", "/2", "/3", "/4", "/5", "/6", "/7", "/8", "/9", "/10"]

for ulica in ulice:
    for numer in numery:
        for mieszkanie in mieszkania:
            print(f"Ulica {ulica} Numer {numer}{mieszkanie}")
print()

# Zadanie 5
print("Zad. 5")

liczba = 80
lista_liczb = []

while liczba >= 0:
    lista_liczb.append(liczba)
    liczba -= 4

print(lista_liczb)
print()

# Zadanie 6
print("Zad. 6")

while True:
    liczba = int(input("Podaj liczbę całkowitą: "))

    if liczba < 0:
        print("Wprowadzono liczbę ujemną. Koniec pętli!")
        break
print()

# Zadanie 8
print("Zad. 8")

tekst = "Python jest super"

print("Zerowy znak:", tekst[0])
print("Ostatni znak:", tekst[-1])
print("Co drugi, zaczynając od zerowego:", tekst[::2])
print("Co trzeci zaczynając od pierwszego:", tekst[1::3])
print("Od dziesiątego do ostatniego:", tekst[10:])
print("Od końca do początku:", tekst[::-1])
print()

# Zadanie 9
imie = input("Podaj imię: ")
print("Witaj", imie)
print()

wiek = input("Podaj wiek: ")
print("Twój wiek to:", wiek)
print()

imie2 = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print("Inicjały:", imie2[0].upper() + nazwisko[0].upper())
print()

lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)
print()

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print("Trzeci łańcuch:", lancuch3)
print()

lancuch4 = input("Podaj łańcuch do połowy: ")
srodek = len(lancuch4) // 2
lancuch5 = lancuch4[:srodek]
print("Pierwsza połowa trzeciego łańcucha:", lancuch5)