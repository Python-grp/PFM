# 🎓 PreSkool - School Management System

## 📌 About the Project
PreSkool is a Django-based web application developed to manage school operations such as student records, teacher management, planning, and authentication.  

The project follows the **MVT architecture** and is organized into multiple Django apps for better scalability and maintainability. It also implements a **role-based authentication system** (Admin, Teacher, Student).

---

## 🚀 Features

### 👨‍🎓 Student Management
- Add, edit, delete students
- View student details
- Link students with parents (OneToOne relationship)

### 👨‍🏫 Teacher Management
- Manage teachers
- Assign roles and responsibilities

### 📅 Planning & Exams
- Manage planning (schedule)
- Handle exams and academic organization

### 🔐 Authentication System
- Custom user model
- Role-based access:
  - Admin
  - Teacher
  - Student
- Signup / Login / Logout

### 🗂️ Admin Panel
- Full data management using Django admin
- Search, filter, and organize records

---

## 🏗️ Project Structure

school/
│

├── faculty/

│ ├── views.py

│ ├── urls.py

│ └── models.py

│
├── student/

│ ├── models.py

│ ├── views.py

│ ├── urls.py

│ └── admin.py

├── home_auth/

│ ├── models.py

│ ├── views.py

│ └── urls.py
│
├── templates/

│ ├── authentication/

│ └── students/
│
├── static/

│ └── assets/

│
└── manage.py

---
## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default)
- **Libraries:**
  - Pillow (for image handling)

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Python-grp/PFM.git
cd PFM
cd school
Create virtual environment
python -m venv monenv
monenv\Scripts\activate      # Windows
# source monenv/bin/activate  # Linux/Mac
Install dependencies
pip install -r ../requirements.txt
Apply migrations
python manage.py makemigrations
python manage.py migrate
Create superuser
python manage.py createsuperuser
. Run server
python manage.py runserver
-----------------> Open in browser:
 http://127.0.0.1:8000
🔑 Test Credentials (optional)
Admin:

email: admin@test.com

password: 123456


## 🎬 Demo & Screenshots

### 🎥 Demo Videos by Role

#### 👨‍💼 Admin Demo
👉 [Watch Admin Demo](your-admin-video-link)

#### 👨‍🏫 Teacher Demo
👉 [Watch Teacher Demo](your-teacher-video-link)

#### 👨‍🎓 Student Demo
👉 [Watch Student Demo](your-student-video-link)

---

### 📸 Screenshots

#### 🖥️ Dashboard
![Dashboard](link)

#### 👨‍🎓 Student Management
![Students](link)

#### 👨‍🏫 Teacher Management
![Teachers](link)

#### ⚙️ Admin Panel
![Admin](link)
📚 What We Learned
Django MVT architecture

Multi-app project structure

Custom authentication system

CRUD operations

Database relationships (OneToOne)
⚠️ Challenges Faced

Configuring custom user model

Managing multiple Django apps

Linking models and templates

Handling static and media files

👥 Authors

 Oussama Jabir

Zineb Khbiaz

Aya Lmasoudi
