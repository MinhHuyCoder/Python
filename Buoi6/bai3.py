import zlib

with open("fileName.txt", "r", encoding="utf-8") as f:
    data = f.read()

compressed_data = zlib.compress(data.encode("utf-8"))

with open("compressed.bin", "wb") as f:
    f.write(compressed_data)

print("Đã tạo file nén.")

with open("compressed.bin", "rb") as f:
    compressed_content = f.read()

decompressed_data = zlib.decompress(compressed_content).decode("utf-8")

print("\nNội dung sau khi giải nén:")
print(decompressed_data)
