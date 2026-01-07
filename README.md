
###A-simple-classroom-model-using-server-side-rendered-Django

A role-based web application built using **Django** where:
- **Teachers** can create assignments and upload reference materials
- **Students** can view assignments and submit their work
- Assignments automatically expire after deadlines

This project is built as a learning-focused academic system with proper **authentication, authorization, and file handling**.

---

## 🚀 Features

### 👩‍🏫 Teacher
- Create assignments
- Upload reference files and links
- Set deadlines
- View student submissions

### 👨‍🎓 Student
- View available assignments
- Download reference materials
- Submit assignment files
- Cannot view or modify other students’ submissions

### 🔐 Authentication & Authorization
- Login / Register system
- Role-based access (Student / Teacher)
- Protected routes using decorators

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (development)
- **Authentication:** Django Auth
- **File Handling:** Django Media Files

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/student-portal.git
cd student-portal
### 2 
