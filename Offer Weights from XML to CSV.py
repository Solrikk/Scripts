import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

weights = []
for offer_elem in root.iter('offer'):
    weight_elem = offer_elem.find('.//weight')
    if weight_elem is not None:
        weight = weight_elem.text
    else:
        weight = "null"
    weights.append([weight])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_weights.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['weight'])  # Записываем заголовок

    # Записываем каждый вес в отдельную строку
    for weight in weights:
        writer.writerow(weight)

print("Данные успешно сохранены в файл offer_weights.csv")