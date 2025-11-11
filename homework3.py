# # Ro‘yxatlar
# universitetlar = ['TATU', 'Texno', 'Oksford', 'Kembridj', 'Kornel', 'Texno']
# mevalar = ['anor', 'gilos', 'olcha', 'shaftoli', 'behi', 'nok']
# hayvonlar = ['ot', 'sigir', 'quyon', 'mushuk', 'it']
#
# # append() — oxiriga yangi element qo‘shadi
# universitetlar.append('Harvard')
# print(universitetlar)
# mevalar.append('anjir')
# print(mevalar)
#
# # clear() — barcha elementlarni o‘chiradi
# hayvonlar.clear()
# print(hayvonlar)
#
# # copy() — ro‘yxat nusxasini qaytaradi
# nusxa = universitetlar.copy()
# print(nusxa)
#
# # count() — ro‘yxatda nechta bir xil qiymat borligini hisoblaydi
# print(universitetlar.count('Texno'))
#
# # extend() — boshqa ro‘yxat elementlarini oxiriga qo‘shadi
# universitetlar.extend(mevalar)
# print(universitetlar)
#
# # index() — berilgan qiymatning tartib raqamini topadi
# raqam = mevalar.index('shaftoli')
# print(raqam)
#
# # insert() — kerakli joyga yangi element qo‘shadi
# mevalar.insert(2, 'limon')
# print(mevalar)
#
# # pop() — berilgan joydagi elementni olib tashlaydi
# olingan = mevalar.pop(3)
# print(olingan)
# print(mevalar)
#
# # remove() — ma’lum qiymatdagi elementni o‘chiradi
# universitetlar.remove('Oksford')
# print(universitetlar)
#
# # reverse() — elementlar tartibini teskari qiladi
# mevalar.reverse()
# print(mevalar)
#
# # sort() — elementlarni tartiblaydi (alfavit yoki sonlar bo‘yicha)
# universitetlar.sort()
# print(universitetlar)
#
# # sort() — sonlar ro‘yxatini tartiblaydi
# sonlar = [8, -4, 23, 0, 15, 9]
# sonlar.sort()
# print(sonlar)