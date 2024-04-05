from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from database import db, ma
from database.Models.Roles import Role

# Create a blueprint for the roles endpoint
roles_bp = Blueprint('roles', __name__)

# Define a schema for the Role model
class RoleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Role
        include_fk = True  # Include foreign key columns
        load_instance = True  # Load instances of the model

    RoleID = ma.auto_field()  # Automatically map the RoleID field
    RoleName = ma.auto_field()  # Automatically map the RoleName field
    Description = ma.auto_field()  # Automatically map the Description field

# Define a GET route for the '/roles' endpoint
@roles_bp.route('/roles', methods=['GET'])
def get_all_roles():
    # Query all roles
    roles = Role.query.all()
    # Create a schema for the roles
    roles_schema = RoleSchema(many=True)
    # Dump the roles as JSON
    return jsonify(roles_schema.dump(roles))

# Define a GET route for the '/roles/<role_id>' endpoint
@roles_bp.route('/roles/<role_id>', methods=['GET'])
def get_role_by_id(role_id):
    # Query a role by its ID
    role = Role.query.get_or_404(role_id)
    # Create a schema for the role
    role_schema = RoleSchema()
    # Dump the role as JSON
    return jsonify(role_schema.dump(role))

# Define a POST route for the '/roles' endpoint
@roles_bp.route('/roles', methods=['POST'])
def add_role():
    # Get the JSON data from the request
    role_data = request.get_json()
    # Create a new Role instance
    role = Role(RoleID=role_data['RoleID'], RoleName=role_data['RoleName'], Description=role_data.get('Description'))
    # Add the role to the database session
    db.session.add(role)
    # Commit the changes
    db.session.commit()
    # Create a schema for the role
    role_schema = RoleSchema()
    # Dump the role as JSON and return a 201 status code
    return jsonify(role_schema.dump(role)), 201

# Define a PUT route for the '/roles/<role_id>' endpoint
@roles_bp.route('/roles/<role_id>', methods=['PUT'])
def update_role(role_id):
    # Get the JSON data from the request
    role_data = request.get_json()
    # Query a role by its ID
    role = Role.query.get_or_404(role_id)
    # Update the role attributes
    role.RoleID = role_data['RoleID']
    role.RoleName = role_data['RoleName']
    role.Description = role_data.get('Description')
    # Commit the changes
    db.session.commit()
    # Create a schema for the role
    role_schema = RoleSchema()
    # Dump the role as JSON and return it
    return jsonify(role_schema.dump(role))

# Define a DELETE route for the '/roles/<role_id>' endpoint
@roles_bp.route('/roles/<role_id>', methods=['DELETE'])
def delete_role(role_id):
    # Query a role by its ID
    role = Role.query.get_or_404(role_id)
    # Delete the role from the database session
    db.session.delete(role)
    # Commit the changes
    db.session.commit()
    # Return a success message
    return jsonify({'message': 'Role deleted successfully'})

