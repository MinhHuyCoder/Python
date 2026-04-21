import re

S = input("Nhập chuỗi S: ")
word = input("Nhập từ cần đếm: ")

S = S.lower()
word = word.lower()

words = re.findall(r'\b\w+\b', S)

count = words.count(word)

print(f"Số từ '{word}' là: {count}")
