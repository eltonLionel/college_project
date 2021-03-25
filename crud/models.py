from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
db =SQLAlchemy()
 
class studentModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(),unique = True)
    fname = db.Column(db.String())
    lname = db.Column(db.String())
    dob = db.Column(db.DateTime, default=datetime.utcnow)
    amt = db.Column(db.Integer())
 
    def __init__(self, student_id,fname,lname,dob,amt):
        self.student_id = student_id
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.amt = amt
 
    def __repr__(self):
        return f"{self.fname}:{self.student_id}"