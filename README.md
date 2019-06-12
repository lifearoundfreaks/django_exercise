# Использование Django Framework

Данный проект является демонстрацией использования Django Framework для создания веб-приложений, работы с базами данных и использования различных технологий (**jQuery**, **ajax**, **Rest Framework**, etc) на данной платформе. В качестве техзадания использовалось тестовое задание [abz.agency](https://abz.agency/). Оно приложено в проекте (*assignment.pdf*).

## Установка

Клонируйте данный репозиторий, установите зависимости с помощью:

```bash
pip install -r requirements.txt
```

Используйте стандартную команду Django для запуска приложения:

```bash
python manage.py runserver
```

## Database seeding

В данном проекте демонстрируется метод "засеивания" базы данных (database seeding) с помощью миграции. Процесс засеивания помещает более 50 тысяч объектов в датабазу, что может занять около 15-20 минут. При написании данной процедуры её эффективность не ставилась целью, поскольку она необходима лишь для демонстрации работы с большими объемами структурированных данных.

По этой причине проект включает в себя уже "засеянный" файл базы данных. Ниже описана последовательность действий, если возникнет потребность засеять базу данных "с нуля":

1. Удалите файл базы данных *db.sqlite3*
2. Используйте команду ```python manage.py migrate``` для засеивания
3. Дождитесь окончания засеивания (15-20 минут)

## Особенности проекта

Это учебный проект для демонстрации в резюме. Он ставит целью продемонстрировать работу с:
- Моделями Django и их полями
- Шаблоном **Model-View-Controller**
- Использованием ORM для работы с базами данных
- Полями, содержащими ссылки на объекты (**ForeignKey**)
- Построением иерархии сотрудников с помощью вложенных объектов
- Миграциями баз данных
- **Bootstrap** и его кастомизацией с помощью стилей и **Javascript**
- **jQuery** (получение значений **html** элементов, отправка **ajax**-запросов)
- **Django QuerySet** (фильтрация, сортировка, исключение) и сортировкой по полям вложенных объектов
- **ajax** для получения данных без обновления страницы
- Пользователями и ограничением доступа к разделам сайта
- Объектами базы данных с клиентской стороны (редактирование, добавление, удаление)
- Загружаемыми файлами (фотографии пользователей)
- Процедурной генерацией страницы (дерево сотрудников)
- Использованием drag-n-drop для выполнения действий на странице

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)