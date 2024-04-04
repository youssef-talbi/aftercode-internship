from database import db
class PayrollDetails(db.Model):
    __tablename__ = 'payroll_details'
    payroll_id = db.Column(db.String(50), primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('employees.employee_id'), nullable=False)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    salary_details = db.Column(db.Numeric(10, 2))

    employee = db.relationship('Employee', backref='payroll_details', foreign_keys=[employee_id])

    @property
    def employee_name(self):
        return '{} {}'.format(self.employee.first_name, self.employee.last_name)


