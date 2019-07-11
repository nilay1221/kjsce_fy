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

ref=[
    {
    'sub':'Applied Mathematics 1',
    'group':'Group P and C',
    'b1':'Higher Engineering Mathematics',
    'b2':'Advanced Engineering Mathematics',
    'b3':'A Textbook of Applied Mathematics',
    'l1':'https://www.amazon.in/Higher-Engineering-Mathematics-B-S-Grewal/dp/8193328493',
    'l2':'https://www.amazon.in/Advanced-Engineering-Mathematics-Erwin-Kreyszig/dp/8126531355',
    'l3':'https://www.amazon.in/textbook-ApplIed-Mathematics-P-N-Wartikar/dp/B01MT1DA5E'
    },
    {
    'sub': 'Engineering Mechanics',
    'group':'Group P',
    'b1':'Engineering Mechanics',
    'b2':'Engineering Mechanics, Statics and Dynamics',
    'b3':'Foundations and Applications of Engineering Mechanics',
    'l1':'https://www.amazon.in/Engineering-Mechanics-Basudeb-Bhattacharyya/dp/0198096321',
    'l2':'https://www.amazon.in/Engineering-Mechanics-Statics-Dynamics-11e/dp/8131726991', 
    'l3':'https://www.amazon.in/Foundations-Applications-Engineering-Mechanics-Ram/dp/1107499836'   
    },
    {
    'sub':'Engineering Physics',
    'group':'Group P',
    'b1':'A Textbook of Engineering Physics',
    'b2':'Introduction to Solid State Physics',
    'b3':'Quantum Mechanics',
    'l1':'https://www.amazon.in/Textbook-Engineering-Physics-Old/dp/8121908175',
    'l2':'https://www.amazon.in/Introduction-Solid-State-Physics-8ed/dp/8126535180',
    'l3':'https://www.amazon.com/Quantum-Mechanics-2nd-B-H-Bransden/dp/0582356911'
    },
    {
    'sub':'Engineering Chemistry',
    'group':'Group C',
    'b1':'A Textbook of Engineering Chemistry',
    'b2':'Engineering Chemistry',
    'l1':'https://www.amazon.in/Textbook-Engineering-Chemistry-SS-Dara/dp/8121903599',
    'l2':'https://www.amazon.in/Engineering-Chemistry-Maheswaramma-Chugh/dp/933257118X?tag=googinhydr18418-21&tag=googinkenshoo-21&ascsubtag=_k_EAIaIQobChMInLjJxbCq4wIVlhmPCh3RswIFEAQYASABEgLTa_D_BwE_k_&gclid=EAIaIQobChMInLjJxbCq4wIVlhmPCh3RswIFEAQYASABEgLTa_D_BwE',
    },
    {
    'sub': 'Engineering Drawing',
    'group':'Group C',
    'b1':'Engineering Drawing (Plane and Solid Geometry)',
    'b2':'Engineering Graphics',
    'b3':'Engineering Graphics and Drafting',
    'l1':'https://www.amazon.in/Engineering-Drawing-Plane-Solid-Geometry/dp/9380358172',
    'l2':'https://www.amazon.in/Textbook-Engineering-Graphics-Shah-P-J/dp/8121929679',
    'l3':'https://www.amazon.in/Engineering-Graphics-Drafting-P-S-Gill/dp/8185749612'
    },
    {   
    'sub':'Elements of Electronics and Electrical Engineering',
    'group':'Group C',
    'b1':'Basics of Electrical and Electronics Engineering : B.R. Patil',
    'b2':'Basics of Electrical and Electronics Engineering : Ravish Singh',
    'l1':'https://www.amazon.in/Basic-Electrical-Electronics-Engineering-Patil/dp/0199469377/ref=sr_1_1?qid=1562763663&refinements=p_27%3ABR+PATIL&s=books&sr=1-1',
    'l2':'https://www.amazon.in/Basic-Electrical-Engineering-Ravish-Singh/dp/935316172X/ref=sr_1_4?qid=1562763733&refinements=p_27%3ARavish+Singh&s=books&sr=1-4'
    },
    {
    'sub':'Programming in C',
    'group':'Group P',
    'b1':'Programming in ANSI C',
    'b2':'Let us C',
    'b3':'Structured Programming Approach',
    'l1':'https://www.amazon.in/Programming-ANSI-C-Balagurusamy/dp/933921966X',
    'l2':'https://www.amazon.in/Let-Us-C-Yashavant-Kanetkar/dp/8183331637',
    'l3':'https://www.amazon.in/Structured-Programming-Approach-University-Mumbai/dp/0199475520'
    },
    {
    'sub': 'Applied Mathematics 2',
    'group':'Group P and C',
    'b1':'Higher Engineering Mathematics',
    'b2':'Advanced Engineering Mathematics',
    'b3':'A Textbook of Applied Mathematics',
    'l1':'https://www.amazon.in/Higher-Engineering-Mathematics-B-S-Grewal/dp/8193328493',
    'l2':'https://www.amazon.in/Advanced-Engineering-Mathematics-Erwin-Kreyszig/dp/8126531355',
    'l3':'https://www.amazon.in/textbook-ApplIed-Mathematics-P-N-Wartikar/dp/B01MT1DA5E'
    },
    {
    'sub': 'Communication Skills',
    'group':'Group C',
    'b1':'Communication Skills',
    'b2':'Basic Business Communication',
    'l1':'https://www.amazon.in/Communication-Skills-GU-Meenakshi-Raman/dp/0198078781',
    'l2':'https://www.amazon.in/Basic-Business-Communication-Raymond-Lesikar/dp/0072397616'
    },
    {
    'sub':'Environmental Studies',
    'group':'Group P',
    'b1':'Perspectives in Environmental Studies',
    'b2':'Environmental Impact Assessment Methodologies',
    'l1':'https://www.amazon.in/Perspectives-Environmental-Studies-2018-19-Session/dp/9386418630',
    'l2':'https://www.amazon.in/Environmental-Impact-Assessment-Methodologies-Anjaneyulu/dp/0415665566'
    }

]



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
@app.route("/books")
def books():
    return render_template('books.html', ref=ref, title='Books')




@app.route("/about")
def about():
    return render_template('about.html')

app.run(debug=True)