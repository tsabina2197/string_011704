# 31. Faqat harflardan iborat bo'lsa, katta harflarga o'tkazish
matnlar31 = ["hello", "python123", "salom", "world!", "uzbek"]
result31 = list(map(lambda x: x.upper() if x.isalpha() else x, matnlar31))
print("31:", result31)

# 32. Faqat raqamli matnni 8 xonali qilib, oldidan nol bilan to'ldirish
matnlar32 = ["1234", "567", "987654", "42"]
result32 = list(map(lambda x: x.zfill(8) if x.isdigit() else x, matnlar32))
print("32:", result32)

# 33. Har bir so'zning bosh harfini katta qilish (Title case)
matnlar33 = ["python string metodlari", "men python o'rganaman", "hello world"]
result33 = list(map(lambda x: x.title(), matnlar33))
print("33:", result33)

# 34. Aralash harfli matnni faqat kichik harflarga aylantirish
matnlar34 = ["PyThOn", "JaVaScript", "PyTHoN"]
result34 = list(map(str.lower, matnlar34))
print("34:", result34)

# 35. Aralash harfli matnni faqat katta harflarga aylantirish
matnlar35 = ["PyThOn", "JaVaScript", "PyTHoN"]
result35 = list(map(str.upper, matnlar35))
print("35:", result35)

# 36. Bo'shliq bilan ajratilgan matnni "-" bilan birlashtirish
matnlar36 = ["men python o'rganaman", "hello world python"]
result36 = list(map(lambda x: '-'.join(x.split()), matnlar36))
print("36:", result36)

# 37. Eng ko'p takrorlangan harfni topish
def most_common_letter(s):
    s = s.lower().replace(" ", "")
    return max(s, key=s.count) if s else ""
    
matnlar37 = ["banana", "python", "mississippi", "level"]
result37 = list(map(most_common_letter, matnlar37))
print("37:", result37)

# 38. Matndan faqat harflarni qoldirish (raqamlarni olib tashlash)
matnlar38 = ["py3th0n9", "hello123world", "uzbek2024"]
result38 = list(map(lambda x: ''.join(c for c in x if c.isalpha()), matnlar38))
print("38:", result38)

# 39. Matn palindrom ekanligini tekshirish
matnlar39 = ["level", "python", "radar", "hello"]
result39 = list(map(lambda x: x.lower() == x.lower()[::-1], matnlar39))
print("39:", result39)

# 40. So'zlar tartibini teskari qilish va birlashtirish
matnlar40 = ["Men Python o'rganaman", "Hello world python"]
result40 = list(map(lambda x: ' '.join(x.split()[::-1]), matnlar40))
print("40:", result40)
