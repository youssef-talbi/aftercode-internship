from database import db
class LeaveRequests(db.Model):
    __tablename__ = 'leave_requests'
    request_id = db.Column(db.String(50), primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('employees.employee_id'), nullable=False)
    leave_type = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(50))
    description = db.Column(db.String(255))
    employee = db.relationship('Employee', backref='leave_requests')

    def __repr__(self):
        employee_name = f"{self.employee.first_name} {self.employee.last_name}"
        return f"Leave Request(Employee ID: {self.employee_id}, Employee Name: {employee_name}, Leave Type: {self.leave_type}, Start Date: {self.start_date}, End Date: {self.end_date}, Description: {self.description})"
