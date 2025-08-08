def take_screenshot(driver, name="screenshot"):
    import os
    from datetime import datetime

    # Proje dizininin tam yolunu al
    # CWD => Current Working Directory
    project_root = os.path.abspath(os.getcwd())

    # Her çalıştırmada o günün tarihinin bir klasörü oluşsun, içerisine ss'ler atılsın.
    date_folder_name = datetime.now().strftime("%d-%m-%Y")
    screenshots_dir = os.path.join(project_root, "screenshots", date_folder_name)
    os.makedirs(screenshots_dir, exist_ok=True)

    # Dosya adını oluştur
    time_stamp = datetime.now().strftime("%H-%M-%S")
    file_name = f"{name}_{time_stamp}_{datetime.now().microsecond}.png"

    # Tam dosya yolu
    file_path = os.path.join(screenshots_dir, file_name)

    # Screenshot al ve kaydet
    driver.save_screenshot(file_path)

    return file_path  # Zaten absolute path
