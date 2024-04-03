from database import db
from sqlalchemy import TIMESTAMP,func

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
    DepartmentID = db.Column(db.String(50), db.ForeignKey('departments.DepartmentID'))
    RoleID = db.Column(db.String(50), db.ForeignKey('roles.RoleID'))
    department = db.relationship('Department', back_populates='employees')
    role = db.relationship('Role', back_populates='employees')
    
    def __repr__(self):
        return f"Employee('{self.FirstName}', '{self.LastName}')"

