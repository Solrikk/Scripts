import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

depths = []
for offer_elem in root.iter('offer'):
    depth_elem = offer_elem.find('.//depth')
    if depth_elem is not None:
        depth = depth_elem.text
    else:
        depth = "null"
    depths.append([depth])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_depths.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['depth'])  # Записываем заголовок

    # Записываем каждую глубину в отдельную строку
    for depth in depths:
        writer.writerow(depth)

print("Данные успешно сохранены в файл offer_depths.csv")