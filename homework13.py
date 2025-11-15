# #1
# def foydalanuvchi_haqida(ism, familiya, tyil, tjoy, email=None, telefon=None, yosh=None):
#     return {
#         "ism": ism,
#         "familiya": familiya,
#         "tugilgan_yil": tyil,
#         "tugilgan_joy": tjoy,
#         "email": email,
#         "telefon": telefon,
#         "yosh": yosh
#     }
# hammasi=foydalanuvchi_haqida('ali','valiyev',2006,'Xiva','jumaniyazovxusnboy19@gmail.com',993332928,19)
# for key,value in hammasi.items():
#     print(f"{key}: {value}")
# #2
# mijozlar=[]
# while True:
#     print("Mijoz maʼlumotlarini kiriting:")
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug‘ilgan yili: "))
#     tjoy = input("Tug‘ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon: ")
#
#     mijozlar.append(foydalanuvchi_haqida(ism, familiya, tyil, tjoy, email, telefon))
#
#     qolgan = input("Yana maʼlumot qo‘shilsinmi? (ha/yo‘q): ")
#     if qolgan.lower() != "ha":
#         break
#
# print("Ro‘yxat tayyor:")
# for a in mijozlar:
#     print(a)
#3
# def eng_katta(a, b, c):
#     return max(a, b, c)
# javob=eng_katta(1,2,3)
# print(javob)
# #4
# def aylana_radiusi(r):
#     import math
#     return {
#         "radius": r,
#         "diametr": 2 * r,
#         "perimetr": 2 * math.pi * r,
#         "yuza": math.pi * r**2
#     }
# aylana=aylana_radiusi(20)
# for k,v in aylana.items():
#     print(f"{k}: {v}")
# #5
# def tub_sonlar(a, b):
#     tublar = []
#     for son in range(a, b + 1):
#         if son > 1:
#             for j in range(2, int(son**0.5) + 1):
#                 if son % j == 0:
#                     break
#             else:
#                 tublar.append(son)
#     return tublar
# javob = tub_sonlar(8,6)
# if javob:
#     for a in javob:
#         print(a)
# else:
#     print("Berilganlarda tub son yo'q")
# 6
