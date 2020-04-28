course = 'Python for beginners'

print(len(course))

print(course.upper())
print(course.lower())
print(course)

# --------------------------------------------------------------------------------- #
kurs = "Kurs dla beginnersow"
print(kurs.find('b'))   #Jesli dostajemy -1 to znaczy, ze nie ma takiej litery

print(kurs.find('dla'))
print(kurs.replace('beginnersow', 'programistow'))

print(course.replace('P', 'J'))

# --------------------------------------------------------------------------------- #
#Wyszukiwanie wyrazow
print('Python' in course) #Oddaje True or False (wielkosc liter ma znaczenie!
