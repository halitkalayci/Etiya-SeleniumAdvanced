class Car:
    brand = ""
    year = 0
    color = ""

    # self -> Fonksiyonlara classın kendi içindeki yapılara erişebilmesi için. Rezerve 1 parametre geçilir.
    def start(self):
        print(f"{self.brand} marka arac baslatiliyor.")

    def stop(self):
        print("Araç durduruluyor..")
    
    def increase_speed(self, speed): #Klasik fonk. parametrelerini almaya devam edebiliriz.
        print(f"Hiz artiriliyor. {speed}")


car = Car() #Instance üretmek.
car.brand = "Toyota"
car.year = 2025
car.color = "Beyaz"
car.start()
car.stop()
car.increase_speed(100)