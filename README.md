
# AWS Lambda + API Gateway + DynamoDB Example

This project contains two AWS Lambda functions integrated with a REST API built using API Gateway, and backed by a DynamoDB table named `users`.

---

## 🔗 API Endpoint

Base URL:  
`https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users`

---

## 📬 POST `/users`

Creates a new user in the DynamoDB table.  
Automatically generates a `user_id` (UUID) and returns it in the response.

### 🔹 Method:
`POST`

### 🔹 URL:
`https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users`

### 🔹 Headers:
`Content-Type: application/json`

### 🔹 Request Body (example):
```json
{
  "first_name": "Ali",
  "age": 30
}
```

### 🔹 Success Response:
```json
{
  "user_id": "f31b7e1b-c6d2-42f9-a0f0-b1a65cddf837"
}
```

### 🔹 PowerShell Example:
```powershell
$uri = "https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users"
$headers = @{
    "Content-Type" = "application/json"
}
$body = '{
  "first_name": "Ali",
  "age": 30
}'

$response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body
$response
```

### 🔹 Python Example:
```python
import requests
import json

url = "https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users"
headers = {"Content-Type": "application/json"}
data = {
    "first_name": "Ali",
    "age": 30
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())
```

---

## 📥 GET `/users/{user_id}`

Returns a user's full data if the given `user_id` exists.

### 🔹 Method:
`GET`

### 🔹 URL:
`https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users/{user_id}`

Replace `{user_id}` with the ID returned from the POST request.

### 🔹 Example Response:
```json
{
  "user_id": "f31b7e1b-c6d2-42f9-a0f0-b1a65cddf837",
  "first_name": "Ali",
  "age": 30
}
```

### 🔹 404 Response:
```json
{
  "message": "User not found"
}
```

---

## 📃 GET `/users`

Returns a list of all user IDs stored in the table.

### 🔹 URL:
`https://pyco897ze3.execute-api.eu-north-1.amazonaws.com/dev/users`

### 🔹 Response:
```json
{
  "user_ids": [
    "f31b7e1b-c6d2-42f9-a0f0-b1a65cddf837",
    "cd993cbe-7a48-4050-a0f2-9c268ac49e8e"
  ]
}
```

---

## 💡 Notes

- All data is stored in a DynamoDB table named `users`.
- Table has one partition key: `user_id` (String).
- Lambda functions are deployed with Python 3.12 runtime.
- Permissions to perform `PutItem` and `GetItem` on DynamoDB must be added to the Lambda IAM role.

---

## 📂 Files

- `create_user.py`: Lambda function to handle POST `/users`
- `get_user.py`: Lambda function to handle GET `/users` and `/users/{user_id}`
