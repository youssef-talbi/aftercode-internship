from database import db
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy import func, TIMESTAMP


class TrainingPrograms(db.Model):
    __tablename__ = 'training_programs'
    
    ProgramID = db.Column(db.String (50), primary_key=True)
    ProgramName = db.Column(db.String(100))
    Trainer = db.Column(db.String(100))
    Schedule = db.Column(db.String(100))
    Description = db.Column(db.Text)
    Status = db.Column(db.String(50))
    StartDate = db.Column(db.TIMESTAMP)
    EndDate = db.Column(db.TIMESTAMP)
    TrainingType = db.Column(db.String(50))
    Cost = db.Column(db.String(50))
    EmployeeID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    EmployeeName = db.Column(db.String(100))
    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.now())


