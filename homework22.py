# 1
import datetime as dt

bugun = dt.date.today()

ramazon = dt.date(2026, 1, 17)
qurbon = dt.date(2026, 3, 27)
farq=ramazon-bugun
farq1=qurbon-bugun
print(f"Ramazonga  {farq.days }  kun qoldi")
print("Qurbon hayitigacha {farq1.days} kun qoldi")
# 2
import datetime as dt

start = dt.date.today()

for i in range(10):
    sana = start + dt.timedelta(weeks=2 * i)
    print(sana)
# 3
import datetime as dt

bugun = dt.date.today()

print(bugun.year)
print(bugun.month)
print(bugun.day)
tyil= dt.date(2006, 4, 8)
farq=bugun-tyil
print(f"Tug'ulgan kunimdan keyin  {farq.days }  kun o'tkan")

# 4

import re

tel1 = "998887360804"
tel2 = "998880740804"
tel3 = "998701073204"

andoza = "^998........4"

print(re.match(andoza, tel1))
print(re.match(andoza, tel2))
print(re.match(andoza, tel3))
# 5
