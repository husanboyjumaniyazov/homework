# # 1
# class Product:
#     def __init__(self, id, nomi, narx, soni, rating):
#         self.id = id
#         self.nomi = nomi
#         self.narx = narx
#         self.soni = soni
#         self.rating = rating
#
#     def info(self):
#         print(f"ID: {self.id}, Nomi: {self.nomi}, Narxi: {self.narx} so'm, "
#               f"Omborda: {self.soni} dona, Rating: {self.rating}")
#
#     def update_price(self, yangi_narx):
#         self.narx = yangi_narx
#         print(f"{self.nomi} narxi yangilandi: {yangi_narx} so'm")

# 2
class Product:
    def __init__(self, nomi, narx, soni):
        self.nomi = nomi
        self.narx = narx
        self.soni = soni

class Cart:
    def __init__(self):
        self.mahsulotlar = []
        self.umumiy_narx = 0

    def add_product(self, product):
        self.mahsulotlar.append(product)
        self.calculate_total()
        print(f"{product.nomi} savatga qo'shildi.")

    def remove_product(self, product_id):
        for p in self.mahsulotlar:
            if p.id == product_id:
                self.mahsulotlar.remove(p)
                self.calculate_total()
                print(f"{p.nomi} savatdan olib tashlandi.")
                return
        print("Mahsulot topilmadi!")

    def clear(self):
        self.mahsulotlar.clear()
        self.umumiy_narx = 0
        print("Savat tozalandi.")

    def calculate_total(self):
        self.umumiy_narx = sum(p.narx for p in self.mahsulotlar)
        return self.umumiy_narx

    def is_empty(self):
        return len(self.mahsulotlar) == 0

# 3
from datetime import datetime
class Order:
    def __init__(self, id, cart):
        self.id = id
class Order:
    def __init__(self, id, cart):
        self.id = id
        self.status = "Yaratildi"
        self.cart = cart
        self.yaratilgan_vaqt = datetime.now()
        self.jami_narx = cart.calculate_total()

    def confirm(self):
        self.status = "Tasdiqlandi"
        print(f"Buyurtma #{self.id} tasdiqlandi!")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Buyurtma {self.id} status yangilandi: {new_status}")

    def info(self):
        print(f"Buyurtma ID: {self.id}")
        print(f"Status: {self.status}")
        print(f"Yaratilgan vaqt: {self.yaratilgan_vaqt}")
        print(f"Jami: {self.jami_narx} so'm")
        print("Mahsulotlar:")
        for p in self.cart.mahsulotlar:
            print(f" - {p.nomi} ({p.narx} so'm)")
# 4
class Customer:
    def __init__(self, id, ism, email):
        self.id = id
        self.ism = ism
        self.email = email
        self.savat = Cart()
        self.buyurtmalar = []

    def add_to_cart(self, product):
        self.savat.add_product(product)

    def remove_from_cart(self, product_id):
        self.savat.remove_product(product_id)

    def create_order(self):
        if self.savat.is_empty():
            print("Savat bo'sh! Buyurtma yaratilmaydi.")
            return

        new_order = Order(len(self.buyurtmalar) + 1, self.savat)
        self.buyurtmalar.append(new_order)
        self.savat = Cart()  # savatni yangidan ochish
        print(f"{self.ism} uchun buyurtma yaratildi (#{new_order.id}).")
        return new_order

    def show_orders(self):
        if not self.buyurtmalar:
            print("Buyurtmalar tarixi bo'sh.")
            return

        for order in self.buyurtmalar:
            order.info()
            print("-" * 40)
# 5
class Store:
    def __init__(self, nomi):
        self.nomi = nomi
        self.mahsulotlar = []
        self.foydalanuvchilar = []

    def add_product(self, product):
        self.mahsulotlar.append(product)
        print(f"{product.nomi} do'konga qo'shildi.")

    def register_user(self, customer):
        self.foydalanuvchilar.append(customer)
        print(f"{customer.ism} ro'yxatga olindi.")

    def search_product(self, nomi):
        for p in self.mahsulotlar:
            if p.nomi.lower() == nomi.lower():
                return p
        return None

    def top_rated_products(self):
        sorted_products = sorted(self.mahsulotlar, key=lambda p: p.rating, reverse=True)
        print("Eng yuqori ratingli mahsulotlar:")
        for p in sorted_products[:5]:
            p.info()

    def sold_report(self):
        print("Sotilgan mahsulotlar hisoboti:")
        for user in self.foydalanuvchilar:
            for order in user.buyurtmalar:
                for p in order.cart.mahsulotlar:
                    print(f"{p.nomi} — {p.narx} so'm")