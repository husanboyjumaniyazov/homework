# //1capitalize()    Converts the first character to upper case.
#                 Birinchi belgini katta harfga aylantiradi.
# 1)
# ism='XUSANBOY'
# familya='JUMANIYOZOV'
# ism_Sharif='XUSANBOY JUMANIYOZOV'
# print(ism_Sharif.capitalize())
#
# javob
#
# Xusanboy jumaniyozov
#
# 2)
# ism_Sharif='XUSANBOY Jumaniyozov'
# print(ism_Sharif.capitalize())
#
# javob
#
# Xusanboy jumaniyozov
#
# 3)ism_Sharif='1XUSANBOY Jumaniyozov'
# print(ism_Sharif.capitalize())
#
# javob
# 1xusanboy jumaniyozov
#
# //2casefold()      Converts string into lower case.
#                 Matnni kichik harflarga o‘zgartiradi.
# 1)
# ism_Sharif='XUSANBOY Jumaniyozov'
# print(ism_Sharif.casefold())
#
# javob
#
# xusanboy jumaniyozov
#
# 2)
# ism_Sharif='baLiQlar OlaMi'
# print(ism_Sharif.casefold())
#
# javob
# baliqlar olami
#
# 3)
# ism_Sharif='Ali 35 yoshda'
# print(ism_Sharif.casefold())
#
# javob
# ali 35 yoshda
#
#
# //3center()        Returns a centered string.
#                 Matnni markazga joylashtiradi.
#
# 1)
# txt='Salom '
# print(txt.center(10))
#
# javob
#   Salom
#
# 2)
# txt='Salom '
# print(txt.center(35))
#
# javob
#                Salom
#
# 3)
# txt='Salom '
# print(txt.center(56))
#
# javob
#                          Salom
#
#
# //4count()         Returns the number of times a specified value occurs in a string.
#                 Belgilangan qiymat nechta marta uchraganini qaytaradi.
# 1)
# matn="salom salom salom salom salom dunyo"
# print(matn.count("salom"))
#
# javob
# 5
# 2)
# matn="python!!!!!!!!!!!!!!1"
# print(matn.count("!"))
#
# javob
# 14
#
# 3)
# matn="olamni bosadi yaxshlik!"
# print(matn.count("a"))
#
# javob
# 3
#
# //5encode()        Returns an encoded version of the string.
#                 Matnning kodlangan (masalan, UTF-8) shaklini qaytaradi.
#
# //6endswith()      Returns true if the string ends with the specified value.
#                 Matn belgilangan qiymat bilan tugasa `True` qaytaradi.
#
# 1)
# txt = "Dunyo go'zal!"
# print(txt.endswith("go'zal!"))
#  javob True
#
# 2)
# txt = "Python dasturlash tili"
# print(txt.endswith("tili"))
#
# javob True
#
# 3)
# txt = "Bugun ob-havo yaxshi"
# print(txt.endswith("yomon"))
#
#  javob False
#
# //7expandtabs()    Sets the tab size of the string.
#                 Tab belgilarini bo‘sh joylar bilan almashtiradi.
# 1)
# txt = "Salom\tDunyo"
# print(txt.expandtabs())
#
# javob
# Salom   Dunyo
#
# 2)
# txt = "1\t2\t3"
# print(txt.expandtabs(4))
#
# javob
# 1   2   3
#
# 3)
# txt = "Python\tDasturlash\tTili"
# print(txt.expandtabs(2))
#
# javoi
#
# //8find()          Searches the string for a specified value and returns the position of where it was found.
#                 Matnda qiymatni qidirib, birinchi uchragan joyning indeksini qaytaradi
#
# 1)
# txt = "Salom dunyo!"
# print(txt.find("dunyo"))
#
# Javob:
# 6
#
# 2)
# txt = "Python dasturlash tili"
# print(txt.find("da"))
#
# Javob:
# 7
#
#
# //9 format()
# Matnga belgilangan qiymatlarni joylashtiradi.
#
# 1)
# txt = "Mening ismim {} va yoshim {}."
# print(txt.format("Ali", 25))
#
#
# Javob:
#
# Mening ismim Ali va yoshim 25.
#
# 2)
# txt = "Bugun {kun} va ob-havo {ob_havo}."
# print(txt.format(kun="dushanba", ob_havo="yomg‘irli"))
#
# Javob:
#
# Bugun dushanba va ob-havo yomg‘irli.
#
#
# //10 format_map()
# Lug‘atdagi qiymatlar yordamida matnni formatlaydi.
#
# 1)
# txt = "Ism: {ism}, Yoshi: {yosh}"
# data = {"ism": "Ali", "yosh": 30}
# print(txt.format_map(data))
#
# Javob:
#
# Ism: Ali, Yoshi: 30
#
# 2)
# txt = "Mahsulot: {nomi}, Narxi: {narxi} so'm"
# data = {"nomi": "Olma", "narxi": 5000}
# print(txt.format_map(data))
#
# Javob:
#
# Mahsulot: Olma, Narxi: 5000 so'm
#
# 3)
# txt = "Ism: {ism}, Familiya: {familiya}"
# data = {"ism": "Nilufar", "familiya": "Karimova"}
# print(txt.format_map(data))
#
# Javob:
#
# Ism: Nilufar, Familiya: Karimova
#
# //11index()
# Qiymatni topib, indeksini qaytaradi. Topilmasa xatolik beradi.
#
# 1)
# txt = "Salom dunyo!"
# print(txt.index("dunyo"))
#
# Javob:
#
# 6
#
# 2)
# txt = "Python dasturlash"
# print(txt.index("das"))
#
# Javob:
#
# 7
#
# 3)
# txt = "Matn ichida yo‘q"
# print(txt.index("hello"))
#
# Javob:
#
# ValueError: substring not found
#
# //12 isalnum()
# Matndagi barcha belgilar harf yoki raqam bo‘lsa True qaytaradi.
#
# 1)
# txt = "Python3"
# print(txt.isalnum())
#
#
# Javob:
#
# True
#
# 2)
# txt = "Salom123"
# print(txt.isalnum())
#
# Javob:
#
# True
#
# 3)
# txt = "Salom Dunyo!"
# print(txt.isalnum())
#
# Javob:
#
# False
#
# //13 isalpha()
# Matndagi barcha belgilar harflar bo‘lsa True qaytaradi.
#
# 1)
# txt = "Salom"
# print(txt.isalpha())
#
# Javob:
#
# True
#
# 2)
# txt = "SalomDunyo"
# print(txt.isalpha())
#
# Javob:
#
# True
#
# 3)
# txt = "Salom123"
# print(txt.isalpha())
#
# Javob:
#
# False
#
# //14 isascii()
# Matndagi barcha belgilar ASCII bo‘lsa True qaytaradi.
#
# 1)
# txt = "Hello123"
# print(txt.isascii())
#
# Javob:
#
# True
#
# 2)
# txt = "Salom"
# print(txt.isascii())
#
# Javob:
#
# False
#
# 3)
# txt = "Python!"
# print(txt.isascii())
#
# Javob:
#
# True
#
# //15 isdecimal()
# Matndagi barcha belgilar o‘nlik raqamlar bo‘lsa True qaytaradi.
#
# 1)
# txt = "12345"
# print(txt.isdecimal())
#
# Javob:
#
# True
#
# 2)
# txt = "12345.6"
# print(txt.isdecimal())
#
# Javob:
#
# False
#
# 3)
# txt = "٠١٢٣٤"  # Arab raqamlari
# print(txt.isdecimal())
#
# Javob:
#
# True
# 5. encode() – Matnni kodlangan (masalan, UTF-8) shaklga o‘tkazadi.
matn = "Salom"
print(matn.encode())
matn2 = "Til o‘rganish"
print(matn2.encode("utf-8"))


# 17. isidentifier() – Matn Python identifikatori bo‘la olsa True qaytaradi.
matn = "ism1"
print(matn.isidentifier())
matn2 = "1ism"
print(matn2.isidentifier())


# 18. islower() – Matndagi barcha harflar kichik bo‘lsa True qaytaradi.
matn = "salom"
print(matn.islower())
matn2 = "Salom"
print(matn2.islower())


# 19. isnumeric() – Matn faqat raqamlardan iborat bo‘lsa True qaytaradi.
matn = "123"
print(matn.isnumeric())
matn2 = "12a3"
print(matn2.isnumeric())


# 20. isprintable() – Matnning barcha belgilarini chop etish mumkin bo‘lsa True.
matn = "Salom dunyo"
print(matn.isprintable())
matn2 = "Salom\t"
print(matn2.isprintable())


# 21. isspace() – Matn faqat bo‘sh joylardan iborat bo‘lsa True.
matn = "     "
print(matn.isspace())
matn2 = "  salom  "
print(matn2.isspace())


# 22. istitle() – Har bir so‘z bosh harfi katta bo‘lsa True.
matn = "O‘zbekiston Yangi Hayot"
print(matn.istitle())
matn2 = "O‘zbekiston yangi hayot"
print(matn2.istitle())

# 23. isupper() – Matndagi barcha harflar katta bo‘lsa True.
matn = "SALOM"
print(matn.isupper())
matn2 = "Salom"
print(matn2.isupper())


# 24. join() – Ro‘yxatdagi elementlarni bitta matnga birlashtiradi.
mevalar = ["olma", "banan", "anjir"]
print(", ".join(mevalar))
shaharlar = ["Toshkent", "Buxoro", "Samarqand"]
print(" - ".join(shaharlar))
# 25. ljust() – Matnni chapga tekislab, o‘ng tomonga bo‘sh joy qo‘shadi.
matn = "salom"
print(matn.ljust(10, "-"))
matn2 = "kitob"
print(matn2.ljust(12, "."))  # misol 2# 26. lower() – Matnni kichik harflarga o‘zgartiradi.
matn = "SALOM DUNYO"
print(matn.lower())
matn2 = "PYTHON Juda Zo‘r"
print(matn2.lower())


# 27. lstrip() – Matn boshidagi bo‘sh joylarni olib tashlaydi.
matn = "     salom"
print(matn.lstrip())
matn2 = "   Python"
print(matn2.lstrip())


# 28. maketrans() – Tarjima qilish uchun jadval (translation table) yaratadi.
jadval = str.maketrans("aeiou", "12345")
matn = "salom"
print(matn.translate(jadval))
jadval2 = str.maketrans({"a": "@", "s": "$"})
matn2 = "asal"
print(matn2.translate(jadval2))


# 29. partition() – Matnni 3 qismga bo‘lib, tuple qaytaradi.
matn = "salom dunyo"
print(matn.partition(" "))
matn2 = "python=til"
print(matn2.partition("="))


# 30. replace() – Belgilangan so‘zni boshqasiga almashtiradi.
matn = "Men olma yaxshi ko‘raman"
print(matn.replace("olma", "anjir"))
matn2 = "Bugun yomg‘ir yog‘di"
print(matn2.replace("yomg‘ir", "quyosh"))


# 31. rfind() – So‘zni oxirgi marta uchragan joydan boshlab qidiradi.
matn = "salom salom salom"
print(matn.rfind("salom"))
matn2 = "kitob daftar kitob"
print(matn2.rfind("kitob"))


# 32. rindex() – So‘zni oxirgi marta topadi, ammo topilmasa xatolik beradi.
matn = "salom dunyo salom"
print(matn.rindex("salom"))
matn2 = "kitob daftar kitob"
print(matn2.rindex("kitob"))


# 33. rjust() – Matnni o‘ngga tekislab, chap tomonga belgi qo‘shadi.
matn = "salom"
print(matn.rjust(10, "*"))
matn2 = "python"
print(matn2.rjust(12, "-"))


# 34. rpartition() – Matnni oxirgi ajratuvchi bo‘yicha 3 qismga bo‘ladi.
matn = "olma, banan, anjir"
print(matn.rpartition(","))
matn2 = "daryo=Amudaryo"
print(matn2.rpartition("="))


# 35. rsplit() – Matnni o‘ng tomondan ajratadi va ro‘yxat qaytaradi.
matn = "olma banan anjir"
print(matn.rsplit(" ", 1))
matn2 = "bir,ikki,uch,to‘rt"
print(matn2.rsplit(",", 2))

# 36. rstrip() – Matn oxiridagi bo‘sh joylarni olib tashlaydi.
matn = "salom     "
print(matn.rstrip())
matn2 = "Python    "
print(matn2.rstrip())


# 37. split() – Matnni bo‘lib, ro‘yxatga ajratadi.
matn = "olma banan anjir"
print(matn.split())
matn2 = "bir,ikki,uch"
print(matn2.split(","))


# 38. splitlines() – Matnni qator bo‘yicha bo‘lib, ro‘yxatga ajratadi.
matn = "Salom\nYaxshimisan?\nMen yaxshiman."
print(matn.splitlines())
matn2 = "Bir\nIkki\nUch"
print(matn2.splitlines())


# 39. startswith() – Matn belgilangan so‘z bilan boshlansa True qaytaradi.
matn = "Salom dunyo"
print(matn.startswith("Salom"))
matn2 = "Python oson"
print(matn2.startswith("Java"))


# 40. strip() – Matnning boshi va oxiridagi bo‘sh joylarni olib tashlaydi.
matn = "   Salom dunyo   "
print(matn.strip())
matn2 = "---Python---"
print(matn2.strip("-"))


# 41. swapcase() – Katta harflarni kichikka, kichik harflarni kattaga o‘zgartiradi.
matn = "Salom Dunyo"
print(matn.swapcase())
matn2 = "pYTHON dASTURI"
print(matn2.swapcase())


# 42. title() – Har bir so‘zning birinchi harfini katta qiladi.
matn = "python dasturlash tili"
print(matn.title())
matn2 = "men o‘zbekistonda yashayman"
print(matn2.title())


# 43. translate() – Belgilarni tarjima jadvali asosida almashtiradi.
jadval = str.maketrans("aeiou", "12345")
matn = "salom"
print(matn.translate(jadval))
jadval2 = str.maketrans({"s": "$", "o": "0"})
matn2 = "soat"
print(matn2.translate(jadval2))


# 44. upper() – Matnni katta harflarga o‘zgartiradi.
matn = "salom dunyo"
print(matn.upper())
matn2 = "python darsi"
print(matn2.upper())
# 45. zfill() – Matn boshiga 0 qo‘shib, belgilangan uzunlikka keltiradi.
matn = "25"
print(matn.zfill(5))
matn2 = "123"
print(matn2.zfill(6))