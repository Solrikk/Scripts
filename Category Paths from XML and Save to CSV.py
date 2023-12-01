import xml.etree.ElementTree as ET
import requests
import os
import csv

def save_to_csv(category_paths):
    file_path = os.path.join(r'C:\Users\Solrikk\Downloads\Doki', 'category_paths.csv')
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Category Path'])
        for category_path in category_paths:
            writer.writerow([category_path])

def get_category_path(offer_ids):
    xml_file = 'https://armos-market.ru/feeds/yandex.xml'
    response = requests.get(xml_file)
    xml_data = response.text

    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    paths = []

    for offer_id in offer_ids:
        path = []
        category = None

        for offer_elem in root.findall('.//offer'):
            if offer_elem.attrib['id'] == offer_id:
                category_id = offer_elem.find('.//categoryId').text
                break

        for category_elem in root.findall('.//category'):
            if category_elem.attrib['id'] == category_id:
                category = category_elem
                break

        if category is not None:
            while category is not None:
                path.insert(0, category.text)
                parent_id = category.attrib.get('parentId')
                category = None
                for category_elem in root.findall('.//category'):
                    if category_elem.attrib['id'] == parent_id:
                        category = category_elem
                        break

        paths.append('/'.join(path))

    return paths

offer_ids = ["279451", "279453", "279440", "279442"]

category_paths = get_category_path(offer_ids)
save_to_csv(category_paths)