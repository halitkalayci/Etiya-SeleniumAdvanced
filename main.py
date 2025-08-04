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

# Scope Kavramı -> {}
# Kullanıcı çekmek istediği tutar hesabında varsa X yoksa Y işlemi.

# 1 tab -> 1 indent içeri (sağ)
# shift+tab -> 1 indent dışarı (sol)
ogrenci = False
if ogrenci == True:
    print("Kisi ogrenci")
else:
    print("Kisi ogrenci degil")
print("Blok disi")


note = 75
#elseif
# Her koşul bloğu yalnızca 1 adet koşulu çalıştırır.
if note >= 80:
    print("AA")
elif note >= 70: # bu koşul sağlanmıyor ama bu sağlanıyorsa
    print("BB")
elif note >= 60:
    print("CC")
elif note >= 50:
    print("DD")
else: # yukarıdaki koşulların hiç biri sağlanmıyorsa.
    print("FF")


# Eğer fatura tarihi geçmişse hesabı dondur.
faturaOdenmedi = True
onGunGecti = False
if faturaOdenmedi:
    print("Fatura ödenmedi işlemler yapılıyor..")
    if onGunGecti:
        print("Hesap donduruluyor.")
    else:
        print("Hatırlatma mesajı atılıyor.")


# aynı scopedaki kodu N adet tekrarlayarak çalıştırma -> Döngüler

# index => i
# i=0 dan başlayan bir sayı, sen bunu 10'a kadar (dahil değil) artırarak her artırma sonrası
# scope'u çalıştır.
for i in range(10):
    print(i) # 10 kere çalıştı.

#