# 🚀 Django REST Framework API

![Django](https://img.shields.io/badge/Django-REST-green?style=for-the-badge&logo=django) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)

## 📌 Overview
This is a **Django REST Framework (DRF) API** project. It provides a structured backend for handling API requests efficiently. This guide will help you set up and run the project step by step.

---

## ✨ Features
✅ **Django REST Framework** for building APIs  
✅ **CRUD operations** for data management  
✅ **SQLite** as the default database (Can be switched to PostgreSQL/MySQL)  
✅ **Modular and Scalable** project structure  

---

## 📂 Project Structure
```
project_root/
│-- api/                # Main API application
│-- project_name/       # Django project settings
│-- db.sqlite3          # SQLite database
│-- manage.py           # Django management script
│-- requirements.txt    # Dependencies list
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone <your-repository-url>
cd <your-project-folder>
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # For Linux/macOS
env\Scripts\activate    # For Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```sh
python manage.py migrate
```

### 5️⃣ Run the Development Server
```sh
python manage.py runserver
```
The API will be available at:  
📍 `http://127.0.0.1:8000/`

---

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| GET | `/api/items/` | Get all items |
| POST | `/api/items/` | Create a new item |
| GET | `/api/items/{id}/` | Retrieve a specific item |
| PUT | `/api/items/{id}/` | Update an item |
| DELETE | `/api/items/{id}/` | Delete an item |

---


📍 The API will be available at `http://127.0.0.1:8000/`


## 🤝 Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome! 🎉

---

## 📜 License
This project is licensed under the MIT License.

---

**👤 Author:** Aditya Roy Karmakar


