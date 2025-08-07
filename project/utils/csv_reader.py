import csv

def read_csv_data(file_path):
    # with -> Bağlam Yöneticisi (Context Manager)
    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # 1. satır => başlıklar
        #list = []
        #for row in reader:
            #list.append(row)
        #return list
        return [row for row in reader]
    
def read_csv_data2(file_path):
    # Eğer bir hata try-except ile sarmallanmışsa o hata programı durdurmaz.
    # Handled-Exception
    dosya = open("data/login_invalid_credentials.csv", "r")
    try:
        icerik = dosya.read()
    except:
        print("Dosya okumada hata.")
    finally:
        dosya.close()
        print("Hata verse de vermese de çalışacak blok")