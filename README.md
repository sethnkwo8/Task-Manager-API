# 🧩 Task Manager API

##  Overview

A secure and fully-featured **Task Management REST API** built with **Django REST Framework (DRF)** and **JWT Authentication (SimpleJWT).**
Users can register, log in, and manage their personal task lists — including creating, updating, searching, and deleting tasks.

---

## 🚀 Features

- ✅ **User Registration & Authentication** using JSON Web Tokens (JWT) 
- ✅ **CRUD Operations** for managing personal tasks 
- ✅ **Automatic user-task association** each user only sees their own tasks 
- ✅ **Filtering, Searching & Pagination** (by title, description, priority, and completion status)
- ✅ **PostgreSQL database** for production-ready persistence 
- ✅ **Comprehensive API Tests** using DRF's APITestCase and JWT 
- ✅ **Custom Serializer Logic** and clean REST architecture 

---

## 🧰 Technologies Used

| Category | Tools |
|-----------|--------|
| **Backend** | Django (Python), Django REST Framework |
| **Database** | PostgreSQL |
| **Authentication** | SimpleJWT |
| **Version Control** | Git & GitHub |
| **Testing** | Django's APITestCase |
| **Environment Management** | python-decouple |

---

## ⚙️ Installation

Follow these steps to set up and run the project locally.

**Step 1 – Clone the Repository**
```bash
git clone https://github.com/sethnkwo8/Task-Manager-API.git
cd taskmanager
```

---

**Step 2 – Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

---

**Step 3 – Install Dependencies**
```bash
pip install -r requirements.txt        
```

---

**Step 4 – Set Up Environment Variables**
Create a .env file in your project root and add:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

---

**Step 5 – Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

**Step 6 – Run the Server**
```bash
python manage.py runserver
```
Visit your app at:
http://127.0.0.1:8000/

---

## 🗒 Task Endpoints (JWT Protected)

| Method | Endpoint | Description |
|-----------|--------------|----------------|
| GET | /api/tasks/ | Get all tasks for the logged-in user |
| POST | /api/tasks/ | Create a new task |
| GET | /api/tasks/id/ | Retrieve a specific task |
| PUT | /api/tasks/id/ | Update a task |
| DELETE | /api/tasks/id/ | Delete a task |
  
---

## Headers
```
Authorization: Bearer <your_access_token>
```

---

## 🔍 Filtering & Search Examples

| Parameter | Example | Description |
|-----------|--------------|----------------|
| ?title= | /api/tasks/?title=report | Filter by title |
| ?completed= | /api/tasks/?completed=true | Filter by completion status |
| ?search= | /api/tasks/?search=meeting | Search by title or description |

---

## 🧪 Running Tests

Run the API tests to verify everything works correctly:
```bash
python manage.py test
```

---

## 🧱 Project Structure

```
taskmanager/
├── tasks/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── .env
``` 

---

## 📸 Example Response
```json
{
  "id": 3,
  "title": "Finish DRF Project",
  "description": "Complete the Task Manager API",
  "priority": "high",
  "completed": false,
  "created_at": "2025-11-03T12:00:00Z",
  "updated_at": "2025-11-03T12:00:00Z"
}
```

---

## 🧠 Key Learning Highlights

- Built reusable **ModelViewSets** with filtering and search
- Implemented **JWT Authentication** with SimpleJWT
- Wrote **unit and integration tests** for each API endpoint
- Used **PostgreSQL** in a production-like environment
---

## 🏁 Future Improvements

- Add Docker support for containerization
- Implement password reset functionality
- Integrate a React or Next.js frontend
- Add Swagger or ReDoc documentation

---

## 👨‍💻 Author

**Seth Nkwo**  
📧 [sethnkwocool@gmail.com]  
🔗 [GitHub Profile](https://github.com/sethnkwo8)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/seth-nkwo/)  

---