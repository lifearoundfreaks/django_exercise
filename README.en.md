# Django Framework usage

This project is a demo of making web-applications, working with databases and using various technologies (**jQuery**, **ajax**, **Rest Framework**, etc) with Django Framework. As a technical assignment, I used a test assignment provided by [abz.agency](https://abz.agency/). It's attached as [assignment.pdf](assignment.pdf) but sadly, no translation is provided.

## Installation

Clone this repository and install dependencies with:

```bash
pip install -r requirements.txt
```

Use a standard Django command for starting a server:

```bash
python manage.py runserver
```

Superuser account (if you are using unchanged database):
```bash
login: super
password: super
```
## Database seeding

This project shows usage of migrations as a database seeding method. The migration will put more than 50 thousand objects inside a database and this process might take from 15 to 20 minutes. It wasn't my goal to make this process efficient but to use it for a demonstration of working with large amounts of structured data instead.

That's why database file is already included in this repository. Here's how you can seed a database "anew" by using my method:

1. Delete a database file *db.sqlite3*
2. Use ```python manage.py migrate``` for seeding
3. Wait till seeding process is complete (15-20 minutes)

## Project features

This is an exercise project for resume display. It shows how to work with:
- Django models and model fields
- **Model-View-Controller** pattern
- ORM while working with databases
- Fields containing links to other objects (**ForeignKey**)
- Enterprise hierarchy with the help of nested objects
- Database migrations
- **Bootstrap** and its customisation using **CSS** and **Javascript**
- **jQuery** (for getting a value of **html** elements, sending **ajax**-queries)
- **Django QuerySet** (filter, order_by, exclude) and nested object field sorting
- **ajax** to get data without updating a page
- Users and limiting access to various parts of a website
- Database objects via client-side use (editing, creating, removing)
- Uploaded files (employee photos)
- Procedural page loading (employee tree)
- Using drag-n-drop to perform actions on the page

## License
[MIT](https://choosealicense.com/licenses/mit/)
