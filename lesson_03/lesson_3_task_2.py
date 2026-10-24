# lesson_3_task_2.py
from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79111112233"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79222223344"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79333334455"))
catalog.append(Smartphone("Google", "Pixel 8", "+79444445566"))
catalog.append(Smartphone("Huawei", "Pura 70", "+79555556677"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
