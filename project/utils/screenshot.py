def take_screenshot(driver, name="screenshot"):
    import os 
    from datetime import datetime
    # Her çalıştırmada o günün tarihinin bir klasörü oluşsun, içerisine ssler atılsın.
    date_folder_name = "screenshots\\"+datetime.now().strftime("%d-%m-%Y")
    # 07.08.2025T13:20
    os.makedirs(date_folder_name, exist_ok=True)

    time_stamp = datetime.now().strftime("%H-%M-%S")
    file_name = f"{name}_{time_stamp}_{datetime.now().microsecond}.png"

    file_path = "project/"+os.path.join(date_folder_name, file_name)
    
    driver.save_screenshot(file_path)
    return file_path
