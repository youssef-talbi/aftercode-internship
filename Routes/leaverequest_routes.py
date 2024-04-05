"""
This module contains the blueprint for the leave request routes.
The routes handle GET, POST, PUT, and DELETE requests for leave requests.
The module also contains docstrings to explain the purpose of each function.
"""

from flask import Blueprint, jsonify, request
from database import db
from database.Models.LeaveRequests import LeaveRequests
from database.Models.Employee import Employee

# Blueprint for the leave request routes
leaverequest_routes = Blueprint('leaverequest_routes', __name__)

# Route to get all leave requests
@leaverequest_routes.route('/leave-requests', methods=['GET'])
def get_all_leave_requests():
    """
    Get all leave requests from the database and return them as a JSON response.
    """
    leave_requests = LeaveRequests.query.all()  # Get all leave requests from the database
    result = []
    for leave_request in leave_requests:  # Convert each leave request to a string representation
        result.append(leave_request.__repr__())
    return jsonify(result)  # Return the result as a JSON response


# Route to get a leave request by ID, employee ID, and name
@leaverequest_routes.route('/leave-requests/<request_id>/employee/<employee_id>/<first_name>-<last_name>', methods=['GET'])
def get_leave_request_by_id_employee_name(request_id, employee_id, first_name, last_name):
    leave_request = LeaveRequests.query.join(Employee).filter(LeaveRequests.request_id == request_id, Employee.employee_id == employee_id, Employee.first_name == first_name, Employee.last_name == last_name).first()
    """
    Get a leave request by ID, employee ID, and name from the database
    and return it as a JSON response. If the leave request is not found, return a 404 error message.
    """
    if leave_request:  # If the leave request is found
        return jsonify(leave_request.__repr__())  # Return the leave request as a JSON response
    return jsonify({'message': 'Leave Request not found'}), 404  # If the leave request is not found, return a 404 error message

# Route to submit a leave request
@leaverequest_routes.route('/leave-requests', methods=['POST'])
def submit_leave_request():
    """
    Submit a leave request by extracting the data from the request body,
    creating a new leave request object, and adding it to the database.
    Return the new leave request as a JSON response.
    """
    data = request.get_json()  # Extract the data from the request body
    employee_id = data.get('employee_id')
    leave_type = data.get('leave_type')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    description = data.get('description')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    employee = Employee.query.filter_by(employee_id=employee_id, first_name=first_name, last_name=last_name).first()
    leave_request = LeaveRequests(employee=employee, leave_type=leave_type, start_date=start_date, end_date=end_date, description=description)  # Create a new leave request object
    db.session.add(leave_request)  # Add the leave request to the database
    db.session.commit()  # Commit the changes to the database
    return jsonify(leave_request.__repr__())  # Return the leave request as a JSON response

# Route to update a leave request
@leaverequest_routes.route('/leave-requests/<request_id>', methods=['PUT'])
@leaverequest_routes.route('/leave-requests/<employee_id>', methods=['PUT'])
@leaverequest_routes.route('/leave-requests/<first_name>-<last_name>', methods=['PUT'])
def update_leave_request(request_id=None, employee_id=None, first_name=None, last_name=None):
    """
    Update a leave request by extracting the data from the request body,
    finding the leave request by ID, employee ID, first name, or last name, updating its attributes, and committing the changes to the database.
    If the leave request is not found, return a 404 error message.
    """
    leave_request = None
    if request_id:
        leave_request = LeaveRequests.query.filter_by(request_id=request_id).first()
    if employee_id:
        leave_request = LeaveRequests.query.join(Employee).filter(Employee.employee_id == employee_id, Employee.first_name == first_name, Employee.last_name == last_name).first()
    if first_name and last_name:
        leave_request = LeaveRequests.query.join(Employee).filter(Employee.first_name == first_name, Employee.last_name == last_name).first()

    if leave_request:  # If the leave request is found
        data = request.get_json()  # Extract the data from the request body
        leave_type = data.get('leave_type')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        description = data.get('description')
        leave_request.leave_type = leave_type  # Update the attributes of the leave request
        leave_request.start_date = start_date
        leave_request.end_date = end_date
        leave_request.description = description
        db.session.commit()  # Commit the changes to the database
        return jsonify(leave_request.__repr__())  # Return the updated leave request as a JSON response
    return jsonify({'message': 'Leave Request not found'}), 404  # If the leave request is not found, return a 404 error message


# Route to cancel a leave request
@leaverequest_routes.route('/leave-requests/<request_id>', methods=['DELETE'])
def cancel_leave_request(request_id):
    """
    Cancel a leave request by finding it by ID, deleting it from the database, and committing the changes.
    If the leave request is not found, return a 404 error message.
    """
    leave_request = LeaveRequests.query.filter_by(request_id=request_id).first()  # Find the leave request by ID
    if leave_request:  # If the leave request is found
        db.session.delete(leave_request)  # Delete the leave request from the database
        db.session.commit()  # Commit the changes to the database
        return jsonify({'message': 'Leave Request cancelled successfully'})  # Return a success message
    return jsonify({'message': 'Leave Request not found'}), 404  # If the leave request is not found, return a 404 error message

