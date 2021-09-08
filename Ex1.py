string1 = 'Съешь еще этих мягких французских булок ДА выпей же чаю'
print(string1.split()[2].upper())
print(string1.split()[6].lower())
print(string1.split()[7].lower()[2])

for words in string1:
    print(words, end='')
