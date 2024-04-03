from flask import Flask
from database import db


app = Flask(__name__)

# Configure MySQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hr_db'  # Replace root with your MySQL username, and add the password if required
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from Models import Employee, Departments,Roles,AuditTrail
from Models import Performance,UserPermissions,LeaveRequests,Training,Attendance
from Models import AccessControl,CommunicationLogs
from Models import BenefitProgram,BenefitSelection,Payroll

if __name__ == '__main__':
    with app.app_context():
        with app.app_context():
            db.create_all()
            # Add the following lines to include the AccessControl and CommunicationLogs models explicitly
            db.reflect()
            db.create_all()