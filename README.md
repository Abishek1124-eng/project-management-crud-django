# Product Management CRUD

A Django web application for managing products through a simple CRUD interface. Products can be registered, viewed, updated, and deleted, with support for product images and availability status.

## Features

- Create products with name, category, brand, price, quantity, description, date, availability, and image
- View products ordered from newest to oldest
- Update product details and replace product images
- Delete products with a confirmation page
- Store uploaded images under `media/images/`
- Responsive glassmorphism-style interface
- Django admin support

## Tech stack

- Python
- Django 6.1
- PostgreSQL
- Pillow for image uploads
- HTML and CSS
- Three.js and Vanta.js for the animated landing-page background

## Project structure

```text
.
├── crudproduct/          # Django project configuration
├── productapp/           # Product model, views, URLs, templates, and static files
├── images/               # Sample image assets
├── manage.py
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.12 or newer
- PostgreSQL
- Git

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Abishek1124-eng/project-management-crud-django.git
cd project-management-crud-django
```

Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv myvenv
.\myvenv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Database configuration

Create a PostgreSQL database named `Database` and make sure PostgreSQL is running on `localhost:5432`.

The project uses the following default database settings:

| Setting | Value |
|---|---|
| Database | `Database` |
| User | `postgres` |
| Host | `localhost` |
| Port | `5432` |

Set the PostgreSQL password before starting the application:

### Windows PowerShell

```powershell
$env:POSTGRES_PASSWORD = "your-postgres-password"
$env:DJANGO_SECRET_KEY = "replace-with-a-secure-secret-key"
```

### macOS/Linux

```bash
export POSTGRES_PASSWORD="your-postgres-password"
export DJANGO_SECRET_KEY="replace-with-a-secure-secret-key"
```

For production deployments, configure `DEBUG`, `ALLOWED_HOSTS`, and all database credentials through environment variables and use a production WSGI server.

## Run migrations

```bash
python manage.py migrate
```

Create an administrator account if you want to use the Django admin:

```bash
python manage.py createsuperuser
```

## Start the development server

```bash
python manage.py runserver
```

Open the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Routes

| URL | Description |
|---|---|
| `/` | Product management home page |
| `/register/` | Register a new product |
| `/list/` | View all products |
| `/update/<id>/` | Update a product |
| `/delete/<id>/` | Delete a product |
| `/admin/` | Django administration |

## Validation

Run Django's system checks with:

```bash
python manage.py check
```

## Media and static files

Uploaded product images are stored in the local `media/` directory during development. The `media/` directory is ignored by Git so user-uploaded files are not committed to the repository.

Static CSS files are located in `productapp/static/`.

## License

This project is provided for learning and development purposes.
