with open("fileName.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()

data = {}

for i in range(len(words)):
    word = words[i]

    if word not in data:
        data[word] = []

    data[word].append(i)

with open("compressed.txt", "w", encoding="utf-8") as f:
    f.write(str(data))

print("Đã tạo file giảm dung lượng.")

result = [""] * len(words)

for word in data:
    for pos in data[word]:
        result[pos] = word

original_text = " ".join(result)

print("\nVăn bản khôi phục:")
print(original_text)
