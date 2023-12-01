import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

heights = []
for offer_elem in root.iter('offer'):
    height_elem = offer_elem.find('.//height')
    if height_elem is not None:
        height = height_elem.text
    else:
        height = "null"
    heights.append([height])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_heights.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['height'])  # Записываем заголовок

    # Записываем каждую высоту в отдельную строку
    for height in heights:
        writer.writerow(height)

print("Данные успешно сохранены в файл offer_heights.csv")