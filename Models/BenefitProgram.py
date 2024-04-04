# BenefitPrograms Table
from database import db
class BenefitPrograms(db.Model):
    __tablename__ = 'BenefitPrograms'
    
    ProgramID = db.Column(db.String(50), primary_key=True)
    ProgramName = db.Column(db.String(100))
    Description = db.Column(db.Text)

