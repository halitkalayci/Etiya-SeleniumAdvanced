print("Fonksiyonlar.")

print(500*0.20)
print(350*0.20)
print(1000*0.20)

# Tekrar kullanılabilecek satırları bir kere yazıp (fonk. haline getirmek)
# bu fonksiyonu çağırmak.

# required arguments
# optional arguments

# kullanıcı 2. argüman geçerse onu dikkate al, geçmezse 0.2 olarak varsayılan değer al.
def calculate_tax(price, rate = 0.2):
    tax = price * rate
    return tax # çağırıldığı noktaya bu değeri dönecek.

tax1 = calculate_tax(500)
print(tax1)

tax2 = calculate_tax(300, 0.1)
print(f"Tax2+300: {tax2+300}")

tax3 = calculate_tax(400)


tax4 = calculate_tax(200)


print("**************")
import os # built-in
import requests # third-party

#import mathematich

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
#os.mkdir("deneme")


# alias
from mathematich import add as ekle # math. modülünden yalnızca addi import eder. add'i ekle ismiyle kullan.
print(ekle(1,2))

import mathematich #bütün mathematich modülünü import eder.
print(mathematich.add(1,2))
ekle(5,10)