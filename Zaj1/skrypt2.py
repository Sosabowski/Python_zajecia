import math
import random
wartosc=100
dodawanie = wartosc + 123.15
potega=dodawanie **12
tekst = str(potega)
print(tekst)
wartosc_pi = math.pi
lista = [1,2,3,4,5]
losowa = random.choice(lista)

tekst=f"Wartosc: {tekst}"
print(tekst)
print(len(tekst))
print(tekst[1:4])
print(dir(tekst))

tekst=tekst.upper()
#tekst[2]="p"
print(tekst)
lista=list(tekst)
lista=lista[:8]
print(lista)
print(dir(lista))
lista.extend([1,2,3,4,5])
lista.remove(":")
print(lista)

lista2 = [1,2,3,"banan",100]
lista3=[element**2 for element in lista2 if not isinstance(element, str)]
print(lista3)
lista4=list(range(2,17,2))
print(lista4)


ja ={}
ja["imie"]="Wiktor"
ja["nazwisko"] = "Salwa"
ja["wiek"]=21
ja["rodzice"] = [
    {
    "imie":"Marta",
    "wiek":53
    },
    {
    "imie":"Sylwester",
    "wiek":54
    }
]
print(ja["rodzice"])
print(ja["rodzice"][0]["imie"])
print(ja.keys())
czy="rodzenstwo" in ja
print(czy)

krotka1=(1,2,"3",4,2,5)
print(len(krotka1))
print(krotka1[0])
#print(dir(krotka1))
print(krotka1.count(2))
#krotka1[0]=2

X=set("kalarepa")
Y=set("lepy")
print(X&Y)


names = ["Szymek", "Bartlomiej1", "Bartlomiej2", "MartynaDborodo", "Sumarix"]

for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")

numer=20
if numer > 0 and numer % 2 == 0:
    print("Liczba jest dodatnia i parzysta.")
else:
    print("Liczba nie jest zarówno dodatnia jak i parzysta.")

if numer != 0:
    print("Liczba jest różna od zera.")
else:
    print("Liczba jest równa zero.")

available_fruits = ['jabłko', 'banan', 'pomarańcza']
fruit = input("Wpisz owoc: ")

if fruit in available_fruits:
    print("Owoc jest dostępny.")
else:
    print("Niestety, nie mamy takiego owocu.")

sum = 0
while sum <= 100:
    number = float(input("Enter a number: "))
    sum += number
    print(f"Sum so far: {sum}")

print(f"The sum of all entered numbers is {sum}")