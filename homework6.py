# 1. Ota-onangiz haqida lug'at yaratish
otam = {
    "ismi": "Mavlutdin",
    "tugilgan_yili": 1954,
    "manzili": "Samarqand viloyati"
}

print(f"Otamning ismi {otam['ismi']}, {otam['tugilgan_yili']}-yilda, {otam['manzili']}da tug'ilgan")

# 2. Oila a'zolaringizning sevimli taomlari lug'ati
sevimli_taomlar = {
    "Alining": "osh",
    "Otabekning": "manti",
    "Mavludaning": "somsa",
    "Umidning": "shashlik",
    "Dilshodning": "lag'mon"
}

print(f"Alining sevimli taomi {sevimli_taomlar['Alining']}")

# 3. Python izohli lug'at yaratish
python_lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn turi",
    "if": "Agar shart operatori",
    "else": "Aks holda shart operatori",
    "list": "Ro'yxat turi",
    "tuple": "O'zgarmas ro'yxat",
    "dictionary": "Kalit-so'zlar lug'ati",
    "for": "Takrorlash sikli",
    "while": "Shartli sikl"
}

# 4. Foydalanuvchidan so'z kiritishni so'raymiz
soz = input("Kalit so'z kiriting: ").lower()

# 5. if-else yordamida tarjimani chiqaramiz
if soz in python_lugat:
    print(f"{soz.capitalize()} so'zi {python_lugat[soz]} deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")