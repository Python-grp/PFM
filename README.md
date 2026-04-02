
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
```

### 2. Create virtual environment
```bash
python -m venv monenv
monenv\Scripts\activate      # Windows
# source monenv/bin/activate  # Linux/Mac
```

### 3. Install dependencies
```bash
pip install -r ../requirements.txt
```

### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Run server
```bash
python manage.py runserver
```

----> Open in browser: http://127.0.0.1:8000

🔑 Test Credentials (optional)
---
Admin:
email: admin@test.com
password: 123456

--------------

## 🎬 Demo & Screenshots

### 🎥 Demo Videos by Role
---

#### 👨‍💼 Admin Demo
 [Watch Admin Demo](https://github.com/Python-grp/PFM/releases/download/v1.0.0/admin.mp4)

#### 👨‍🏫 Teacher Demo
 [Watch Teacher Demo](https://github.com/Python-grp/PFM/releases/download/v2.0.0/Teacher.mp4)

#### 👨‍🎓 Student Demo
 [Watch Student Demo](https://github.com/Python-grp/PFM/releases/download/v3.0.0/student.mp4)


### 📸 Screenshots
---
#### ⚙️ Admin Panel
![Image](https://github.com/user-attachments/assets/cc363c95-b2b3-4389-94da-f4a0e7ac72c8)

![Image](https://github.com/user-attachments/assets/b1ef9f64-7e75-4b3f-aafc-1f8983ff2008)

![Image](https://github.com/user-attachments/assets/cab33231-cd08-4bed-8a4f-36abbccac7e8)

![Image](https://github.com/user-attachments/assets/398f47c3-46bb-4669-86f3-12231d40ef0c)

![Image](https://github.com/user-attachments/assets/a22346a7-49ec-4605-956f-b7e87d1bf2b3)

![Image](https://github.com/user-attachments/assets/36f660e2-e5ec-452b-9b8e-aa5b4e3798e8)

![Image](https://github.com/user-attachments/assets/c3b75d43-bd72-4822-bc46-8b0f73bfba70)

![Image](https://github.com/user-attachments/assets/162d740f-a31a-4875-bc7d-f3b216b48695)

![Image](https://github.com/user-attachments/assets/9e94fdee-4301-4013-ae3e-b58ff75eac11)

![Image](https://github.com/user-attachments/assets/95a0e6af-a3a1-4e03-873c-ae1d6e88cac1)

![Image](https://github.com/user-attachments/assets/7b055e23-3d21-4383-afdd-df8cb5d63dd9)

![Image](https://github.com/user-attachments/assets/5cc81296-b15e-4a3c-beb8-3a87b7c99614)

#### 👨‍🏫 Teacher Management
<img width="1267" height="601" alt="Image" src="https://github.com/user-attachments/assets/7865fd93-1fc0-4279-974e-d2465078a17d" />

<img width="1284" height="607" alt="Image" src="https://github.com/user-attachments/assets/f3472ce6-5020-421e-9732-96cec368499d" />

<img width="1285" height="608" alt="Image" src="https://github.com/user-attachments/assets/1b61f2b6-a818-4c8b-af5d-a5594f6bfde3" />

<img width="1280" height="605" alt="Image" src="https://github.com/user-attachments/assets/631a7073-0367-498c-b5b4-5f05b24a276b" />

<img width="1266" height="609" alt="Image" src="https://github.com/user-attachments/assets/f9f37d08-5aad-4613-833e-8cebc3faf227" />

<img width="1280" height="606" alt="Image" src="https://github.com/user-attachments/assets/248f3f44-07c3-4a2b-87fb-576ccc47a33a" />

#### 👨‍🎓 Student Management

![Image](https://github.com/user-attachments/assets/683dd4de-fde2-4ec8-99b8-126b54c86835)

![Image](https://github.com/user-attachments/assets/55610c98-edb3-43f5-863c-cae55e838731)

![Image](https://github.com/user-attachments/assets/326fc564-9a12-40c6-9480-4bd26074e5cb)

![Image](https://github.com/user-attachments/assets/acdaa6ea-d7f8-4008-a9a3-e5263431c657)

-----

📚 What We Learned
-
Django MVT architecture

Multi-app project structure

Custom authentication system

CRUD operations

Database relationships (OneToOne)

⚠️ Challenges Faced
-

Configuring custom user model

Managing multiple Django apps

Linking models and templates

Handling static and media files

👥 Authors
-

 Oussama Jabir

Zineb Khbiaz

Aya Lmasoudi
