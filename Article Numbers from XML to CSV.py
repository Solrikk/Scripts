import requests
import xml.etree.ElementTree as ET
import csv
import os

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

article_numbers = []
for offer_elem in root.iter('offer'):
    article_elem = offer_elem.find('.//vendorCode')
    if article_elem is not None:
        article_number = article_elem.text
    else:
        article_number = "null"
    article_numbers.append([article_number])

save_path = r'C:\Users\Solrikk\Downloads\Doki'
os.makedirs(save_path, exist_ok=True)

file_path = os.path.join(save_path, 'offer_article_numbers.csv')

with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['article_number'])  # Записываем заголовок

    for article_number in article_numbers:
        writer.writerow(article_number)

print("Данные успешно сохранены в файл offer_article_numbers.csv")