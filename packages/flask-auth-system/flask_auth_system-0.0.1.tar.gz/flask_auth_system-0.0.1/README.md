# Flask Authentication API

This is a simple authentication API built using Flask, JWT, and Fernet encryption.

## Features

- User registration with hashed passwords
- User login with JWT token generation
- Token refresh functionality
- Token blacklist mechanism

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-repo/flask-auth-api.git
   cd flask-auth-api
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:

   ```sh
   python app.py
   ```

## API Endpoints

### 1. Register a new user

**Endpoint:** `POST /register`

**Request Body:**

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**

```json
{
    "token": "your_jwt_token"
}
```

### 2. Login

**Endpoint:** `POST /login`

**Headers:**

```json
Authorization: Basic <base64-encoded-credentials>
```

**Response:**

```json
{
    "token": "your_jwt_token"
}
```

### 3. Refresh Token

**Endpoint:** `POST /refresh`

**Headers:**

```json
X-Access-Token: your_jwt_token
```

**Response:**

```json
{
    "token": "new_jwt_token"
}
```

### 4. Blacklist a Token

**Endpoint:** `POST /blacklist`

**Headers:**

```json
X-Access-Token: your_jwt_token
```

**Response:**

```json
{
    "message": "Token blacklisted"
}
```

## License

This project is licensed under the MIT License.


