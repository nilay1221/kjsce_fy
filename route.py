from flask import Flask,render_template, flash, redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from form import register

app = Flask(__name__,template_folder='D:/Nilay pycharm/kjsce_fy/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/kjsce_contact'
app.secret_key = 'development key'
db = SQLAlchemy(app)

class contact(db.Model):
	sno=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(50),nullable=False)
	email=db.Column(db.String(20),nullable=False)
	phone_num=db.Column(db.String(12),nullable=False)
	msg=db.Column(db.String(500),nullable=False)

@app.route('/')
def home_page():
   return render_template('index.html',)
@app.route('/contact',methods=['GET','POST'])
def contact_page():
   form=register()
   if form.validate_on_submit():
      flash('Succesfully Submited')
      if(request.method=='POST'):
         name=request.form.get('name')
         email=request.form.get('email')
         phone_num=request.form.get('phone')
         message=request.form.get('message')
         entry=contact(name=name,email=email,phone_num=phone_num,msg=message)
         db.session.add(entry)
         db.session.commit()
      return render_template('contact_us.html',form=form)
   else:
      # flash('Please Try Again')
      return render_template('contact_us.html',form=form)

app.run(debug=True)