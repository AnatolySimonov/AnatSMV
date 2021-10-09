import re


cats = open('cats.txt', 'r', encoding="utf-8")
file_contents = cats.read()
cats.close()
result = re.findall(r'\b[Кк]ош[а-я]+', file_contents)
print(len(result))

