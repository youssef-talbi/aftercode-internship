from database import db

from sqlalchemy import TIMESTAMP,func




class AuditTrail(db.Model):
    __tablename__ = 'audit_trail'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))  # Correct the table name to 'employees' and the column name to 'employee_id'
    action = db.Column(db.String(50))
    created_at = db.Column(TIMESTAMP, server_default=func.now())
    updated_at = db.Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    employee = db.relationship('Employee', back_populates='audit_trail')

    def __repr__(self):
        return f'AuditTrail(id={self.id}, employee_id={self.employee_id}, action={self.action}, created_at={self.created_at}, updated_at={self.updated_at})'
    
