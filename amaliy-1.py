# 8.	Kiruvchi faylda n ta son berilgan. Ular orasidan bir xonali sonlarni “output.txt”
# fayliga chiqaruvchi dastur tuzing

# input.txt dan sonlarni o‘qish
with open("input.txt", "r") as f:
    numbers = list(map(int, f.read().split()))

# Bir xonali sonlarni ajratib olish
one_digit_numbers = [str(x) for x in numbers if -9 <= x <= 9]

# Natijani output.txt ga yozish
with open("output.txt", "w") as f:
    f.write(" ".join(one_digit_numbers))