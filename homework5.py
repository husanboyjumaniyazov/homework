#  1-topshiriq: Foydalanuvchidan 5 ta eng sevimli kinoni so‘rash
kinolar = []
for i in range(1, 6):
    kino = input(f"{i}-sevimli kino nomini kiriting: ")
    kinolar.append(kino)

print("Sizning eng sevimli kinolaringiz:")
print(kinolar)


#  2-topshiriq: Bugun nechta kishi bilan suhbat qilganini so‘rash
n = int(input("Bugun necha kishi bilan suhbat qildingiz? >>> "))
suhbatlar = []

for i in range(1, n + 1):
    ism = input(f"{i}-suhbat qilgan odamingiz kim edi: ")
    suhbatlar.append(ism)

print("Siz suhbat qilgan odamlar ro‘yxati:")
print(suhbatlar)


#  3-topshiriq: Kamida 5 ta ismli ro‘yxat yaratish va har biriga "Salom" yozish
print("Ismlar ro‘yxati:")
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]

for ism in ismlar:
    print(f"Salom {ism}")

print(f"Kod {len(ismlar)} marta takrorlandi")


# 4-topshiriq: 10 dan 100 gacha bo‘lgan TOQ sonlar ro‘yxatini tuzish
# va ularning kubini chiqarish
print("10 dan 100 gacha bo‘lgan TOQ sonlarning kubi:")
toq_sonlar = list(range(11, 100, 2))

for son in toq_sonlar:
    print(son ** 3)