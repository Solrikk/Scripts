import requests
import os

url = 'https://armos-market.ru/feeds/yandex.xml'
response = requests.get(url)
xml_data = response.text

save_path = r'C:\Users\Solrikk\Downloads\Doki\process-work'
file_path = os.path.join(save_path, 'yandex.xml')

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(xml_data)

print("Файл успешно сохранен в", file_path)