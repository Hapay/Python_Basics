birth_year = input('Rok urodzenia: ')
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

#ZADANIE 1  Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

askweight = input('Hello user! What is your weight in pounds?')
weightinKG = int(askweight) * 0.45
print('Your weight in kgs is: ', weightinKG)