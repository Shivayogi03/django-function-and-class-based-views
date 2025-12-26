# Django Function & Class Based Views

This repository demonstrates different ways of handling views in Django using:

- Function Based Views (FBV)
- Class Based Views (CBV)
- TemplateView
- FormView
- Django Forms with database insertion

It is useful for beginners to understand how Django views work in real projects.

---

## 📌 Features Covered

### 1️⃣ Function Based View (FBV)
- Insert data using Django forms
- Handle GET and POST requests manually

### 2️⃣ Class Based View (CBV)
- Same functionality as FBV
- Cleaner and reusable code using `View` class

### 3️⃣ TemplateView
- Render static and dynamic HTML
- Pass context data to templates

### 4️⃣ FormView
- Built-in form handling
- Automatic validation and saving

---

## 🛠 Technologies Used

- Python
- Django
- HTML
- Django Forms
- SQLite (default)

---

## 📂 Project Structure

project/
│── app/
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│ └── templates/
│ ├── insert_by_fbv.html
│ ├── insert_by_cbv.html
│ ├── insert_by_TV.html
│ ├── Insertbyfv.html
│ ├── RenderHTMLbyTV.html
│ └── Direct.html
│
│── project/
│ ├── urls.py
│ └── settings.py
│
└── manage.py

yaml

---

## 🚀 How to Run the Project

```bash
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Open browser:

cpp
http://127.0.0.1:8000/
📖 Learning Purpose
This project is created to practice and understand:

Django Views

Forms handling

URL routing

CBV vs FBV differences
