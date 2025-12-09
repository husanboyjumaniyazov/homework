 # 1
import json
data = {
    "Model":"Malibu",
    "Rang":"Qora",
    "Yil": 2020,
    "Narhi":40000
}
data_json=json.dumps(data,indent=4 )
print(data_json)
print(type(data_json))
# 2
import json

talaba_json = """
{"ism":"Hasan", "familiya":"Husanov", "tyil":2000}"""

talaba = json.loads(talaba_json)

print("Ism:", talaba["ism"])
print("Familiya:", talaba["familiya"])
# 3
# 1-fayl: mashina.json
with open("mashina.json", "w") as f:
    json.dump(data, f)

# 2-fayl: talaba.json
with open("talaba.json", "w") as f:
    json.dump(talaba, f)

# 4
ucta_talaba_json ="""{"ism": "Ali", "familiya": "Olimov", "kurs": 1, "fakultet": "IT"},
    {"ism": "Barno", "familiya": "Alijonov", "kurs": 3, "fakultet": "Axborot"},
    {"ism": "Timur", "familiya": "G'anoyev", "kurs": 2, "fakultet": "Mexanika}"""
with open("ucta_talaba_json", "w") as f:
    json.dump(ucta_talaba_json, f)
