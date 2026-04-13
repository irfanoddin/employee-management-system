from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Employee, Department, Attendance
from datetime import datetime, date
from sqlalchemy import or_

main_bp = Blueprint('main', __name__)

# Home route
@main_bp.route('/')
def index():
    """Home page"""
    total_employees = Employee.query.count()
    total_departments = Department.query.count()
    active_employees = Employee.query.filter_by(status='Active').count()
    return render_template('index.html', 
                         total_employees=total_employees,
                         total_departments=total_departments,
                         active_employees=active_employees)

# ============ EMPLOYEE ROUTES ============

@main_bp.route('/employees')
def employees():
    """List all employees"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '')
    
    query = Employee.query
    if search:
        query = query.filter(or_(
            Employee.first_name.ilike(f'%{search}%'),
            Employee.last_name.ilike(f'%{search}%'),
            Employee.email.ilike(f'%{search}%')
        ))
    
    employees_list = query.paginate(page=page, per_page=10)
    return render_template('employees.html', 
                         employees=employees_list.items,
                         total=employees_list.total,
                         page=page,
                         pages=employees_list.pages,
                         search=search)

@main_bp.route('/employee/add', methods=['GET', 'POST'])
def add_employee():
    """Add new employee"""
    departments = Department.query.all()
    
    if not departments:
        flash('No departments available. Please create a department first.', 'warning')
        return redirect(url_for('main.add_department'))
    
    if request.method == 'POST':
        try:
            if not all([request.form.get('first_name'), request.form.get('last_name'), 
                       request.form.get('email'), request.form.get('position'),
                       request.form.get('salary'), request.form.get('hire_date'),
                       request.form.get('department_id')]):
                flash('All fields are required!', 'danger')
                return render_template('add_employee.html', departments=departments)
            
            dept_id = int(request.form['department_id'])
            if not Department.query.get(dept_id):
                flash('Invalid department selected!', 'danger')
                return render_template('add_employee.html', departments=departments)
            
            employee = Employee(
                first_name=request.form['first_name'].strip(),
                last_name=request.form['last_name'].strip(),
                email=request.form['email'].strip().lower(),
                phone=request.form.get('phone', '').strip(),
                position=request.form['position'].strip(),
                salary=float(request.form['salary']),
                hire_date=datetime.strptime(request.form['hire_date'], '%Y-%m-%d').date(),
                department_id=dept_id,
                status='Active'
            )
            db.session.add(employee)
            db.session.commit()
            flash(f'Employee {employee.full_name} added successfully!', 'success')
            return redirect(url_for('main.employees'))
        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_employee.html', departments=departments)

@main_bp.route('/employee/<int:employee_id>/edit', methods=['GET', 'POST'])
def edit_employee(employee_id):
    """Edit employee"""
    employee = Employee.query.get_or_404(employee_id)
    departments = Department.query.all()
    
    if request.method == 'POST':
        try:
            if not all([request.form.get('first_name'), request.form.get('last_name'),
                       request.form.get('email'), request.form.get('position'),
                       request.form.get('salary'), request.form.get('hire_date'),
                       request.form.get('department_id')]):
                flash('All fields are required!', 'danger')
                return render_template('edit_employee.html', employee=employee, departments=departments)
            
            dept_id = int(request.form['department_id'])
            if not Department.query.get(dept_id):
                flash('Invalid department selected!', 'danger')
                return render_template('edit_employee.html', employee=employee, departments=departments)
            
            employee.first_name = request.form['first_name'].strip()
            employee.last_name = request.form['last_name'].strip()
            employee.email = request.form['email'].strip().lower()
            employee.phone = request.form.get('phone', '').strip()
            employee.position = request.form['position'].strip()
            employee.salary = float(request.form['salary'])
            employee.hire_date = datetime.strptime(request.form['hire_date'], '%Y-%m-%d').date()
            employee.department_id = dept_id
            employee.status = request.form.get('status', 'Active')
            
            db.session.commit()
            flash(f'Employee {employee.full_name} updated successfully!', 'success')
            return redirect(url_for('main.employees'))
        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('edit_employee.html', employee=employee, departments=departments)

@main_bp.route('/employee/<int:employee_id>/delete', methods=['POST'])
def delete_employee(employee_id):
    """Delete employee"""
    employee = Employee.query.get_or_404(employee_id)
    name = employee.full_name
    
    db.session.delete(employee)
    db.session.commit()
    flash(f'Employee {name} deleted successfully!', 'success')
    return redirect(url_for('main.employees'))

# ============ DEPARTMENT ROUTES ============

@main_bp.route('/departments')
def departments():
    """List all departments"""
    page = request.args.get('page', 1, type=int)
    departments_list = Department.query.paginate(page=page, per_page=10)
    return render_template('departments.html', 
                         departments=departments_list.items,
                         total=departments_list.total,
                         page=page)

@main_bp.route('/department/add', methods=['GET', 'POST'])
def add_department():
    """Add new department"""
    if request.method == 'POST':
        try:
            if not request.form.get('name', '').strip():
                flash('Department name is required!', 'danger')
                return render_template('add_department.html')
            
            department = Department(
                name=request.form['name'].strip(),
                description=request.form.get('description', '').strip()
            )
            db.session.add(department)
            db.session.commit()
            flash(f'Department {department.name} added successfully!', 'success')
            return redirect(url_for('main.departments'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_department.html')

@main_bp.route('/department/<int:dept_id>/edit', methods=['GET', 'POST'])
def edit_department(dept_id):
    """Edit department"""
    department = Department.query.get_or_404(dept_id)
    
    if request.method == 'POST':
        try:
            if not request.form.get('name', '').strip():
                flash('Department name is required!', 'danger')
                return render_template('edit_department.html', department=department)
            
            department.name = request.form['name'].strip()
            department.description = request.form.get('description', '').strip()
            db.session.commit()
            flash(f'Department {department.name} updated successfully!', 'success')
            return redirect(url_for('main.departments'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('edit_department.html', department=department)

@main_bp.route('/department/<int:dept_id>/delete', methods=['POST'])
def delete_department(dept_id):
    """Delete department"""
    department = Department.query.get_or_404(dept_id)
    name = department.name
    
    db.session.delete(department)
    db.session.commit()
    flash(f'Department {name} deleted successfully!', 'success')
    return redirect(url_for('main.departments'))

# ============ ATTENDANCE ROUTES ============

@main_bp.route('/attendance')
def attendance():
    """View attendance records"""
    page = request.args.get('page', 1, type=int)
    employee_id = request.args.get('employee_id', type=int)
    
    query = Attendance.query.order_by(Attendance.date.desc())
    if employee_id:
        query = query.filter_by(employee_id=employee_id)
    
    attendance_list = query.paginate(page=page, per_page=20)
    employees = Employee.query.all()
    
    return render_template('attendance.html', 
                         attendance=attendance_list.items,
                         employees=employees,
                         selected_employee=employee_id,
                         page=page)

@main_bp.route('/attendance/add', methods=['GET', 'POST'])
def add_attendance():
    """Add attendance record"""
    employees = Employee.query.all()
    
    if request.method == 'POST':
        try:
            if not all([request.form.get('date'), request.form.get('employee_id'), request.form.get('status')]):
                flash('Date, Employee, and Status are required!', 'danger')
                return render_template('add_attendance.html', employees=employees)
            
            attendance = Attendance(
                date=datetime.strptime(request.form['date'], '%Y-%m-%d').date(),
                status=request.form['status'],
                notes=request.form.get('notes', '').strip(),
                employee_id=int(request.form['employee_id'])
            )
            db.session.add(attendance)
            db.session.commit()
            flash('Attendance record added successfully!', 'success')
            return redirect(url_for('main.attendance'))
        except ValueError as e:
            flash(f'Invalid input: {str(e)}', 'danger')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('add_attendance.html', employees=employees)

@main_bp.route('/api/employees/search')
def search_employees():
    """API endpoint for employee search"""
    query = request.args.get('q', '')
    employees = Employee.query.filter(
        or_(
            Employee.first_name.ilike(f'%{query}%'),
            Employee.last_name.ilike(f'%{query}%'),
            Employee.email.ilike(f'%{query}%')
        )
    ).all()
    
    return jsonify([{
        'id': e.id,
        'name': e.full_name,
        'email': e.email,
        'position': e.position
    } for e in employees])
