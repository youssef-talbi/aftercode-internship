from database import db



class Role(db.Model):
    __tablename__ = 'roles'

    RoleID = db.Column(db.String(50), primary_key=True)
    RoleName = db.Column(db.String(100))
    Description = db.Column(db.Text)

    employees = db.relationship('Employee', back_populates='role')

    def __repr__(self):
        return f"Role('{self.RoleName}')"
    
