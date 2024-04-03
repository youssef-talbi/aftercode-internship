from Models.AuditTrail import AuditTrail
from database import db
from datetime import datetime

class UserPermissions(db.Model):
    __tablename__ = 'user_permissions'
    
    UserID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'), primary_key=True)
    RoleID = db.Column(db.String(50), db.ForeignKey('roles.RoleID'), primary_key=True)
    
    audit_trail = db.relationship('AuditTrail', primaryjoin='and_(UserPermissions.UserID==AuditTrail.employee_id, AuditTrail.action=="Added User Permission")', viewonly=True)
    
    def add_log(self):
        audit = AuditTrail(employee_id=self.UserID, action="Added User Permission")
        db.session.add(audit)
        
    def delete_log(self):
        audit = AuditTrail(employee_id=self.UserID, action="Deleted User Permission")
        db.session.add(audit)
