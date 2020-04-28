def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😒",
        "<3": "❤"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))

# Zazwyczaj w funkcji nie uwzgledniamy inputu i outputu dlatego, ze input i output moga miec rozne "zadanie" i roznie
# moga byc odbierane. Np input nie musi byc z konsoli tylko np z jakiegos przycisku, dlatego lepiej definiowac go poza
# funkcja. To samo z wyjsciem. Output moze nie byc printem tylko np returnem do jakiejs innej funkcji