import random
rand = random.randrange(1, 11, 1)
print(rand)
# liczba = input("Zgaduj: ")
tries = 0
print("Wylosowano liczbe z przedzialu 1-10")
while tries < 3:
    liczba = int(input("Podaj liczbe: "))
    if liczba != rand:
        print("Bledna liczba. Zgaduj dalej")
        tries += 1
        print(f"Uzyto prob: {tries}")
    else:
        print("")
        print("Podano poprawnie liczbe! Wygrales/as!")
        break
else:
    print("")
    print("Podano blednie liczbe 3x. Koniec gry")
