import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

descriptions = []
for offer_elem in root.iter('offer'):
    description_elem = offer_elem.find('.//description')
    if description_elem is not None:
        description = description_elem.text
    else:
        description = "null"
    descriptions.append([description])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_descriptions.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['description'])  # Записываем заголовок

    # Записываем каждое описание в отдельную строку
    for description in descriptions:
        writer.writerow(description)

print("Данные успешно сохранены в файл offer_descriptions.csv")