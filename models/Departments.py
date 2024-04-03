from database import db




class Department(db.Model):
    __tablename__ = 'departments'

    DepartmentID = db.Column(db.String(50), primary_key=True)
    DepartmentName = db.Column(db.String(100))
    Description = db.Column(db.Text)
    DepartmentHeadID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))

    employees = db.relationship('Employee', back_populates='department')
    department_head = db.relationship('Employee', foreign_keys=[DepartmentHeadID])

    @property
    def department_head_name(self):
        return f"{self.department_head.FirstName} {self.department_head.LastName}" if self.department_head else None

    def __repr__(self):
        return f"Department('{self.DepartmentName}')"
    
    
