# Тестовое задание Supl.biz 
## "Работа с основными компонентами Django"

### Описание задания

Необходимо создать Django­проект для работы с базой Заказчиков и Поставщиков. 
Сущности реализовать с помощью моделей Django.
СУБД - любая. 

Django >= 1.7 

Python >= 2.7

Django модели:  

|Название модели |  Поля |
| --- | --- |
| Регион  | Название региона |
Заказчик |  Название компании, Регионы | 
Поставщик | Название компании, Регионы |

На главной странице должно располагаться поле ввода. 
 
После ввода названия компании-заказчика в это поле и отправки данных на сервер на 
странице должны отображаться названия компаний-поставщиков, регионы которых 
пересекаются с регионами указанной компании-заказчика. 
 
Названия компаний-поставщиков должны быть оформлены как ссылки. Ссылки 
должны вести на личную страницу поставщика, на которой должны быть указаны 
название компании и ее регионы.

### Запуск проекта

Для запуска тестового Django-проекта выполните следующие шаги:

1. Склонируйте Git-репозиторий проекта командой:

   $ git clone https://github.com/MarinaMeyta/suplbiz_test_task.git

   Либо загрузите zip-архив на главной странице проекта и распакуйте в рабочую директорию командой:
   
   $ unzip suplbiz\_test\_task.zip

   Далее перейдите в директорию проекта:
   
   $ cd suplbiz\_test\_task

2. Cоздайте командой virtualenv виртуальную оболочку, где suplbizenv - название виртуальной оболочки:

   $ virtualenv --python=python2.7 suplbizenv

   Для ее активации используйте команду:
   
   $ source suplbizenv/bin/activate

   Для деактивации виртуальной оболочки необходимо набрать в командной строке команду:
   
   $ deactivate

3. После активации виртуальной оболочки установите необходимые пакеты из файла requirements.txt:

   $ pip install -r requirements.txt
   
4. Создание базы данных поставщиков, заказчиков и регионов (по умолчанию СУБД SQLite):

   $ python manage.py makemigrations
   
   $ python manage.py migrate

   Добавить сущности в БД можно, запустив shell и прописав Python команды на добавление поставщиков, заказчиков и регионов:

   $ python manage.py shell
   
   Скрипт, приведенный ниже, добавит 2 региона ("Tomsk" и "Moskow") и провайдера "company_p1", работающего в этих регионах.

```python
from suplbizapp.models import Region
from suplbizapp.models import Client
from suplbizapp.models import Provider
r1 = Region(region_name="Tomsk")
r1.save()
r2 = Region(region_name="Moskow")
r2.save()
p1 = Provider(company_name="company_p1")
p1.save()
p1.regions.add(r1, r2)
p1.regions.all()
```
