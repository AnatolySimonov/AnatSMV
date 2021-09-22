f = open(r"C:\Users\anato\Desktop\ДЗ5\notetoself.txt", "a")
f.write(input('What is the date today? Any news? \n') + '\n')
f.close()
f = open(r"C:\Users\anato\Desktop\ДЗ5\notetoself.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
