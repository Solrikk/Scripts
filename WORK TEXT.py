import pandas as pd

# Загрузить файл Excel с описанием
data = pd.read_excel(r'C:\Users\Solrikk\Downloads\Doki\fileess.xlsx')

# Заменить переносы строк на тег <br>
data['Описание'] = data['Описание'].str.replace('\n', '<br>')

# Обработать каждый абзац в столбце 'Описание'
data['Описание'] = '<p>' + data['Описание'] + '</p>'

# Сохранить изменения в файле Excel
data.to_excel(r'C:\Users\Solrikk\Downloads\Doki\fileess123.xlsx', index=False)