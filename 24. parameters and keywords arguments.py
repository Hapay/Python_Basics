def przywitanie(first_name, last_name):
    print(f"Hejoooo, {first_name} {last_name} ")
    print("Kolejna funkcja z Mosh'em")


print("Poczatek")
przywitanie("Patryk", "Majchrzak")
print("Koniec")

print("")
przywitanie(last_name="Majchrzak", first_name="Patryk")  # to jest nazywane keyword argument'em tj podajemy wartosc
# do argumentu, tym samym nie musimy zachowywac kolejnosci. Jest to dobre kiedy masz np w argumentach liczby
# i ciezko wywnioskowac co dana liczba ma przekazywac.
# Nalezy pamietac ze mozna mieszac keyword arg z positional arg, ale positional MUSI byc na poczatku!
