import requests
import xml.etree.ElementTree as ET
import csv

xml_url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(xml_url)
xml_data = response.text

root = ET.fromstring(xml_data)

offer_ids = ["306501", "292730", "292734", "292746", "292750", "292762", "292766", "311318", "309358", "309359", "309360", "309361", "309362", "309363", "309364", "309365"]
urls = []

for offer_id in offer_ids:
    offer_elem = root.find(".//offer[@id='{}']".format(offer_id))
    if offer_elem is not None:
        url_elem = offer_elem.find('url')
        if url_elem is not None:
            url = url_elem.text
            urls.append(url)
        else:
            print("Ссылка не найдена для оффера с идентификатором {}.".format(offer_id))
    else:
        print("Оффер с идентификатором {} не найден.".format(offer_id))

# Сохраняем список URL в CSV файл
file_path = r'C:\Users\Solrikk\Downloads\Doki\url.csv'
with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL'])
    for url in urls:
        writer.writerow([url])

print("Результаты сохранены в файл:", file_path)