from flask import Blueprint, jsonify, request
from database import db
from database.Models.Employee import Employee

# Creating a blueprint for the employee module
employee_bp = Blueprint('employee', __name__)

# Route to get all employees
@employee_bp.route('/employees', methods=['GET'])
def get_all_employees():
    """
    This route retrieves all the employees from the database and returns them as a JSON response.
    """
    # Querying the database to get all employees
    employees = Employee.query.all()
    # Converting each employee to a JSON object
    employees_list = [employee.to_json() for employee in employees]
    # Returning the list of employees as a JSON response
    return jsonify(employees_list)

# Route to get an employee by ID
@employee_bp.route('/employees/<employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    """
    This route retrieves an employee from the database by their ID and returns them as a JSON response.
    """
    # Querying the database to get an employee by ID
    employee = Employee.query.get(employee_id)
    # If the employee is found, return it as a JSON response
    if employee:
        return jsonify(employee.to_json())
    # If the employee is not found, return an error message with a 404 status code
    return jsonify({'message': 'Employee not found'}), 404

# Route to add a new employee
@employee_bp.route('/employees', methods=['POST'])
def add_employee():
    """
    This route adds a new employee to the database by extracting the data from the request body and creating a new employee object.
    """
    # Extracting the data from the request body
    data = request.get_json()
    # Creating a new employee object using the data
    new_employee = Employee(**data)
    # Adding the new employee to the database session
    db.session.add(new_employee)
    # Committing the changes to the database
    db.session.commit()
    # Returning the new employee as a JSON response with a 201 status code
    return jsonify(new_employee.to_json()), 201

# Route to update an employee by ID
@employee_bp.route('/employees/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    """
    This route updates an employee in the database by their ID by extracting the data from the request body and updating the employee's attributes.
    """
    # Extracting the data from the request body
    data = request.get_json()
    # Querying the database to get an employee by ID
    employee = Employee.query.get(employee_id)
    # If the employee is found, updating its attributes with the data
    if employee:
        for key, value in data.items():
            setattr(employee, key, value)
        # Committing the changes to the database
        db.session.commit()
        # Returning the updated employee as a JSON response
        return jsonify(employee.to_json())
    # If the employee is not found, return an error message with a 404 status code
    return jsonify({'message': 'Employee not found'}), 404

# Route to delete an employee by ID
@employee_bp.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    """
    This route deletes an employee from the database by their ID.
    """
    # Querying the database to get an employee by ID
    employee = Employee.query.get(employee_id)
    # If the employee is found, deleting it from the database
    if employee:
        db.session.delete(employee)
        # Committing the changes to the database
        db.session.commit()
        # Returning a success message as a JSON response
        return jsonify({'message': 'Employee deleted'})
    # If the employee is not found, return an error message with a 404 status code
    return jsonify({'message': 'Employee not found'}), 404

# End of employee module

