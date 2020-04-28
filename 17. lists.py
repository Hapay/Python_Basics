names = ['John', 'Bob', 'Mosh', 'Patryk', 'Gabi']
names[0] = 'Jon'
print(names)
print(names[2])
print(names[-1])
print(names[2:]) #Od pozycji drugiej do samego konca


# Find the highest number in the list
tablica = [5, 12, 7, 111, 543, 62, 542, 1]
max = tablica[0]
for number in tablica:
    if number > max:
        max = number
print(max)

