customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["is_verified"])  # lub można tak
print(customer.get("name"))  # różnica jest taka, że po wpisaniu np. "birthdate" (nie ma takiego czegos uwzglednionego
# w metodzie "customer" to nie wywala nam bledu w drugim przypadku, tylko wyswietla "none"
print(customer.get("birthdate", "5 Sep 1997"))

# ZADANIE   Program pyta o nr telefonu. Po wpisaniu nr wyswietla on sie slownie
ask_number = input("Phone: ")
number = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for char in ask_number:
    output += number.get(char, "!") + " "   # tutaj "!" to jest liczba, ktora nie zostala uwzgledniona w "number" czyli np 0
print(output)
