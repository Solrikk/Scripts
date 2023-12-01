numbers = """



"""

formatted_numbers = ', '.join(['"{}"'.format(number.strip()) for number in numbers.split('\n') if number.strip()])

file_path = r'C:\Users\Solrikk\Downloads\Doki\output.txt'  # Полный путь к файлу, куда будут записаны данные

with open(file_path, 'w') as file:
    file.write(formatted_numbers)

print("Данные успешно записаны в файл 'output.txt'.")