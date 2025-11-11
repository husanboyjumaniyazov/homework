
#1-savol: add() — Setga element qo‘shish
#1
a = {1, 2}
a.add(3)
print(a)
#2
a = {"apple", "banana"}
a.add("cherry")
print(a)

# 2-savol: discard() — Elementni o‘chirish (xatosiz)
#1
a = {1, 2, 3}
a.discard(2)
print(a)
#2
a = {10, 20, 30}
a.discard(100)
print(a)

#3-savol: remove() — Elementni o‘chirish (xato bo‘lishi mumkin)
#1
a = {1, 2, 3}
a.remove(2)
print(a)


#4-savol: intersection() — Umumiy elementlar
#1
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))
#2
a = {"a", "b", "c"}
b = {"b", "d"}
print(a & b)

# 5-savol: symmetric_difference() — Faqat birida borlar

a = {1, 2, 3}
b = {3, 4}
print(a.symmetric_difference(b))

a = {"a", "b"}
b = {"b", "c"}
print(a ^ b)

#6-savol: issubset() — Ichida bo‘lishini tekshirish
#1
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))
#2
a = {5}
b = {1, 2, 3}
print(a <= b)
# 7-savol: pop() — Tasodifiy element o‘chirish
#1
a = {10, 20, 30}
x = a.pop()
print(a, x)
#2
a = {"apple", "banana"}
x = a.pop()
print(a, x)
#8-savol: update() — Setni kengaytirish
#1
a = {1, 2}
b = {2, 3}
a.update(b)
print(a)
#2
a = {"a"}
a.update(["b", "c"])
print(a)
# 9-savol: difference() — Faqat 1-setda borlar
#1
a = {1, 2, 3}
b = {3, 4, 5}
print(a.difference(b))
#2
a = {"a", "b", "c"}
b = {"b"}
print(a - b)

# 10-savol: difference_update() — Farqni setga qo‘llash
#1
a = {1, 2, 3}
b = {3, 4, 5}
a.difference_update(b)
print(a)
#2
a = {"x", "y", "z"}
b = {"y"}
a -= b
print(a)



