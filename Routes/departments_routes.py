from flask import jsonify, request
from flask_restful import Resource
from flask import Blueprint
import sys

sys.path.insert(0, 'c:/Users/youssef/Desktop/hrsystem-aftercode/hrsystem_backend/database/Models')
sys.path.insert(0, 'c:/Users/youssef/Desktop/hrsystem-aftercode/hrsystem_backend/database/Models')
sys.path.insert(0, 'c:/Users/youssef/Desktop/hrsystem-aftercode/hrsystem_backend/database')

import database

departments_routes = Blueprint('departments_routes', __name__)

@departments_routes.route('/departments', methods=['GET'])
def get_all_departments():
    departments = database.Models.Departments.query.all()
    departments_data = [department.__repr__() for department in departments]
    return jsonify({'departments': departments_data})

@departments_routes.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    department = Departments.query.get_or_404(department_id)
    return jsonify({'department': department.__repr__()})

@departments_routes.route('/departments', methods=['POST'])
def add_department():
    data = request.get_json()
    department_name = data.get('department_name')
    description = data.get('description')
    department_head_name = data.get('department_head_name')
    department_head_id = data.get('department_head_id')
    
    # Check if department head exists as an employee
    existing_employee = db.session.query(Employee).filter_by(EmployeeID=department_head_id).first()
    if existing_employee:
        # If existing, use his first name and last name
        department_head_first_name = existing_employee.FirstName
        department_head_last_name = existing_employee.LastName
    else:
        # If not existing, add him as a new employee
        new_employee = Employee(EmployeeID=department_head_id, FirstName=department_head_name.split(' ')[0], LastName=department_head_name.split(' ')[1])
        db.session.add(new_employee)
        db.session.commit()
        department_head_first_name = new_employee.FirstName
        department_head_last_name = new_employee.LastName

    department = Departments(DepartmentName=department_name, Description=description, DepartmentHeadID=department_head_id, DepartmentHeadFirstName=department_head_first_name, DepartmentHeadLastName=department_head_last_name)
    db.session.add(department)
    db.session.commit()
    return jsonify({'message': 'Department and department head added successfully', 'department': department.__repr__()}), 201
@departments_routes.route('/departments/<int:department_id>', methods=['PUT'])
def update_department(department_id):
    data = request.get_json()
    department = Departments.query.get_or_404(department_id)
    department.DepartmentName = data.get('department_name', department.DepartmentName)
    department.Description = data.get('description', department.Description)
    department.DepartmentHeadID = data.get('department_head_id', department.DepartmentHeadID)
    db.session.commit()
    return jsonify({'message': 'Department updated successfully', 'department': department.__repr__()}), 200

@departments_routes.route('/departments/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    department = Departments.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()
    return jsonify({'message': 'Department deleted successfully'}), 200

