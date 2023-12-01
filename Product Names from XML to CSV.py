import requests
import xml.etree.ElementTree as ET
import csv

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

offer_ids = ["306501", "292730", "292734", "292746", "10467", "297582", "297584", "297598", "297600", "297614", "297616", "297630", "297632", "297646"]
urls = []
product_names = []

for offer_id in offer_ids:
    offer_elem = root.find(".//offer[@id='{}']".format(offer_id))
    if offer_elem is not None:
        name_elem = offer_elem.find('name')
        if name_elem is not None:
            product_name = name_elem.text
            product_names.append(product_name)
        else:
            print("Название товара не найдено для оффера с идентификатором {}.".format(offer_id))
    else:
        print("Оффер с идентификатором {} не найден.".format(offer_id))

# Путь для сохранения файла
save_path = r'C:\Users\Solrikk\Downloads\Doki'
file_path = rf"{save_path}\product_names.csv"

# Сохраняем данные в CSV файл с кодировкой cp1251
with open(file_path, 'w', newline='', encoding='cp1251') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name'])  # Записываем заголовок

    # Записываем каждое название товара в отдельную строку
    for product_name in product_names:
        writer.writerow([product_name])

print("Данные успешно сохранены в файл product_names.csv")