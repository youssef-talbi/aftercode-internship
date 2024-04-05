from flask import Blueprint, jsonify, request
from database import db
from database.Models.Training import TrainingPrograms

# Creating blueprint for our routes, named 'traininprog_routes'
traininprog_routes = Blueprint('traininprog_routes', __name__)

# Route to get all training programs
@traininprog_routes.route('/training-programs', methods=['GET'])
def get_all_training_programs():
    # Querying the database to get all training programs
    training_programs = TrainingPrograms.query.all()
    
    # Creating a list to store serialized training programs
    result = []
    
    # Looping through all training programs and appending their serialized form to the list
    for training_program in training_programs:
        result.append(training_program.serialize())
    
    # Returning the serialized training programs as a JSON response
    return jsonify(result)

# Route to get a specific training program by its ID
@traininprog_routes.route('/training-programs/<program_id>', methods=['GET'])
def get_training_program(program_id):
    # Querying the database to get a specific training program by its ID
    training_program = TrainingPrograms.query.get(program_id)
    
    # If the training program exists, return its serialized form as a JSON response
    if training_program:
        return jsonify(training_program.serialize())
    
    # If the training program does not exist, return an error message as a JSON response with a 404 status code
    return jsonify({'error': 'Training program not found'}), 404

# Route to add a new training program
@traininprog_routes.route('/training-programs', methods=['POST'])
def add_training_program():
    # Getting the JSON data from the request body
    data = request.get_json()
    
    # Creating a new TrainingPrograms object using the data
    training_program = TrainingPrograms(**data)
    
    # Adding the new training program to the database session
    db.session.add(training_program)
    
    # Committing the changes to the database
    db.session.commit()
    
    # Returning the serialized new training program as a JSON response with a 201 status code
    return jsonify(training_program.serialize()), 201

# Route to update a specific training program by its ID
@traininprog_routes.route('/training-programs/<program_id>', methods=['PUT'])
def update_training_program(program_id):
    # Querying the database to get a specific training program by its ID
    training_program = TrainingPrograms.query.get(program_id)
    
    # If the training program exists, update its attributes with the data from the request body
    if training_program:
        data = request.get_json()
        training_program.ProgramID = data.get('ProgramID', training_program.ProgramID)
        training_program.ProgramName = data.get('ProgramName', training_program.ProgramName)
        training_program.Trainer = data.get('Trainer', training_program.Trainer)
        training_program.Schedule = data.get('Schedule', training_program.Schedule)
        training_program.Description = data.get('Description', training_program.Description)
        training_program.Status = data.get('Status', training_program.Status)
        training_program.StartDate = data.get('StartDate', training_program.StartDate)
        training_program.EndDate = data.get('EndDate', training_program.EndDate)
        training_program.TrainingType = data.get('TrainingType', training_program.TrainingType)
        training_program.Cost = data.get('Cost', training_program.Cost)
        training_program.EmployeeID = data.get('EmployeeID', training_program.EmployeeID)
        training_program.EmployeeName = data.get('EmployeeName', training_program.EmployeeName)
        
        # Committing the changes to the database
        db.session.commit()
        
        # Returning the serialized updated training program as a JSON response
        return jsonify(training_program.serialize())
    
    # If the training program does not exist, return an error message as a JSON response with a 404 status code
    return jsonify({'error': 'Training program not found'}), 404

# Route to delete a specific training program by its ID
@traininprog_routes.route('/training-programs/<program_id>', methods=['DELETE'])
def delete_training_program(program_id):
    # Querying the database to get a specific training program by its ID
    training_program = TrainingPrograms.query.get(program_id)
    
    # If the training program exists, delete it from the database
    if training_program:
        db.session.delete(training_program)
        db.session.commit()
        
        # Returning a success message as a JSON response
        return jsonify({'message': 'Training program deleted'})
    
    # If the training program does not exist, return an error message as a JSON response with a 404 status code
    return jsonify({'error': 'Training program not found'}), 404


