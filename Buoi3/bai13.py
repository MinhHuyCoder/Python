import re

def chuan_hoa_chuoi(s):
    lines = s.split('\n')
    lines = [line.strip() for line in lines]

    new_lines = []
    for line in lines:
        line = re.sub(r'\s+', ' ', line)

        line = re.sub(r'\s+([,.])', r'\1', line)

        new_lines.append(line)

    return '\n'.join(new_lines)


s = input("Nhập chuỗi:\n")

print("\nChuỗi sau khi chuẩn hóa:")
print(chuan_hoa_chuoi(s))
