import os
import time

''' Работаем в текущей директории'''
directory = os.getcwd()
print ("Текущая директоия:", directory)

'''Сделаем папку 'First', сначало проверим её наличие '''
if os.path.exists ('First'):
    os.chdir('First')
else:
    os.mkdir('First')
    os.chdir('First')
    '''Добавим еще папки'''
    os.makedirs(r'Second\Third\Fourth\Fifth\Sixth')


'''
1. Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
2. Примените os.path.join для формирования полного пути к файлам.
3. Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
4. Используйте os.path.getsize для получения размера файла.
5. Используйте os.path.dirname для получения родительской директории файла.
'''

# Обходим директорию и все её поддиректории
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время в удобный вид
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(
            f"Обнаружен файл: {file}, "
            f"Путь: {filepath}, "
            f"Размер: {filesize} байт, "
            f"Время изменения: {formatted_time}, "
            f"Родительская директория: {parent_dir}"
        )







