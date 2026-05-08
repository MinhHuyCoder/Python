S = input("Nhập chuỗi: ")

tu = S.split()

da_xuat_hien = []

ket_qua = None

for i in tu:
    if i in da_xuat_hien:
        ket_qua = i
        break
    da_xuat_hien.append(i)

print(ket_qua)
