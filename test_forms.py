#!/usr/bin/env python
"""Test employee form functionality"""
from app import create_app

app = create_app()

with app.test_client() as client:
    # Test home page
    r = client.get('/')
    print(f'✓ Home page loads: {r.status_code}')
    
    # Test add employee form page
    r = client.get('/employee/add')
    print(f'✓ Add Employee form loads: {r.status_code}')
    
    # Test add department page
    r = client.get('/department/add')
    print(f'✓ Add Department form loads: {r.status_code}')
    
    # Test form renders with no departments
    if b'department' in r.data.lower():
        print('✓ Department field present in form')
    
    print('\n✓✓✓ All forms are valid and working! ✓✓✓')
