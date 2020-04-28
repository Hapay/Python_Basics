# NIE PATRZ NA ROZWIAZANIE
# Uzywajac "nested loops" (podwojna petla) wyswietla na kosoli litere "F"
"""
XXXXX
XX
XXXXX
XX
XX
"""











# Izi way done in 1min haha
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    if i == 5:
        print("xxxxx")
    else:
        print("xx")
print("")

# Other way, done wrong again
cyfry = [5, 2, 5, 2, 2]

for k in cyfry:
    print("x" * k)
print("")

# Should be done with nested loop
tablica = [5, 2, 5, 2, 2]
for liczba in tablica:
    output = ""
    for licz in range(liczba):
        output += "x"
    print(output)