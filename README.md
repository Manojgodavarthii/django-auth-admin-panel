## django-auth-admin-panel or   Django Role-Based User Management System

A simple and secure **User Management System built with Django** that provides user registration, mobile-number-based authentication, role-based access control, user profile management, and an admin panel for managing users.

This project was **developed as a technical task assigned by a company as part of an interview/selection process** to demonstrate practical skills in Django, Python, database integration, authentication, authorization, CRUD operations, form validation, and frontend-backend integration.

---

## 📌 Project Title

# Django Role-Based User Management System

---

## 🏢 Company Interview Task

This project was developed as a **technical assignment provided by a company during the interview process**.

The purpose of the task was to demonstrate practical implementation skills in:

* Python and Django
* User authentication
* Role-Based Access Control (RBAC)
* Database integration
* CRUD operations
* Form validation
* Password security
* Frontend and backend integration
* Django project structure
* User and admin management

The project was developed independently based on the requirements provided as part of the company interview task.

---

## 📖 Project Overview

The Django Role-Based User Management System is a web application designed to manage users through two different roles:

* **User**
* **Admin**

Users can create an account using their name, mobile number, and password. After registration, users can log in using their mobile number and password and access their own dashboard.

Administrators have additional privileges. They can view all registered users, add new users, edit existing users, delete users, and assign user roles.

The application uses Django's authentication system with a **custom User model**, where the mobile number is used as the login identifier instead of the default username.

---

## 🎯 Objectives

The main objectives of this project are:

* Implement user registration and login.
* Authenticate users using mobile number and password.
* Implement role-based access control.
* Create separate user and admin sections.
* Allow users to view and update their own profile.
* Allow administrators to manage all users.
* Validate mobile numbers and passwords.
* Store user information in a database.
* Implement secure password storage using Django's password hashing.
* Use Django templates for frontend rendering.
* Implement CRUD operations for user management.

---

## ✨ Key Features

### 👤 User Features

* User registration
* Mobile number validation
* Unique mobile number checking
* Strong password validation
* Password confirmation
* User login
* User logout
* User dashboard
* View personal details
* Edit personal profile
* Session-based authentication
* Access restriction for unauthenticated users

### 👨‍💼 Admin Features

* Admin login
* Admin dashboard
* View all registered users
* Add new users
* Edit existing users
* Delete users
* Assign User/Admin roles
* Prevent admin from deleting their own account
* Admin-only access protection

### 🔐 Security Features

* Django authentication system
* Password hashing using Django's `set_password()`
* Session-based authentication
* CSRF protection
* `login_required` protection
* Custom admin authorization decorator
* Role-based access control
* Unique mobile number validation
* Password complexity validation
* Form-level server-side validation

---

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Database

* SQLite3

### Development Tools

* VS Code / PyCharm
* Python Virtual Environment
* Django Development Server
* Git
* GitHub

---

## 🏗️ Project Architecture

The project is divided into two main Django applications:

### 1. `users`

Responsible for normal user functionality.

Main responsibilities:

* Registration
* Login
* Logout
* User dashboard
* Profile editing
* User authentication
* User form validation
* Custom User model

### 2. `adminpanel`

Responsible for administrator functionality.

Main responsibilities:

* Admin dashboard
* View all users
* Add users
* Edit users
* Delete users
* Role management
* Admin authorization

---

## 📂 Project Structure

```text
dajngo_user_managment/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── links.txt
│
├── user_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── migrations/
│   │   └── 0001_initial.py
│   │
│   └── templates/
│       └── users/
│           ├── login.html
│           ├── register.html
│           ├── home.html
│           └── edit_profile.html
│
├── adminpanel/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   │
│   ├── migrations/
│   │
│   └── templates/
│       └── adminpanel/
│           ├── home.html
│           ├── add_user.html
│           └── edit_user.html
│
├── templates/
│   └── base.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

---

# 🔄 Application Workflow

## User Registration Flow

```text
User
  ↓
Registration Page
  ↓
Enter Name + Mobile + Password
  ↓
Validate Mobile Number
  ↓
Check Mobile Number Uniqueness
  ↓
Validate Password
  ↓
Confirm Password
  ↓
Create User
  ↓
Hash Password
  ↓
Save User to SQLite Database
  ↓
Redirect to Login
```

---

## User Login Flow

```text
User
  ↓
Login Page
  ↓
Enter Mobile Number + Password
  ↓
Django Authentication
  ↓
Check Credentials
  ↓
Identify User Role
  ↓
 ┌───────────────┐
 │               │
User           Admin
 │               │
 ↓               ↓
User Dashboard  Admin Dashboard
```

---

# 👤 User Module

The `users` application handles all normal user operations.

## Registration

The registration form collects:

* Name
* Mobile Number
* Password
* Confirm Password

The application validates:

### Mobile Number

* Must contain only numbers.
* Must contain exactly 10 digits.
* Must be unique.

### Password

The password must:

* Contain at least 6 characters.
* Contain at least one uppercase letter.
* Contain at least one lowercase letter.
* Contain at least one number.
* Contain at least one special character.

The password and confirmation password must also match.

---

## Login

Users log in using:

```text
Mobile Number
Password
```

The custom user model uses:

```python
USERNAME_FIELD = 'mobile'
```

Therefore, the mobile number acts as the primary login identifier.

---

## User Dashboard

After successful login, a normal user is redirected to the user dashboard.

The dashboard displays:

* User name
* Mobile number
* Role
* Account creation date

The user can also:

* Edit their profile
* Logout

---

## Edit Profile

Users can update:

* Name
* Mobile number

The application again validates the mobile number and checks that the new mobile number is not already registered by another user.

Users cannot access the admin management functionality.

---

# 👨‍💼 Admin Module

The `adminpanel` application handles administrator functionality.

## Admin Dashboard

After an administrator logs in, they are redirected to the admin dashboard.

The dashboard displays all registered users in a table containing:

* User ID
* Name
* Mobile number
* Role
* Account creation date
* Actions

---

## Add User

An administrator can create a new user from the admin dashboard.

The administrator can specify:

* Name
* Mobile number
* Role
* Password

The same mobile-number and password validation rules are applied.

---

## Edit User

An administrator can select an existing user and update:

* Name
* Mobile number
* Role
* Password

If a new password is entered, it is stored using Django's password hashing mechanism.

---

## Delete User

An administrator can delete users from the admin dashboard.

The system also prevents an administrator from deleting their own currently logged-in admin account.

---

# 🔐 Authentication and Authorization

The project uses Django's built-in authentication framework along with a custom user model.

The custom model extends:

```python
AbstractBaseUser
```

and uses:

```python
USERNAME_FIELD = 'mobile'
```

This allows authentication using a mobile number instead of a username.

---

# 🛡️ Role-Based Access Control

The application implements two roles:

```text
user
admin
```

The role is stored in the User model.

The application checks the user's role before allowing access to protected functionality.

For example, admin views use a custom decorator:

```python
@admin_required
```

The decorator verifies that:

1. The user is logged in.
2. The user's role is `admin`.

If a normal user attempts to access an admin page, access is denied and the user is redirected to the user dashboard.

---

# 🔒 Password Security

Passwords are never directly stored as plain text.

During registration, the password is passed to:

```python
user.set_password(password)
```

Django hashes the password before storing it in the database.

During login, Django's authentication system compares the entered password against the stored password hash.

---

# 🗄️ Database

The project uses:

```text
SQLite3
```

The database file is:

```text
db.sqlite3
```

The main custom database model is:

```text
User
```

It contains fields such as:

| Field        | Description             |
| ------------ | ----------------------- |
| id           | Unique user ID          |
| name         | User's name             |
| mobile       | Unique mobile number    |
| role         | User/Admin role         |
| created_at   | Account creation date   |
| is_active    | Account active status   |
| is_staff     | Django staff status     |
| is_superuser | Django superuser status |
| password     | Django hashed password  |

The custom user model is configured using:

```python
AUTH_USER_MODEL = 'users.User'
```

---

# 🧩 Django Forms

The project uses Django Forms and ModelForms for input handling and validation.

### `RegisterForm`

Used for:

* User registration
* Mobile validation
* Password validation
* Password confirmation

### `LoginForm`

Used for:

* Mobile number
* Password

### `UserUpdateForm`

Used for:

* Updating the logged-in user's profile

### `AdminUserForm`

Used by administrators for:

* Adding users
* Editing users
* Assigning roles
* Updating passwords

---

# 🔗 URL Structure

| URL                             | Purpose               |
| ------------------------------- | --------------------- |
| `/`                             | Login                 |
| `/login/`                       | Login                 |
| `/register/`                    | User registration     |
| `/logout/`                      | Logout                |
| `/user/home/`                   | User dashboard        |
| `/user/edit/`                   | Edit user profile     |
| `/adminpanel/`                  | Admin dashboard       |
| `/adminpanel/add-user/`         | Add user              |
| `/adminpanel/edit-user/<id>/`   | Edit user             |
| `/adminpanel/delete-user/<id>/` | Delete user           |
| `/django-admin/`                | Django administration |

---

# 🎨 Frontend

The frontend is implemented using:

* HTML
* CSS
* JavaScript
* Django Template Language

A common base template is used:

```text
templates/base.html
```

Static resources are organized as:

```text
static/
├── css/
│   └── style.css
└── js/
    └── script.js
```

---

# 🔄 CRUD Operations

The admin module implements complete CRUD operations for user management.

### Create

Administrator can create a new user.

### Read

Administrator can view all registered users.

### Update

Administrator can modify user details.

### Delete

Administrator can remove users.

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project:

```bash
cd dajngo_user_managment
```

---

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

For Git Bash:

```bash
source venv/Scripts/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

## 5. Create an Admin Account

```bash
python manage.py createsuperuser
```

Enter the requested information.

---

## 6. Run the Development Server

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

---

# 🌐 Application Pages

### Login

```text
http://127.0.0.1:8000/
```

### Registration

```text
http://127.0.0.1:8000/register/
```

### User Dashboard

```text
http://127.0.0.1:8000/user/home/
```

### Admin Dashboard

```text
http://127.0.0.1:8000/adminpanel/
```

### Django Admin

```text
http://127.0.0.1:8000/django-admin/
```

---

# 🧪 Validation

## Mobile Number Validation

The application validates that:

* The mobile number contains only digits.
* The mobile number contains exactly 10 digits.
* The mobile number is unique.

---

## Password Validation

The password must contain:

* Minimum 6 characters
* Uppercase letter
* Lowercase letter
* Number
* Special character

Example:

```text
Admin@123
```

---

# 🔐 Security Implementation

The project uses several Django security mechanisms.

### CSRF Protection

Forms use Django's CSRF token:

```django
{% csrf_token %}
```

This helps protect POST requests against Cross-Site Request Forgery.

### Authentication

Protected pages use:

```python
@login_required
```

This prevents unauthenticated users from accessing protected pages.

### Authorization

Admin functionality uses:

```python
@admin_required
```

to ensure that only administrators can access admin views.

### Password Hashing

Passwords are processed using:

```python
set_password()
```

instead of storing plain-text passwords.

### Input Validation

Django Forms validate:

* Mobile number
* Password
* Password confirmation
* Duplicate mobile numbers
* User data

---

# 🧠 Django Concepts Demonstrated

This project demonstrates practical usage of:

* Django project structure
* Django applications
* Custom User Model
* `AbstractBaseUser`
* `BaseUserManager`
* Django authentication
* Django sessions
* `login()`
* `logout()`
* `authenticate()`
* `login_required`
* Custom decorators
* Role-Based Access Control
* Django Forms
* ModelForms
* Form validation
* Django ORM
* SQLite database
* CRUD operations
* Django templates
* Template inheritance
* Static files
* URL routing
* Migrations
* CSRF protection
* Password hashing
* Django messages framework

---

# 📊 Project Flow

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                 ┌───────────▼───────────┐
                 │   Registration/Login   │
                 └───────────┬───────────┘
                             │
                    Authentication
                             │
                    ┌────────▼────────┐
                    │   Check Role    │
                    └───────┬─────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
        ┌─────▼─────┐               ┌─────▼─────┐
        │   User    │               │   Admin   │
        └─────┬─────┘               └─────┬─────┘
              │                           │
        User Dashboard              Admin Dashboard
              │                           │
        Edit Profile              Manage All Users
                                      │
                         ┌────────────┼────────────┐
                         │            │            │
                       Add          Edit         Delete
                       User         User         User
```

---

# 🚀 Future Improvements

Possible future enhancements include:

* Email verification
* OTP-based mobile authentication
* Password reset
* User search and filtering
* Pagination
* User activation/deactivation
* Audit logs
* Login activity tracking
* Django REST API
* PostgreSQL/MySQL support
* Improved responsive UI
* Automated testing
* Docker deployment
* Cloud deployment

---

# ⚠️ Production Considerations

This project was developed primarily for **company interview/task demonstration purposes**.

Before production deployment:

* Set `DEBUG = False`
* Store `SECRET_KEY` in environment variables
* Configure `ALLOWED_HOSTS`
* Use a production database such as PostgreSQL
* Configure HTTPS
* Configure secure cookies
* Configure production security settings
* Remove development credentials
* Keep sensitive configuration outside the repository

---

# 💼 Company Interview Task

This project was developed as a **technical task assigned by a company as part of an interview process**.

The project demonstrates practical knowledge of:

```text
Python
Django
Authentication
Authorization
Role-Based Access Control
CRUD Operations
Database Integration
SQLite
Django ORM
Form Validation
Password Security
Session Management
CSRF Protection
HTML
CSS
JavaScript
Django Templates
Git/GitHub
```

The implementation focuses on building a functional, maintainable, and secure Django application while following the requirements provided as part of the interview assignment.

---

# 👨‍💻 Skills Demonstrated

```text
Python
Django
HTML5
CSS3
JavaScript
SQLite
Django ORM
Custom User Model
Authentication
Authorization
RBAC
CRUD
Form Validation
Password Hashing
Session Management
CSRF Protection
Django Templates
Git
GitHub
```

---

# 📌 Conclusion

The **Django Role-Based User Management System** is a practical Django application developed as a **company interview technical assignment**.

It demonstrates how user authentication, role-based authorization, database operations, form validation, password security, and CRUD functionality can be combined to create a complete user-management application.

The project provides separate functionality for normal users and administrators while controlling access to management operations through Django's authentication and authorization mechanisms.

---

# Proprietary License

Copyright © 2026 **Godavarthi Naga Manoj Balaji**. All Rights Reserved.

This project was developed by **Godavarthi Naga Manoj Balaji** as part of a technical task assigned by a company during an interview/selection process.

All source code, documentation, designs, and other materials contained in this repository are the intellectual property of the author, unless otherwise stated.


The project is provided for **demonstration, evaluation, and portfolio purposes only**.

Unauthorized copying, redistribution, modification, or reuse of this project is not permitted.

---
📄 License

Copyright © 2026 Godavarthi Naga Manoj Balaji. All Rights Reserved.

This project is proprietary and was developed as a company technical interview assignment.

The source code and associated materials are provided for **demonstration, evaluation, and portfolio purposes only**. No permission is granted to modify, distribute, publish,  the project without prior written permission from the author.

