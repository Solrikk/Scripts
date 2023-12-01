import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

offer_ids = []
for offer_elem in root.findall('.//offer'):
    offer_id = offer_elem.attrib.get('id')
    if offer_id is not None:
        offer_ids.append(offer_id)

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_ids.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['offer_id'])  # Записываем заголовок

    # Записываем каждый offer_id в отдельную строку
    for offer_id in offer_ids:
        writer.writerow([offer_id])

print("Данные успешно сохранены в файл offer_ids.csv")