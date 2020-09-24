# -----------------------------------------------------------
# Creating a webapp with a database back-end and email support using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------
 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email                 #Our python code file and function.
from sqlalchemy import func

# Create a Flask instance.
app=Flask(__name__)

# Pass the database URI to the flask instance.
# username: postgres 
# password: password123
# server address: localhost
# database name: height_collector
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password123@localhost/height_collector'

#Create SQLAlchemy object for your flash application.
db=SQLAlchemy(app)

#Create a class specifying properties of the Database.
class Database(db.Model):
    __tablename__="height data"
    SLNo=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150), unique=True)
    height=db.Column(db.Integer)
    
    def __init__(self,email,height):
        self.email=email
        self.height=height   
    

#Home page of the website.
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["emailid"]
        height=request.form["height"]
        if db.session.query(Database).filter(Database.email==email).count()==0:  #If the email input by user doesn't exist in the database already.
            data=Database(email,height)
            db.session.add(data)              #Insert user-data to the database.
            db.session.commit()               #Commit the changes.
            average=db.session.query(func.avg(Database.height)).scalar()   #Finding the average of heights.
            average=round(average,1)
            count=db.session.query(Database.height).count()                #Getting the number of rows.
            send_email(email,height,average,count)
            return render_template("success.html")
        else:                                                                  #If the email input by user already exist in the database.
            return render_template("index.html",text="You have already submitted your response!")
            
        

if __name__=="__main__":
    app.run(debug=True)
