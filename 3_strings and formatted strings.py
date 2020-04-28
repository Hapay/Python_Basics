#Jesli chcemy pojedynczy cudzyslow (') w stringu lub princie to musimy uzyc (")
#Dziala to w dwie strony!
course= "It's course"
print(course)

#Jesli chcemy zrobic np email lub zrobic stringiem caly blok wtedy uzywamy potrojnie ' (''')
email = '''
Hi Patryk,
Here is our first email to you ;)

Thank you,
The support team 
'''
print(email)

#Printowanie danych liter ze stringa
kurs = 'Kurs dla beginnersow XD'
print(kurs[1])


#Mozemy tez podawac ujemne liczby
print(kurs[-1])


#Wyswietlanie przedzialow stringa
print(kurs[0:4]) #5 znak (czyli 4) juz nie jest wliczany!

#===============FORMATTED STRINGS=====================

first = 'John'
last = 'Smith'
msg = first + '[' + last + '] is a coder'
message = f'{first} [{last}] is a coder' #TO JEST NAZYWANE WLASNIE FORMATTED STRINGIEM!
print(msg)
print(message)