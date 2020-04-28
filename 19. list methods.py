numbers = [4, 5, 1, 7, 21, 44, 9, 4]
numbers.append(20)  # .append dodaje liczbe na koniec listy
print(numbers)
numbers.insert(0, 77)  # dodaje liczbe we wskazane miejsce w liscie. po wpisaniu numbers.insert i wejscie
# w nawias to pokazuje sie nad nim tooltip, ktory mowi, co gdzie nalezy wpisac
print(numbers)
numbers.remove(1)
print(numbers)
print("")

# .clear usuwa wszystko z listy
lista = [1, 2, 3]
print(lista)
lista.clear()
print(lista)
print("")

# .pop usuwa ostatni dodany element z listy
numbers.pop()
print(numbers)
print("")

# .index wyszukuje danego w elementu w liscie
print(numbers.index(7))  # liczba 7 jest na 4 miejscu w liscie
print("")

# mozna takze spawdzic czy dany element istnieje w liscie
print(50 in numbers)  # bool'owa odpowiedz
print(numbers.count(4))  # pokazuje, ile takich samych elementow jest w liscie

print("")
numbers.sort()  # sortowanie rosnąco
print(numbers)
numbers.reverse()  # odbicie lustrzane
print(numbers)
print("")

numbers2 = numbers.copy()  # kopiuje liste. wszystko, co jest po tym jest juz nie wliczane do tej kopii. pretty simple :)
numbers.append(69)
print(numbers)
print(numbers2)
print("")

# ZADANIE   Remove the duplicates in the list
tab = [1, 44, 2, 7, 2, 4, 51, 4, 1, 23, 7, 12]
uniques = []
print(tab)
for number in tab:
    if number not in uniques:
        uniques.append(number)
print(uniques)
