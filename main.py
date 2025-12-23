def qavslarni_tekshir(matn):
    stek = []
    juftlar = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for belgi in matn:
        if belgi in '([{':
            stek.append(belgi)
        elif belgi in ')]}':
            if not stek or stek.pop() != juftlar[belgi]:
                return False
    
    return len(stek) == 0


# Test misollar
test_misollar = [
    "([we]}",
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((()))",
    "(()",
    "hello(world)",
    "{a[b(c)d]e}",
    "",
]

# Natijalarni chiqarish
print("=" * 50)
print("QAVSLARNI TEKSHIRISH DASTURI")
print("=" * 50)
print()

for matn in test_misollar:
    natija = qavslarni_tekshir(matn)
    holat = "✓ To'g'ri" if natija else "✗ Noto'g'ri"
    print(f"{matn:20s} → {holat}")

print("\n" + "=" * 50)

# Foydalanuvchidan kiritish
print("\nO'zingizning matnni kiriting:")
foydalanuvchi_matni = input("Matn: ")
natija = qavslarni_tekshir(foydalanuvchi_matni)

if natija:
    print("✓ Qavslar to'g'ri ochilgan va yopilgan!")
else:
    print("✗ Qavslar noto'g'ri!")
