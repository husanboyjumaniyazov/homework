# 1
# with open('new_file.txt') as fayl:
#     bu_kun=fayl.read()
#
# print(bu_kun)
# print(type(bu_kun))
#
# # 2
# faylni_nomi ='pi_million_digits.txt'
# pi = 3,14
#
# with open(faylni_nomi,'r') as fayl:
#     fayl.write(pi)
#     faylni_nomi ='pi_million_digits.txt'

# 3
# def tugilgan_sana_pi_da(pi_million_digits, sana):
#     with open(pi_million_digits) as f:
#         pi = f.read().replace("\n", "").replace(" ", "")
#     if pi.startswith("3."):
#         pi = pi[2:]
#     return sana in pi
#
# sana = "802006"   # <-- mana shu joyga yozing
#
# natija = tugilgan_sana_pi_da("pi_million_digits.txt", sana)
# print(natija)

# 4
faylnomi ='new_file.txt'
ism='Jumaniyazav Xusanboy'
tyil=2004

import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
