from database import db
class PerformanceGoals(db.Model):
    __tablename__ = 'performance_goals'
    goal_id = db.Column(db.String(50), primary_key=True)
    employee_id = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    goal_description = db.Column(db.Text)
    deadline = db.Column(db.Date)
    status = db.Column(db.String(50))
    employee = db.relationship('Employee', backref='performance_goals', primaryjoin='PerformanceGoals.employee_id == Employee.employee_id')

    def __repr__(self):
        return f"Goal(Goal ID: {self.goal_id}, Employee Name: {self.employee.first_name} {self.employee.last_name}, Goal Description: {self.goal_description}, Deadline: {self.deadline}, Status: {self.status})"
