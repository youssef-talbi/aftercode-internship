from app import db

class Employee(db.Model):
    __tablename__ = 'Employees'
    EmployeeID = db.Column(db.Text, primary_key=True)
    FirstName = db.Column(db.Text)
    LastName = db.Column(db.Text)
    Email = db.Column(db.Text)
    Phone = db.Column(db.Text)
    JobTitle = db.Column(db.Text)
    DepartmentID = db.Column(db.Text)
    RoleID = db.Column(db.Text)

