from flask import Flask,render_template,request,redirect
from models import db,studentModel
from datetime import datetime
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    return render_template('homepage.html')
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        dob1 = datetime.strptime(dob, '%Y-%m-%d').date()
        amt = request.form['amt']
        student = studentModel(student_id = student_id,fname = fname,lname = lname,dob = dob1,amt =amt)
        db.session.add(student)
        db.session.commit()
        return redirect('/data')
 
@app.route('/data', methods=['GET','POST'])
def RetrieveList():
    students = studentModel.query.all()
    if request.method == 'GET':
        return render_template('datalist.html',students = students)
    
    if request.method == 'POST':
        id = request.form['student_id']
        return redirect(f'/data/{id}')
 
@app.route('/data/<int:id>')
def Retrievestudent(id):
    student = studentModel.query.filter_by(student_id=id).first()
    if student:
        return render_template('data.html', student = student)
    return f"Student with id ={id} Doenst exist"

@app.route('/data/update/', methods=['GET','POST'])
def update1():
    students = studentModel.query.all()
    if request.method == 'GET':
        return render_template('update1.html',students = students)

    if request.method == 'POST':
        id = request.form['student_id']
        return redirect(f'/data/update/{id}')
 
@app.route('/data/update/<int:id>',methods = ['GET','POST'])
def update(id):
    student = studentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            fname = request.form['fname']
            lname = request.form['lname']
            dob = request.form['dob']
            amt = request.form['amt']
            student = studentModel(student_id = id,fname = fname,lname = lname,dob = dob,amt =amt)
            db.session.add(student)
            db.session.commit() 
            return redirect(f'/data/{id}')
        return f"Student with id = {id} Does nit exist"
 
    return render_template('update.html', student = student)
 

@app.route('/data/delete/', methods=['GET','POST'])
def delete1():
    students = studentModel.query.all()
    if request.method == 'GET':
        return render_template('delete1.html',students = students)

    if request.method == 'POST':
        id = request.form['student_id']
        return redirect(f'/data/delete/{id}')

@app.route('/data/delete/<int:id>', methods=['GET','POST'])
def delete(id):
    student = studentModel.query.filter_by(student_id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/data')
        abort(404)
    return render_template('delete.html')
 
if __name__ == "__main__":

	app.run(debug=True)
