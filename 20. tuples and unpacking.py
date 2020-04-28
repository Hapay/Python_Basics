# Tuples to inaczej Krotka – struktura danych będąca odzwierciedleniem matematycznej n-ki, tj. uporządkowanego ciągu wartości.
# Krotki przechowują stałe wartości o różnych typach danych – nie można zmodyfikować żadnego elementu, odczyt natomiast
# wymaga podania indeksu liczbowego żądanego elementu.

numbers = (1, 2, 3)
print(numbers)

#UNPACKING lesson
coordinates = (1, 2, 3)
print(coordinates[0] * coordinates[1] * coordinates[2])

# inna metoda
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# TUTAJ DOPIERO JEST METODA UNPACKING'U
x, y, z = coordinates # To co jest tutaj to dokladnie to samo co w linijce 12-15!