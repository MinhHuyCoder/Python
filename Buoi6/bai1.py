S = input("Nhập số điện thoại: ")

khong_co = []

for i in range(10):
    if str(i) not in S:
        khong_co.append(i)

print("Các số không xuất hiện là:", khong_co)
