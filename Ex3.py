f = open(r"C:\Users\anato\Desktop\ДЗ5\lesson05_cats_of_ulthar.txt")
wordcount = 0
word = "кошка"
for line in f:
    if word in line.split():
        wordcount += 1
        print('Слово', word, 'встречается', wordcount, 'раз' '\t')
        print(line)
print('Всего слово', word, 'встречается', wordcount, 'раз(а)')
