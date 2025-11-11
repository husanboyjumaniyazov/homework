## Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni
## lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
## O'zbekistonning poytaxti Toshkent Hududi: 448978 kv.km Aholisi: 33000000 Pul birligi:
##so'm
##Rossiyaning poytaxti Moskva Hududi: 17098246 kv.km Aholisi: 144000000 Pul birligi: rubl
## AQSHning poytaxti Vashington Hududi: 9631418 kv.km Aholisi: 327000000 Pul birligi: dollar
## Malayziyaning poytaxti Kuala-Lumpur Hududi: 329750 kv.km Aholisi: 25000000 Pul birligi:
## rinngit
## Kutilgan natijaga misal
## Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi
## so'ragan davlat haqida ma'lumot bering. Agar davlat sizning
## lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q degan xabarni
## chiqaring
## Davlat nomini kiriting: O'zbekiston
## O'zbekistonning poytaxti Toshkent Hududi: 448978 kv.km Aholisi: 33000000 Pul birligi: so'm
##Davlat nomini kiriting: Singapur Bizda bu davlat haqida ma'lumot mavjud emas
#Davlatlar haqidagi ma'lumotlarni lug'atda saqlaymiz
davlatlar = {
    "o'zbekiston": {
        "poytaxt": "Toshkent",
        "hududi": "448978 kv.km",
        "aholisi": "33000000",
        "pul_birligi": "so'm"
    },
    "rossiya": {
        "poytaxt": "Moskva",
        "hududi": "17098246 kv.km",
        "aholisi": "144000000",
        "pul_birligi": "rubl"
    },
    "aqsh": {
        "poytaxt": "Vashington",
        "hududi": "9631418 kv.km",
        "aholisi": "327000000",
        "pul_birligi": "dollar"
    },
    "malayziya": {
        "poytaxt": "Kuala-Lumpur",
        "hududi": "329750 kv.km",
        "aholisi": "25000000",
        "pul_birligi": "rinngit"
    }
}

# Foydalanuvchidan davlat nomini so'raymiz
davlat = input("Davlat nomini kiriting: ").lower()  # Katta-kichik farqini yo'qotamiz

# Davlat lug'atda mavjudligini tekshiramiz
if davlat in davlatlar:
    info = davlatlar[davlat]
    # Birinchi harfini katta qilib chiqaramiz
    nom = davlat.capitalize() if davlat != "aqsh" else "AQSH"
    print(f"\n{nom}ning poytaxti {info['poytaxt']}")
    print(f"Hududi: {info['hududi']}")
    print(f"Aholisi: {info['aholisi']}")
    print(f"Pul birligi: {info['pul_birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas.")
