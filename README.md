# 📚 Proyecto Educativo: Library API & Web Frontend

Este proyecto consiste en un ecosistema educativo dividido en un **Backend** robusto (Django REST Framework) y un **Frontend** (Django Web) para la gestión de una biblioteca, incluyendo autores, libros y categorías.

## 🚀 Configuración Inicial

Sigue estos pasos para replicar el entorno de desarrollo:

### 1. Entorno Virtual y Dependencias

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno
# En Windows:
venv\Scripts\activate

# Instalar Django inicialmente
pip install django

```

### 2. Estructura de Proyectos

Se han creado dos núcleos independientes para separar la lógica de datos de la interfaz:

```bash
# Crear proyecto de Backend
django-admin startproject config backend

# Crear proyecto de Frontend
django-admin startproject config frontend

```

---

## ⚙️ Backend: API RESTful

El backend centraliza la lógica de negocio y la persistencia de datos.

### Aplicaciones del Backend

Dentro de la carpeta `backend`, se han inicializado los siguientes módulos:

* `api`: Endpoints principales.
* `authors`: Gestión de autores.
* `books`: Gestión de libros.
* `categories`: Clasificación de contenido.
* `docs`: Documentación automática (OpenAPI/Swagger).
* `profiles`: Perfiles de usuario.

### Instalación de Requerimientos

Asegúrate de tener el archivo `requirements.txt` con las versiones específicas y ejecuta:

```bash
pip install -r requirements.txt

```

> **Dependencias clave:** `Django 6.0.2`, `djangorestframework`, `drf-spectacular` (para OpenAPI 3.0), y `psycopg2-binary`.

### Base de Datos y Superusuario

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate

# Crear acceso al panel administrativo
python manage.py createsuperuser

```

---

## 🎨 Frontend: Interfaz Web

El frontend consume la API o maneja sus propias vistas para la interacción con el usuario.

### Aplicaciones del Frontend

Dentro de la carpeta `frontend`, se creó la app principal:

```bash
python manage.py startapp web

```

### Estructura de Plantillas

La aplicación `web` cuenta con las siguientes vistas preparadas:

* `base.html`: Estructura global.
* `books_list.html`: Catálogo de libros.
* `author_create.html` / `book_create.html`: Formularios de registro.

---

## 📂 Estructura de Directorios

### Backend Workspace

```text
backend
 ┣ api, authors, books, categories, docs, profiles
 ┣ config (settings, urls)
 ┣ db.sqlite3
 ┗ manage.py

```

### Frontend Workspace

```text
frontend
 ┣ web
 ┃ ┣ templates/web (base, lists, forms)
 ┃ ┣ forms.py, views.py, urls.py
 ┣ config
 ┗ manage.py

```

---

## 📖 Especificación de la API (OpenAPI 3.0.3)

La API está documentada bajo el estándar OpenAPI. Algunos de los endpoints principales incluyen:

| Método | Endpoint | Descripción |
| --- | --- | --- |
| `GET` | `/api/v1/authors/` | Listar todos los autores |
| `POST` | `/api/v1/books/` | Registrar un nuevo libro |
| `POST` | `/api/v1/books/{id}/add_category/` | Vincular categoría a un libro |
| `GET` | `/api/v1/categories/` | Listar categorías disponibles |

### Modelos de Datos (Schemas)

* **Author**: `id`, `name`, `birth_date`.
* **Book**: `id`, `title`, `isbn`, `author_id`, `categories`.
* **Category**: `id`, `name`.
