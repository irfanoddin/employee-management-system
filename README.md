# Employee Management System

A comprehensive web-based employee management system built with Flask and SQLite, designed to streamline HR operations and employee data management.

## Features

### Core Functionality
- **Employee Management**: Add, edit, delete, and search employees with detailed profiles
- **Department Management**: Manage organizational departments and track departmental assignments
- **Salary Tracking**: Monitor employee salaries and compensation details
- **Attendance Records**: Track daily attendance, absences, lateness, and leave requests
- **Search & Filtering**: Quickly find employees by name, email, or other criteria
- **Responsive Dashboard**: Real-time statistics and quick access to key functions

## Technology Stack

- **Backend**: Python 3.8+ with Flask web framework
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, Bootstrap 5, CSS3, JavaScript
- **Additional Tools**: Flask-SQLAlchemy for database operations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd c:\Users\aftabirfan\Desktop\new
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```
   The SQLite database will be created automatically on first run.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
.
├── app.py                      # Flask application entry point
├── config.py                   # Configuration settings
├── models.py                   # SQLAlchemy database models
├── routes.py                   # Flask routes and views
├── requirements.txt            # Python dependencies
├── database.db                 # SQLite database (created on startup)
│
├── templates/                  # HTML templates
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Dashboard
│   ├── employees.html         # Employee list
│   ├── add_employee.html      # Add employee form
│   ├── edit_employee.html     # Edit employee form
│   ├── departments.html       # Department list
│   ├── add_department.html    # Add department form
│   ├── edit_department.html   # Edit department form
│   ├── attendance.html        # Attendance records
│   └── add_attendance.html    # Add attendance form
│
└── static/                     # Static files
    ├── css/
    │   └── style.css          # Custom styles
    └── js/
        └── script.js          # Client-side JavaScript

```

## Database Models

### Employee
- First Name, Last Name
- Email, Phone
- Position, Salary
- Hire Date
- Department (Foreign Key)
- Status (Active, Inactive, On Leave)

### Department
- Name, Description
- List of associated employees

### Attendance
- Date, Status (Present, Absent, Late, Leave)
- Notes
- Employee (Foreign Key)

## Usage Guide

### Adding an Employee
1. Click "Add New Employee" on the dashboard
2. Fill in all required employee information
3. Select the appropriate department
4. Click "Add Employee"

### Managing Departments
1. Navigate to "Departments"
2. View all departments as cards
3. Edit or delete existing departments
4. Click "Add New Department" to create a department

### Tracking Attendance
1. Go to "Attendance" section
2. Click "Add Attendance Record"
3. Select employee and date
4. Mark attendance status
5. Add optional notes
6. Filter by employee to view individual attendance history

### Searching Employees
1. Use the search box on the Employees page
2. Search by name or email
3. Results update in real-time

## Development Features

- **Pagination**: Employee and department lists are paginated for better performance
- **Flash Messages**: User feedback for all operations (success/error)
- **Form Validation**: Client and server-side validation
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Error Handling**: Graceful error handling throughout the application

## API Endpoints

### Employee Search
```
GET /api/employees/search?q=<query>
```
Returns JSON array of matching employees

## Configuration

Edit `config.py` to customize:
- Database location
- Flask secret key
- Debug mode
- Upload folder

```python
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key-change-this'
```

## Troubleshooting

### Database Issues
If you encounter database errors, delete `database.db` and restart the application to reinitialize.

### Port Already in Use
If port 5000 is in use, modify the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Missing Dependencies
Ensure all packages in `requirements.txt` are installed:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- Export data to CSV/Excel
- Employee performance ratings
- Payroll integration
- Email notifications
- User authentication and roles
- Advanced reporting and analytics
- Leave management system
- Document storage

## License

This project is provided as-is for educational and business purposes.

## Support

For issues or questions, refer to the Flask and SQLAlchemy documentation:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)

---

**Created**: April 12, 2026
**Version**: 1.0.0
