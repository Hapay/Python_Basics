# Modulem w pythonie jest wlasciwie plik z jakims python kodem
# i uzywamy modolow do organizowania kodow do wielu plikow
# W pliku 31.2 mam konwerter wagi (lbs na kgs i na odwrot)
# Lub mozemy tez importowac dane funkcje (jak jestesmy przy import to CTRL + SPACE

from paczka.importowanie import kgs_to_lbs

print(kgs_to_lbs(60))

#import converters
#print(converters.kgs_to_lbs(60))



#ZADANIE zrob tablice, funkcje, ktora bedzie wyznaczac najwyzsza liczbe z tablcy. importuj funkcje z innego modulu
# (u mnie z converters) i uruchom ja tu
from paczka import importowanie

tab = [6, 2, 11, 87, 69, 111, 97, 21, 234, 87]
maximum = importowanie.find_max(tab)
print(maximum)