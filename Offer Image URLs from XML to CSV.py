import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

image_urls = []
for offer_elem in root.iter('offer'):
    image_elem = offer_elem.find('.//picture')
    if image_elem is not None:
        image_url = image_elem.text
    else:
        image_url = "null"
    image_urls.append([image_url])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_image_urls.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_url'])  # Записываем заголовок

    # Записываем каждую ссылку на изображение в отдельную строку
    for image_url in image_urls:
        writer.writerow(image_url)

print("Данные успешно сохранены в файл offer_image_urls.csv")