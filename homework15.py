# # 1.
# def user_data(ism,familya,yosh):
#     print(f"Ism: {ism}")
#     print(f"Familiya: {familya}")
#     print(f"Yosh: {yosh}")
# ism = input("Ismingiz: ")
# fam= input("Familiyangiz: ")
# yosh= int(input("Yoshingiz: "))
# user_data(ism,fam,yosh)
# # 2.
# def find_max(a, b, c):
#     max_son= max(a, b, c)
#
#     if a == b == c:
#         print(f"Eng katta son - A va B va C = {max_son}")
#     elif a == b == max_son:
#         print(f"Eng katta son - A va B = {max_son}")
#     elif a == c == max_son:
#         print(f"Eng katta son - A va C = {max_son}")
#     elif b == c == max_son:
#         print(f"Eng katta son - B va C = {max_son}")
#     else:
#         print(f"Eng katta son = {max_son}")
# x = int(input("A: "))
# y = int(input("B: "))
# z = int(input("C: "))
# find_max(x, y, z)
#
# # 3
# def find_letter_count(word, letter):
#     count = word.count(letter)
#     print(f'"{word}" so‘zida "{letter}" dan {count} ta.')
# w = input("So‘zni kiriting: ")
# l = input("Qaysi harfni qidiramiz: ")
# find_letter_count(w, l)
# # 4
# def list_sum(myList):
#     print("List elementlari yig‘indisi =", sum(myList))
# myList = [4, 7, 8, 5, 2, 6]
# list_sum(myList)
#
# # 5
# def daraja(a, b):
#     print(a ** b)
# daraja(2, 5)
#
# # 6
# def daraja4(a, b, c, d):
#     print(a ** b)
#     print(a ** c)
#     print(a ** d)
# daraja4(2, 3, 4, 5)
#
# # 7
# def digit_count_and_sum(word):
#     yigindi= 0
#     soni = 0
#     for x in word:
#         if x.isdigit():
#             yigindi += int(x)
#             soni+= 1
#     print("Raqamlar soni:", soni)
#     print("Raqamlar yig‘indisi:", yigindi)
# digit_count_and_sum("a1b5c90")
#
# # 8
# def add_right(a, b):
#     print(int(str(a) + str(b)))
# add_right(123, 45)
#
# # 9
# def add_left(a, b):
#     print(int(str(b) + str(a)))
# add_left(123, 45)
#
# # 10
# def work_with_list(a):
#     mn = min(a)
#     for i in range(len(a)):
#         a[i] *= mn
#     print(a)
# work_with_list([4, 2, 6, 3])
#
# # 11
# def big_sales(sales):
#     max_month = max(sales, key=sales.get)
#     return max_month
# sales = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000
# }
# print("Eng ko‘p sotuv bo‘lgan oy:", big_sales(sales))
#
# # 12
# def min_max(numbers, max_num, min_num):
#     if max_num == max(numbers):
#         print("max_num – eng katta son. ")
#     else:
#         print("max_num – eng katta son EMAS. ")
#
#     if min_num == min(numbers):
#         print("min_num – eng kichik son. ")
#     else:
#         print("min_num – eng kichik son EMAS. ")
# min_max([4, 6, 2, 9], 9, 2)
#
# # 13
# def expensiveProduct(products):
#     max_price = max(products, key=lambda x: x["price"])
#     print("Eng qimmat telefon:", max_price["name"])
#
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100},
# ]
#
# expensiveProduct(products)