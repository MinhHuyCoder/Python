money = [500, 200, 100, 50, 20, 10, 5, 2, 1]

x = int(input("Nhập số tiền: "))

tong_to = 0

print(f"So tien {x} duoc doi thanh:")

for i in money:
    so_to = x // i
    x = x % i

    print(f"Loai {i} gom {so_to} to")

    tong_to += so_to

print(f"TONG CONG CO {tong_to} TO")
