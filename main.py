# Değişkenler
# Tanımlandıktan sonra programda kullanılacak isimlendirilmiş veriler.

print(10) #statik

price = 500 # değişken tanımıdır. 
# 6. satırdan itibaren price ismine 500 değerini atadım.
print(price)

price = 600 #Tip-güvenli değil!
print(price)
#
print(type(price)) 
# integer => tam sayı
# str,string => metinsel ifade
# float,double,decimal => ondalıklı sayı
# bool,boolean => true-false
price2 = "Merhaba"
price2 = 100
price3 = 50 
print(type(price2))
print(type(price3))

# Harf veya _ ile başlamalı
# Sayı içerebilir ama sayı ile başlayamaz.
# Büyük-küçük harf duyarlıdır
# Türkçe karakter içermemelidir.
name = "Halit"
Name = "Halit"

title = "Etiya Homepage"#......


# Operatörler 

# Matematiksel (Aritmetik Operatörler)
print(1 + 1) 
print(5 - 2)
print(5 * 5)
print(31 / 4) # Sonuç float
print(31 // 4) # Sonucu int olarak istiyorsak (her zaman aşağı yuvarlama.)
print(100 % 3) # Mod 
print(5 ** 2) #Üs alma
#

# boolean, bool -> True,False
isActive = False
# Karşılaştırma Operatörleri
print(1 == 1) # Değer karşılaştırma -> İki taraf aynı mı?
print(1 == 2)
print(1 != 2) # İki taraf farklı mı?

faturaBedeli = 100
print(faturaBedeli > 50)
print(50 < 100)
print(150 >= 50)
print(50 <= 50)
#

# Atama Operatörleri

a = 5 #atama
a += 3 # a+3 
print(a)
a *= 3
print(a)
a //= 3
print(a)
#


# Mantıksal Operatöler
# and-or
ogrenci = True
yas = 18

print(ogrenci == True and yas >= 20) # and -> true-true 
print(ogrenci == True or yas >= 20) # or -> iki koşuldan bir tanesinin true olması yeterli

# and her zaman önceliklidir (parantez yoksa)
print(True and True or False and True)
#