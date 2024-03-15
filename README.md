# Django Kits Store
A football soccer kits store backend made with Django

![Screenshot of the index page](/screenshots/index.png)

Additional Django's packages installed:
- crispy_forms
- crispy_boostrap5
- django-boostrap5

## How to run
NOTE: This project was developed in Linux, so the following instructions may vary if you're running another OS.

First you need to activate de Python virtual enviroment. From the project directory, type:
```
source django-kits-store-env/bin/activate
```

Next, install the dependencies
```
pip install -r requirements.txt
```

Then, run the server
```
python kitsStore/manage.py runserver
```

## Miscellaneous
Dump data is provided.
To load the dump data for the Category model, type:
```
python kitsStore/manage.py loaddata kitsStore/kits_management/fixtures/Category.json
```

To load the dump data for the Team model, type:
```
python kitsStore/manage.py loaddata kitsStore/kits_management/fixtures/Team.json
```

To load the dump data for the Kit model, type:
```
python kitsStore/manage.py loaddata kitsStore/kits_management/fixtures/Kit.json
```

## Credits
Project made by David López for the Django course at the 4° Escuela de Actualización en Tecnologías de Informática (2024)
Universidad Nacional del Sur
Bahía Blanca, Buenos Aires, Argentina 🇦🇷
