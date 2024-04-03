from database import db

class BenefitSelections(db.Model):
    __tablename__ = 'BenefitSelections'
    SelectionID = db.Column(db.String(50), primary_key=True)
    EmployeeID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    ProgramID = db.Column(db.String(50), db.ForeignKey('BenefitPrograms.ProgramID'))
    SelectionDetails = db.Column(db.Text)

    employee = db.relationship('Employee', back_populates='benefit_selections', foreign_keys=[EmployeeID])
    program = db.relationship('BenefitProgram', back_populates='selections', foreign_keys=[ProgramID])

    @property
    def employee_name(self):
        return f'{self.employee.first_name} {self.employee.last_name}'

    def __repr__(self):
        return f"BenefitSelections('{self.SelectionID}', '{self.employee_name}', '{self.ProgramID}', '{self.SelectionDetails}')"