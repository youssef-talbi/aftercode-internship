from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import TIMESTAMP, func

app = Flask(__name__)

# Configure MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hr_db'  # Replace root with your MySQL username, and add the password if required
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'  # Specify the table name explicitly

    employee_id = db.Column(db.String(50), unique=True, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    phone = db.Column(db.String(20), unique = True, nullable = False)
    job_title = db.Column(db.String(100), nullable = False)
    shift_time = db.Column(TIMESTAMP)  # Use TIMESTAMP type
    created_at = db.Column(TIMESTAMP, server_default=func.now())
    updated_at = db.Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    DepartmentID = db.Column(db.Integer, db.ForeignKey('departments.DepartmentID'))
    RoleID = db.Column(db.Integer, db.ForeignKey('roles.RoleID'))
    department = db.relationship('Department', back_populates='employees')
    role = db.relationship('Role', back_populates='employees')
    
    def __repr__(self):
        return f"Employee('{self.FirstName}', '{self.LastName}')"

class Department(db.Model):
    __tablename__ = 'departments'

    DepartmentID = db.Column(db.Integer, primary_key=True)
    DepartmentName = db.Column(db.String(100))
    Description = db.Column(db.Text)
    DepartmentHeadID = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))

    employees = db.relationship('Employee', back_populates='department')
    department_head = db.relationship('Employee', foreign_keys=[DepartmentHeadID])

    @property
    def department_head_name(self):
        return f"{self.department_head.FirstName} {self.department_head.LastName}" if self.department_head else None

    def __repr__(self):
        return f"Department('{self.DepartmentName}')"

class Role(db.Model):
    __tablename__ = 'roles'

    RoleID = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(100))
    Description = db.Column(db.Text)

    employees = db.relationship('Employee', back_populates='role')

    def __repr__(self):
        return f"Role('{self.RoleName}')"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
