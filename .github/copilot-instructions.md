<!-- Employee Management System - Copilot Instructions -->

# Employee Management System

## Project Overview
A full-featured employee management system built with Flask, SQLite, and modern web technologies.

## Features
- Employee CRUD operations
- Department management
- Salary tracking
- Attendance records
- Search and filtering
- Data export capabilities

## Project Structure
```
├── app.py                 # Flask application entry point
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── models.py             # Database models
├── routes.py             # Flask routes
├── database.db           # SQLite database
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── employees.html
│   ├── add_employee.html
│   ├── edit_employee.html
│   └── departments.html
├── static/               # CSS and JavaScript
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── README.md
```

## Setup Instructions
1. Install Python 3.8 or higher
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize database: `python app.py`
4. Run application: `python app.py`
5. Access at http://localhost:5000

## Development Notes
- Uses Flask for web framework
- SQLite for database
- SQLAlchemy ORM for database operations
- Bootstrap for responsive UI
