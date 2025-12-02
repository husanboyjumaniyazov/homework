class Fan:
    def __init__(self, nom):
        self.nom = nom

class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar = [fan.nom for fan in self.fanlar]
        return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fanlar: {fanlar}"

class Professor:
    def __init__(self, ism, fan):
        self.ism = ism
        self.fan = fan

    def get_info(self):
        return f"Professor: {self.ism}, Fan: {self.fan}"

class Foydalanuvchi:
    def __init__(self, ism, login):
        self.ism = ism
        self.login = login

    def get_info(self):
        return f"Foydalanuvchi: {self.ism}, Login: {self.login}"

class Mijoz:
    def __init__(self, ism, balans):
        self.ism = ism
        self.balans = balans

    def get_info(self):
        return f"Mijoz: {self.ism}, Balans: {self.balans}"

class Admin(Foydalanuvchi):
    def ban_user(self):
        print("Foydalanuvchi bloklandi")

    def get_info(self):
        return f"Admin: {self.ism}, Login: {self.login}"

math = Fan("Matematika")
eng = Fan("Ingliz tili")

talaba = Talaba("Ali", 20)
talaba.fanga_yozil(math)
talaba.fanga_yozil(eng)
talaba.remove_fan(math)

prof = Professor("Hasan", "Fizika")
user = Foydalanuvchi("Bekzod", "bek123")
mijoz = Mijoz("Jasmin", 50000)
admin = Admin("Admin", "root")

admin.ban_user()

print(talaba.get_info())
print(prof.get_info())
print(user.get_info())
print(mijoz.get_info())
print(admin.get_info())