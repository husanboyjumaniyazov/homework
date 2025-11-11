# 1. Foydalanuvchilar ro'yxati
foydalanuvchilar = ["umar", "ozod", "dilshod", "javlon", "aziz"]

login = input("Yangi login tanlang: ").lower()

if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz!")

# 2. Foydalanuvchidan son kiritishni so'rash va 2 dan 10 gacha bo'linishini tekshirish
son = int(input("\nIstalgan butun son kiriting: "))

for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")

# 3. Juft son tekshirish
juft_son = int(input("\nJuft son kiriting: "))
if juft_son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")

# 4. Yoshga qarab muzeyga kirish narhini aniqlash
yosh = int(input("\nYoshingizni kiriting: "))

if yosh < 4 or yosh > 60:
    print("Sizga kirish bepul!")
elif yosh < 18:
    print("Chipta narxi 10 000 so'm")
else:
    print("Chipta narxi 20 000 so'm")

# 5. Ikkita sonni solishtirish
birinchi = float(input("\nBirinchi sonni kiriting: "))
ikkinchi = float(input("Ikkinchi sonni kiriting: "))

if birinchi < ikkinchi:
    print(f"{birinchi} < {ikkinchi}")
elif birinchi > ikkinchi:
    print(f"{birinchi} > {ikkinchi}")
else:
    print(f"{birinchi} = {ikkinchi}")