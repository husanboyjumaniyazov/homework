
#1. Svetafor masalasi.
#Foydalanuvchidan input orqali svetafor qaysi rangda ekanini so‘rang.
#Foydalanuvchi qizil, sariq yoki yashil deb yozmagunicha, “xato rang” deb qayta so‘rab turing.
#Agar shu ranglardan birini tanlasa, “Rahmat, to‘g‘ri keladi” degan xabar chiqsin.

while True:
    rang = input("Svetafor qaysi rangda? (qizil, sariq yoki yashil): ").lower()
    if rang in ["qizil", "sariq", "yashil"]:
        print("Rahmat, to'g'ri keladi!")
        break
    else:
        print("Xato rang, qayta urinib ko'ring.")

#2. Tasodifiy sonni topish o‘yini
#Kompyuter 1 dan 10 gacha bo‘lgan tasodifiy son o‘ylaydi.
#Foydalanuvchidan ushbu sonni topishni so‘rang.
#Foydalanuvchi to‘g‘ri sonni topmaguncha “Noto‘g‘ri, qayta urinib ko‘ring” deb chiqaring.
#To‘g‘ri topilganda esa “Tabriklaymiz, siz topdingiz!” deb chiqsin.
#Ko‘rsatma: random kutubxonasidan foydalaning.

#3. Do‘stlar ro‘yxatini yaratish
#Foydalanuvchidan do‘stlarining ismlarini kiritishni so‘rang.
#Foydalanuvchi "stop" deb yozmaguncha yangi ismlar kiritishda davom etsin.
#Oxirida barcha kiritilgan do‘stlarning ismlari ro‘yxat ko‘rinishida chiqsin.
#Ko‘rsatma: while sikli va listdan foydalaning.
do_stlar = []
while True:
    ism = input("Do'stingizning ismini kiriting (to'xtatish uchun 'stop' yozing): ")
    if ism.lower() == "stop":
        break
    else:
        do_stlar.append(ism)
print("\nSizning do'stlaringiz ro'yxati:")
for ism in do_stlar:
    print("-", ism)

# 4. Valyuta ayirboshlash kalkulyatori
#Foydalanuvchiga valyuta ayirboshlash imkoniyatini bering.
#U so‘mni dollarga almashtirishi mumkin.
#Valyuta kursi oldindan belgilansin (masalan, 1 USD = 12,600 so'm).
#Foydalanuvchi summani kiritadi, dastur esa uni dollarga hisoblab beradi.
#Foydalanuvchi "exit" deb yozmaguncha dastur ishlashda davom etadi.
#exit yozsa dastur to‘xtasin.