## 🚀 Live API
Base URL: https://todo-backend-ma5f.onrender.com

#### 1️⃣ Signup: `POST /signup` and 2️⃣ Login: `POST /login`

Request Body
```
{
  "email": "user@example.com",
  "password": "strongpassword"
}
```

Login Response
```
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

##### 🔑 Using the Access Token

Header Format
```
Authorization: Bearer <access_token>
```

➕ Create Task ```POST /tasks``` and ✏️ Update Task ```PUT /tasks/{id}``` 

##### Request Body
```
{
  "title": "Task title",
  "description": "Task description",
  "due_date": "2026-02-20T12:00:00"
}
```

📋 Get All Tasks
```GET /tasks```

🔎 Get Task by ID
```GET /tasks/{id}```

🗑️ Delete Task by ID
```DELETE /tasks/{id}```
