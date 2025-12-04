class Shaxs:
    odamlar_soni = 0

    def __init__(self, ism, familiya, yosh):
        self.__ism = ism
        self.__familiya = familiya
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def get_familiya(self):
        return self.__familiya

    def get_yosh(self):
        return self.__yosh

    def set_ism(self, ism):
        self.__ism = ism

    def set_familiya(self, familiya):
        self.__familiya = familiya

    def set_yosh(self, yosh):
        if yosh > 0:
            self.__yosh = yosh
        else:
            print("Yosh manfiy bo'lishi mumkin emas!")

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


class Talaba(Shaxs):

    talabalar_soni = 0

    def __init__(self, ism, familiya, yosh, universitet):
        super().__init__(ism, familiya, yosh)
        self.__universitet = universitet

        Talaba.talabalar_soni += 1

    def get_universitet(self):
        return self.__universitet

    def set_universitet(self, universitet):
        self.__universitet = universitet

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni

sh1 = Shaxs("Ali", "Valiyev", 30)
sh2 = Shaxs("Hasan", "Xolmatov", 25)

t1 = Talaba("Aziz", "Karimov", 20, "TATU")
t2 = Talaba("Madina", "Xudoyberdiyeva", 19, "IDU")

print("Odamlar soni:", Shaxs.get_odamlar_soni())
print("Talabalar soni:", Talaba.get_talabalar_soni())

print(t1.get_ism(), t1.get_universitet())
t1.set_universitet("NUU")
print("Yangi universitet:", t1.get_universitet())
