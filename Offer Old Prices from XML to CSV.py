import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

prices = []
for offer_elem in root.iter('offer'):
    old_price_elem = offer_elem.find('.//oldprice')
    if old_price_elem is not None:
        old_price = old_price_elem.text
    else:
        old_price = "null"
    prices.append([old_price])

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

# Полный путь к файлу
file_path = os.path.join(save_path, 'offer_old_prices.csv')

# Сохраняем данные в CSV файл
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['old_price'])  # Записываем заголовок

    # Записываем каждую старую цену в отдельную строку
    for price in prices:
        writer.writerow(price)

print("Данные успешно сохранены в файл offer_old_prices.csv")