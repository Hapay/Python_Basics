weight = input("Waga: ")
in_kg = int(weight) * 2.2 #zmienia na lbs
in_lbs = int(weight) * 0.45 #zmienia na kgs
ask_for_unit = input("Is the weight in (L)bs or (K)gs? ")
if ask_for_unit.upper() == "L":
    print(f"You weight {int(in_lbs)} kgs")
else:
    print(f"You weight {int(in_kg)} lbs")

# To u góry jest moje, na dole typa

waga = int(input("Waga: "))
unit = input("Podales/as wage w (F)untach czy (G)kilogramach? ")
if unit.upper() == "F":
    waga = waga * 0.45
    print(f"Podana waga w funtach wynosi {waga} kilogramow")
else:
    waga = waga * 2.2
    print(f"Podana waga w kilogramach wynosi {waga} funtow")