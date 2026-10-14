## backend

Holds all the backend files.
Dev Environment Setup: 
uv
Django 6.0.3.
Python 3.14.2

Start Django app: 
uv run python manage.py runserver

Compile Finnish and English translations after changing translation catalogs or
before starting the app from a fresh checkout:

```powershell
uv run python manage.py compilemessages
```
