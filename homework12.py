# #1)Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def yosh_hisobla(tugulgan_yil,joriy_yil=2025):
#     """Foydalanuvchi tugilgan yilini uning yoshini hisoblaydi"""
#     print(f"Siz{joriy_yil-tugulgan_yil} yoshdasiz")
#
# yosh_hisobla(2006,2025)
# #2) Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing
# def kvadrat_kub(son):
#     """Berilgan sonning kvadrati va kubini chiqaradi"""
#     print(f"{son} ning kvadrati = {son ** 2}, kubi = {son ** 3}")
#
# kvadrat_kub(4)
#3). Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing
def juft_yoki_toq(son):
    """Sonning juft yoki toq ekanligini aniqlaydi"""
    if son % 2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")

juft_yoki_toq(7)
# #4) Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kattasini_top(a, b):
#     """Ikki sondan kattasini aniqlaydi"""
#     if a > b:
#         print(f"Kattasi: {a}")
#     elif b > a:
#         print(f"Kattasi: {b}")
#     else:
#         print("Sonlar teng")
#
# kattasini_top(8, 5)
# #5)Foydalanuvchidan x va y sonlarini olib, zni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     """x ning y-darajasini hisoblaydi"""
#     print(f"{x}^{y} = {x ** y}")
#
# daraja(3, 4)
# #6) Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=2):
#     """x ning y-darajasini hisoblaydi, agar y kiritilmasa 2 bo‘ladi"""
#     print(f"{x}^{y} = {x ** y}")
#
# daraja(5)
# daraja(5, 3)
# #7)7. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini
# tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
#
# In [93]: bolinish_alomatlari(70)
#
# 70 2 ga qoldiqsiz bo'linadi
#
# 70 5 ga qoldiqsiz bo'linadi
#
# 70 7 ga qoldiqsiz bo'linadi
#
# 70 10 ga qoldiqsiz bo'linadi
# def bolinish_alomatlari(son):
#     """Sonning 2 dan 10 gacha bo‘lgan sonlarga qoldiqsiz bo‘linishini tekshiradi"""
#     for n in range(2, 11):
#         if son % n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
#
# bolinish_alomatlari(70)
