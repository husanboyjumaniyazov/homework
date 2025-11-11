# # 1 Davlatlar ro'yxatini tuzamiz
# davlatlar = ["O'zbekiston", "AQSh", "Yaponiya", "Germaniya", "Fransiya", "Rossiya", "Turkiya"]
# print("Davlatlar ro'yxati:", davlatlar)

# # 2 Ro'yxat uzunligini konsolga chiqaramiz
# print("Ro'yxat uzunligi:", len(davlatlar))

# # 3 sorted() yordamida ro'yxatni tartiblaymiz
# print("Tartiblangan ro'yxat:", sorted(davlatlar))

# # 4 sorted() yordamida ro'yxatni teskari tartibda chiqaramiz
# print("Teskari tartibda tartiblangan ro'yxat:", sorted(davlatlar, reverse=True))

# # 4 Asl ro'yxatni qayta chiqaramiz
# print("Asl ro'yxat:", davlatlar)

# # 6 reverse() yordamida ro'yxatni orqadan boshlab chiqaramiz
# davlatlar.reverse()
# print("Orqadan boshlab:", davlatlar)

# # 7 sort() yordamida ro'yxatni avval alifbo, keyin teskari tartibda chiqaramiz
# davlatlar.sort()
# print("Alifbo bo'yicha tartiblangan:", davlatlar)

# davlatlar.sort(reverse=True)
# print("Alifboga teskari tartibda:", davlatlar)


# # 8 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzamiz
# juft_sonlar = list(range(120, 1201, 2))
# print("Juft sonlar ro'yxati:", juft_sonlar)

# #  9 Ro'yxatdagi sonlar yig'indisini hisoblaymiz
# print("Yig'indi:", sum(juft_sonlar))

# # 10 Eng katta va eng kichik son ayirmasi
# ayirma = max(juft_sonlar) - min(juft_sonlar)
# print("Eng katta va eng kichik son ayirmasi:", ayirma)

# # 11 Elementlar soni
# print("Elementlar soni:", len(juft_sonlar))

# # 12️ Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni chiqaramiz
# print("Boshidan 20 ta:", juft_sonlar[:20])
# print("O'rtasidan 20 ta:", juft_sonlar[len(juft_sonlar)//2 : len(juft_sonlar)//2 + 20])
# print("Oxiridan 20 ta:", juft_sonlar[-20:])


# # 13️ taomlar ro'yxatini yaratamiz
# taomlar = ["osh", "shashlik", "manti", "somsa", "lag'mon"]
# print("Taomlar:", taomlar)

# # 14️ nonushta ro'yxatini taomlar dan nusxa olamiz
# nonushta = taomlar[:]

# # 15️ Faqat nonushtaga yeyiladigan taomlarni qoldiramiz va 2 ta yangi qo'shamiz
# nonushta.remove("shashlik")
# nonushta.remove("manti")
# nonushta.append("tuxum")
# nonushta.append("qaymoq")

# # 16️ Ikkala ro'yxatni chiqaramiz
# print("Asl taomlar:", taomlar)
# print("Nonushta taomlari:", nonushta)

# # 17️ nonushta ro'yxatini o'zgarmas ro'yxatga (tuple) aylantiramiz
# nonushta = tuple(nonushta)

# # Tuple elementini o'zgartirib ko'ramiz
# # Bu xatolik beradi, chunki tuple o'zgarmas turdagi ro'yxat
# try:
# nonushta[0] = "qaymoq va non"
# except TypeError:
# print("xatolik: Tuple (o'zgarmas ro'yxat) elementlarini o'zgartirib bo'lmaydi!")
# print("Yakuniy nonushta ro'yxati:", nonushta)
