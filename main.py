import random

nuo = 1
iki = int(input("Įveskite spėjamo skaičiaus diapazoną"))
diapazonas_nuo = nuo
diapazonas_iki = iki

spejamas_skaicius = random.randint(nuo, iki)
skaitiklis = 0

while True:
    print(f"Spėjimo diapazonas: nuo {diapazonas_nuo} iki {diapazonas_iki}")
    spejimas = int(input("Spėkite skaičių: "))
    if spejimas >= diapazonas_iki or spejimas <= diapazonas_nuo:
        print("Pasirinkote skaičių už diapazono")
        continue
    skaitiklis += 1

    if spejimas > spejamas_skaicius:
        print("Mažiau")
        diapazonas_iki = spejimas

    if spejimas < spejamas_skaicius:
        print("Daugiau")
        diapazonas_nuo = spejimas

    if spejimas == spejamas_skaicius:
        print(f"Laimėjote. Spėjamas skaičius - {spejimas}")
        print(f"Spėjimų skaičius - {skaitiklis}")
        break

print("Žaidimo pabaiga")


