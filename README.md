# Django REST приложение для отслеживания контактирующих
 
Реализовано API следующих функций:
1) CRUD - создание, просмотр, изменение и удаление клиентов и сотрудников
2) Метод добавления новых связей между клиентами и сотрудниками
3) Метод, получающий на вход две даты, возвращающий csv-файл со списком
контактов сотрудников с клиентами в промежуток времени между заданными датами
(строка отчета содержит инфу о сотруднике, дату контактирования и инфу о клиенте)

##Стек
 
Python 3, Django 3.0.5, Django REST Framework, SQLite3, GIT


## Установка 
Клонируем репозиторий на локальную машину: ```$ git clone https://github.com/DariaKalinichenko/employee-contacts```

Создаем виртуальное окружение:  ```$ python -m venv venv```

Устанавливаем зависимости: ```$ pip install -r requirements.txt```

Создание и применение миграций: ```$ python manage.py makemigrations``` и ```$ python manage.py migrate```

Создадим суперпользователя: ```python manage.py createsuperuser```

Запускаем django сервер: ```$ python manage.py runserver```

Адрес API: http://localhost:8000/api/v1/

##Подробная документация методов API c примерами команд:

http://localhost:8000/swagger/

## Несколько примеров использования API
Что бы получить отчет, содержащий информацию о сотруднике, дату контактирования и инфо о клиенте, следует в параметрах 
get запроса передать 'date_after' и 'date_before'. Форматы даты - YYYY-MM-DD

**GET /api/v1/contact/?date_after=2020-12-14&date_before=2020-12-19**

Для вывода данной информации в CSV-файл нужно сделать всё то же самое, используя endpoint 'csv':

**GET /api/v1/csv/?date_after=2020-12-14&date_before=2020-12-19**


**Пример отчета можно посмотреть в файле Пример_вывода.csv**