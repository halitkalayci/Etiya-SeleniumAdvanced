class Car():
    # constructor -> yapıcı blok -> her instance üretildiği anda çağırılan fonk.
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year  = year
        self.color = color
        print("Bir arac olusturuldu.")

    # self -> Fonksiyonlara classın kendi içindeki yapılara erişebilmesi için. Rezerve 1 parametre geçilir.
    def start(self):
        print(f"{self.brand} marka arac baslatiliyor.")

    def stop(self):
        print("Araç durduruluyor..")
    
    def increase_speed(self, speed): #Klasik fonk. parametrelerini almaya devam edebiliriz.
        print(f"Hiz artiriliyor. {speed}")

# Inheritance (kalıtım) - extends
class ElectricCar(Car): # ElectricCar - Car -> Miras aldığım class => superclass, Miras alan class => subclass
    def __init__(self, brand, year, color, batarya):
        super().__init__(brand, year, color)
        self.batarya = batarya

car = Car("Toyota",2025,"Kırmızı") #Instance üretmek.
car.start()
car.stop()
car.increase_speed(100)

electric_car = ElectricCar("Tesla",2025,"Beyaz","500Mah")