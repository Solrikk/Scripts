import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

vendors = []
for offer_elem in root.findall('.//offer'):
    vendor = offer_elem.find('.//vendor').text
    if vendor is not None:
        vendors.append(vendor)

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_vendors.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['vendor'])  # Записываем заголовок

    # Записываем каждый vendor в отдельную строку
    for vendor in vendors:
        writer.writerow([vendor])

print("Данные успешно сохранены в файл offer_vendors.csv")