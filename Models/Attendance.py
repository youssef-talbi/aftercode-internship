from database import db

class attendance(db.Model):
    attendance_id = db.Column(db.String(50), primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('employees.employee_id'), nullable=False)
    clockintime = db.Column(db.DateTime)
    clockouttime = db.Column(db.DateTime)
    employee = db.relationship('Employee', backref='attendances', primaryjoin='attendance.employee_id == Employee.employee_id')

    def __repr__(self):
        employee_name = self.employee.first_name + ' ' + self.employee.last_name
        return f"attendance('{self.employee_id}', '{employee_name}', '{self.clockintime}', '{self.clockouttime}')"

