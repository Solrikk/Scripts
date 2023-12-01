import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

manufacturers = []
for offer_elem in root.iter('offer'):
    manufacturer_elem = offer_elem.find('.//vendor')
    if manufacturer_elem is not None:
        manufacturer = manufacturer_elem.text
    else:
        manufacturer = "null"
    manufacturers.append([manufacturer])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_manufacturers.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['manufacturer'])  # Записываем заголовок

    # Записываем каждого производителя в отдельную строку
    for manufacturer in manufacturers:
        writer.writerow(manufacturer)

print("Данные успешно сохранены в файл offer_manufacturers.csv")