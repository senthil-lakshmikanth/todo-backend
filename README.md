## 🌐 Backend Server
[🚀 Live API](https://todo-backend-ma5f.onrender.com)

1️⃣ Signup
```POST /signup```
2️⃣ Login
``` POST /login ```

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

➕ Create Task
```POST /tasks```

Request Body
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
