# 5. Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar -faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar(a, b):
    tublar = []
    for son in range(a, b + 1):
        if son > 1:
            for i in range(2, int(son**0.5) + 1):
                if son % i == 0:
                    break
            else:
                tublar.append(son)
    return tublar
print(tub_sonlar(1, 30))
# 1.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kopaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija *= son
    return natija
print(kopaytma(2, 3, 4))      # 24
print(kopaytma(5, 10))        # 50
print(kopaytma())

# 2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasimajburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda
# istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
    talaba = {
        "ism": ism,
        "familiya": familiya
    }
    talaba.update(malumotlar)
    return talaba
print(talaba_info("Ali", "Valiyev", yosh=20, kurs=2, universitet="TATU"))
print(talaba_info("Laylo", "Karimova", yosh=19))