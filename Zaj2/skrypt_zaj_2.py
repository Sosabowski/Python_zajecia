#Przypisania

dane = (2024, 'Python', 3.8)

rok, jezyk, wersja = dane
print(f'Rok: {rok}, Język: {jezyk}, Wersja: {wersja}')

oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(f'Pierwsza ocena: {pierwsza}, Środek: {srodek}, Ostatnia ocena: {ostatnia}')

info = ('Jan', 'Kowalski', 30, 'Polska', 'Programista')
imie, nazwisko, _, _, zawod = info
print(f'Imię: {imie}, Nazwisko: {nazwisko}, Zawód: {zawod}')

dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, lista = dane
jezyk, wersja, opis = lista
print(f'Rok: {rok}, Język: {jezyk}, Wersja: {wersja}, Opis: {opis}')

#Zad 10-12

a = b = [1, 2, 3]
b[0] = 'zmieniono'
print(f'a :{a}, b :{b}')

c = a.copy()

c[0] = 'nowa wartość'

print(f'a :{a}, b :{b}, c : {c}')

x = y = 10
y = y + 1

print(f'x :{x}, y :{y}')

#Zad 13

K = [1, 2]
L = K
K = K + [3, 4]
M = [1, 2]
N = M
M += [3, 4]

print(f'K :{K}, L :{L}, M : {M}, N : {N}')

#Zad 14-15

imiona = ['Anna', 'Jan', 'Ewa'] 
oceny = [5, 4, 3]

pairs = zip(imiona, oceny)

for para in pairs:
    print(para)

print(f'pary :{pairs}')



def kwadrat(x):
    return x**2

liczby = [1, 2, 3, 4, 5]

n_lista = list(map(kwadrat, liczby))

print(f'Liczby : {liczby}, Lista po podniesieniu do kwadratu :{n_lista}')

#Zad 16

def zmien_wartosc(arg):
    if isinstance(arg, list): 
        arg[0] = 'kalafior'
    elif isinstance(arg, int): 
        arg = 65482652
    return arg

lista = [1, 2, 3]
print("Lista przed:", lista)
print("Lista po:", zmien_wartosc(lista))

int_przed = 123
print("Int przed:", int_przed)
print("Int po:", zmien_wartosc(int_przed))

#Zad 17

def zamowienie_produktu(produkt, *, cena, ilosc=1):
    wartosc_zam = cena * ilosc
    pods = f"Nazwa produktu: {produkt}, Cena: {cena} zł, Ilość: {ilosc}, Łączna cena: {wartosc_zam} zł"
    return pods, wartosc_zam

zamowienia = []

zamowienia.append(zamowienie_produktu("Kawa", cena=5, ilosc=3))
zamowienia.append(zamowienie_produktu("Herbata", cena=5.5))
zamowienia.append(zamowienie_produktu("Chlebek", cena=15, ilosc=12))

for index, (pods, wartosc) in enumerate(zamowienia, start=1):
    print(f"Zamówienie {index}: {pods}")

suma_zamowien = sum(wartosc for _, wartosc in zamowienia)
print("Sumaryczna wartość zamówień:", suma_zamowien)

#Zad 18
def stworz_raport(*args, **kwargs):
    for id_produktu in args:
        print(f"Informacje o produkcie o ID {id_produktu}:")
        for key, value in kwargs.items():
            if str(id_produktu) in key:
                print(f"{key.split('_')[0]}: {value}")

stworz_raport(101, 102, nazwa_101='Kubek termiczny', cena_101='45.99 zł', nazwa_102='Długopis', cena_102='4.99 zł')

#Zad 19

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega_2 = stworz_funkcje_potegujaca(2)

print(potega_2(4)) 


#Zad 21

from typing import Callable

def licznik() -> Callable[[], int]:
    if not hasattr(licznik, 'count'):
        licznik.count = 0
    licznik.count += 1
    return licznik.count

print(licznik())  
print(licznik())  

#Zad 22

ksiazki = [
    {'tytul': 'Droga wiodła ugorem', 'autor': 'Stanisław Sosabowski', 'rok_wydania': 1967},
    {'tytul': 'Księgi Jakubowe', 'autor': 'Olga Tokarczuk', 'rok_wydania': 2014},
    {'tytul': 'Don Kichot', 'autor': 'Miguela de Cervantesa', 'rok_wydania': 1615},
    {'tytul': 'Zemsta', 'autor': 'Aleksander Fredro', 'rok_wydania': 1838},
    {'tytul': 'Jak wytresować smoka', 'autor': 'Cressida Cowell', 'rok_wydania': 2003}
]

#Sortowanie po roku
posortowane = sorted(ksiazki, key=lambda x: x['rok_wydania'])
print("Książki posortowane (rok wydania):")
print(posortowane)
#Filtracja > 2000 rok
ksiazki_2000 = list(filter(lambda x: x['rok_wydania'] > 2000, ksiazki))
print("\nWydane po roku 2000:")
print(ksiazki_2000)
#c Transformacja do listy tytułów książek
tytuly = list(map(lambda x: x['tytul'], ksiazki))
print("\nTytuły:")
print(tytuly)

#Zad 23

def generator_dni_tygodnia():
    tagen = ['Montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag']
    for tag in tagen:
        yield tag


print("Alle Tage der Woche:")
for tag in generator_dni_tygodnia():
    print(tag)

print("\nErste drei Tage der Woche:")
pierwsze_trzy_dni = list(generator_dni_tygodnia())[:3]
print(pierwsze_trzy_dni)
