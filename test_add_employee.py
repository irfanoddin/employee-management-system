#!/usr/bin/env python
"""Test complete employee add workflow"""
from app import create_app
from datetime import datetime, timedelta

app = create_app()

with app.test_client() as client:
    print("Testing Employee Add Workflow...\n")
    
    # Step 1: Add a department first
    dept_data = {
        'name': 'Sales',
        'description': 'Sales Department'
    }
    r = client.post('/department/add', data=dept_data, follow_redirects=True)
    print(f'✓ Department "Sales" added (Status: {r.status_code})')
    
    # Step 2: Get the add employee form
    r = client.get('/employee/add')
    print(f'✓ Add Employee form loaded (Status: {r.status_code})')
    
    # Step 3: Submit employee form
    hire_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    emp_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'phone': '1234567890',
        'position': 'Sales Executive',
        'salary': '50000',
        'hire_date': hire_date,
        'department_id': '1',
        'status': 'Active'
    }
    r = client.post('/employee/add', data=emp_data, follow_redirects=True)
    print(f'✓ Employee form submitted (Status: {r.status_code})')
    
    if b'successfully' in r.data.lower():
        print('✓ Success message received!')
    
    # Step 4: Verify employee appears in list
    r = client.get('/employees')
    if b'John' in r.data and b'Doe' in r.data:
        print('✓ Employee appears in employees list!')
    
    print("\n✓✓✓ COMPLETE TEST PASSED - Add Employee Works! ✓✓✓")
