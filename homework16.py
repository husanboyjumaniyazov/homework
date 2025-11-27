# # rasmdagi
# class User:
#     def __init__(self, ism, username, email):
#         """Foydalanuvchi haqida malumot tuzush uchun funksiya"""
#         self.ism = ism
#         self.username = username
#         self.email = email
# 
#     def get_info(self):
#         """Foydalanuvchi malumotni konsilga chiqarish uchun funksiya"""
#         print(f"Foydalanuvchi: {self.username}, ismi: {self.ism}, email: {self.email}")
#
# # Obyektlar
# user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com")
# user2 = User("Gulbahor To'xtayeva", "gulbahor22", "gulbahor22@mail.com")
#
# # Ma'lumotlarni chiqarish
# user1.get_info()
# user2.get_info()
# # telegramdagi
# class Avto:
#     def __init__(self, model, yil, yurgan_km, narx):
#         self.model = model
#         self.yil = yil
#         self.yurgan_km = yurgan_km
#         self.narx = narx
# # 1
#     def info(self):
#         print(f"Model: {self.model}, Yil: {self.yil}, Yurgan masofa: {self.yurgan_km}"
#               f" km, Narx: {self.narx}")
# # 2
#     def yurish(self, km):
#         if km >= 0:
#             self.yurgan_km += km
#         else:
#             print("Km manfiy bo‘lishi mumkin emas")
# # 3
#     def chegirma(self, foiz):
#         if 0 <= foiz <= 100:
#             self.narx *= 1 - foiz / 100
#         else:
#             print("Chegirma foizi noto‘g‘ri")
# # 4
# # Obyektlarni yaratish
# nexia = Avto("Nexia", 2018, 60000, 9000)
# malibu = Avto("Malibu", 2020, 45000, 18000)
# tracker = Avto("Tracker", 2022, 30000, 25000)
#
# # Natijalarni chiqarish
# print("Boshlang‘ich ma’lumotlar:")
# for avto in [nexia, malibu, tracker]:
#     avto.info()
#
# # Metodlarni chaqirish
# malibu.yurish(500)
# tracker.chegirma(15)
# # Yangilangan natijalarni chiqarish
# print("\nYangilangan ma’lumotlar:")
# for avto in [nexia, malibu, tracker]:
#     avto.info()