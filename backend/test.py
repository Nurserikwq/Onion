import yaml
from pprint import pprint

# Укажите имя вашего YAML файла
file_path = r'C:\Users\Nurserik\Desktop\trash\КЖК Q&A.yml'

try:
    # --- ИЗМЕНЕНИЕ ЗДЕСЬ: добавляем encoding='utf-8' ---
    with open(file_path, 'r', encoding='utf-8') as file:
        # Загружаем содержимое YAML с помощью safe_load()
        data = yaml.safe_load(file)

    # Теперь data — это словарь Python, который можно использовать:
    print("Содержимое YAML, загруженное как словарь Python:")
    pprint(data)

    # ВНИМАНИЕ: Следующие строки могут вызвать ошибку KeyError,
    # если в вашем файле 'КЖК Q&A.yml' нет ключей 'database' и 'app'.
    # Я их закомментирую, предполагая, что ваш файл имеет другую структуру.

    # db_host = data['database']['host']
    # app_version = data['app']['version']

    # print(f"\nХост базы данных: {db_host}")
    # print(f"Версия приложения: {app_version}")

except FileNotFoundError:
    print(f"Ошибка: файл '{file_path}' не найден.")
except yaml.YAMLError as exc:
    print(f"Ошибка при парсинге YAML: {exc}")
except Exception as e:
    # Дополнительно добавим отлов других ошибок, например, KeyError,
    # если структура файла не соответствует ожидаемой.
    print(f"Произошла другая ошибка: {e}")