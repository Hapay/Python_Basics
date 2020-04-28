message = input(">")
words = message.split(' ')
print(words)
print("")
emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)