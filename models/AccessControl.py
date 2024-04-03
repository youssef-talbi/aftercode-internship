from database   import db
from sqlalchemy import func, TIMESTAMP
class AccessControlLogs(db.Model):
    __tablename__ = 'access_control_logs'

    LogID = db.Column(db.String(50), primary_key=True)
    EmployeeID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    ActionType = db.Column(db.String(50))
    Timestamp = db.Column(TIMESTAMP, server_default=func.now())

    employee = db.relationship('Employee', backref='access_control_logs')

    def __repr__(self):
        return f"AccessControlLog ( LogID: {self.LogID}, Employee Name: {self.employee.first_name} {self.employee.last_name}, ActionType: {self.ActionType}"
