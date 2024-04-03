from database import db
from sqlalchemy import TIMESTAMP

class CommunicationLogs(db.Model):
    __tablename__ = 'CommunicationLogs'
    LogID = db.Column(db.String(50), primary_key=True)
    SenderID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    ReceiverID = db.Column(db.String(50), db.ForeignKey('employees.employee_id'))
    MessageType = db.Column(db.String(50))
    MessageContent = db.Column(db.String(255))
    Timestamp = db.Column(TIMESTAMP)
    sender = db.relationship("Employee", foreign_keys=[SenderID])
    receiver = db.relationship("Employee", foreign_keys=[ReceiverID])