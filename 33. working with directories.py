# Dodaje klasy, ktore mozemy uzyc do utworzenia obiektow, ktore mozemy uzyc do dzialania z folderami i plikami
from pathlib import Path

# We can use 'absolute path' (c:/program files/asdasd)
# Or 'relative path' czyli sciezka rozpoczynajaca sie od aktualnej sciezki

path = Path("paczka")
print(path.exists()) # Sprawdzamy czy taki folder w ogole istnieje


sciezka = Path("emails")
# sciezka.mkdir()   stwarza folder o nazwie "emails"
# sciezka.rmdir()   usuwa folder

path2 = Path()
print(path2.glob('*.py'))       # Sposoby szukania 1) '*' szuka wszystko    2) '*.*' szuka tylko pliki  3) '*.py' tylko rozszerzenia
# Generator objects to jest advanced shit, ale musimy tutaj uzyc "for" loopa zeby ogarnac jakie sa pliki

for file in path2.glob('*.py'):
    print(file)