def odamlar_haqida(ism,familya,yosh):
   odam={
       'ism':ism,
       'familya':familya,
       'yosh':yosh
   }
   return odam

def odamlarni_kirit():
    odamlar=[]
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        ismi=input("ismi: ")
        familya=input("familya: ")
        yosh=input("yosh: ")
        odamlar.append(odamlar_haqida(kompaniya, model, rangi, korobka, yili, narhi))
        javob = input("Yana odam qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
#     return odamlar


def odamlar_print(odamlar_haqida):
    print(f"{odamlar_haqida['ism'].title()} {odamlar_haqida['familya'].upper()} "
          f"{odamlar_haqida['yosh'].upper()}")
