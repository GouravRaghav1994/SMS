from flask import *
from flask_mysqldb import MySQL
import yaml
from yaml.loader import SafeLoader
import pandas as pd
from datetime import datetime

app = Flask(__name__)

app.secret_key = "secret key"
#configure db
db = yaml.load(open('db.yaml'), Loader=SafeLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        ty=request.form['type']
        name=request.form['username'];
        cur = mysql.connection.cursor()
        if ty == 'staff':
            result = cur.execute("SELECT * FROM userAdmin WHERE username=%s",(name,))
        else:
            result = cur.execute("SELECT * FROM userstudent WHERE username=%s",(name,))
        if result > 0:
            user = cur.fetchone();
            if request.form['password']==user[2]:
                session['sno']= user[1]
                if ty == 'staff':
                    return redirect(url_for('dashboard'))
                else:
                    return 'student Dashboard'
            else:
                return 'password do not match';
        else:
            return 'no user exist'

    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'sno' in session:
        return render_template('dashboard.html')
    
    return redirect('/') 

@app.route('/view-staff',methods=['GET','POST'])
def view_staff():
    if 'sno' in session:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM userAdmin")
        if result > 0:
            user = cur.fetchall()
            print(user)
        return render_template('view-staff.html', data=user, msg=request.args.get('msg'))
    return redirect('/')

@app.route('/view-student',methods=['GET','POST'])
def view_student():
    if 'sno' in session:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM userstudent")
        if result > 0:
            user = cur.fetchall()
            print(user)
        return render_template('view-student.html', data=user, msg=request.args.get('msg'))
    return redirect('/')

@app.route('/add-staff', methods=['GET','POST'])
def add_staff():
    if 'sno' in session:
        if request.method=='POST':
            first=request.form['firstName']
            middle=request.form['middleName']
            last= request.form['lastName']
            gender=request.form['gender']
            dob=request.form['dateOfBirth']
            mobile=request.form['mobileNo']
            email=request.form['email']
            desig=request.form['designation']
            pincode=request.form['pincode']
            house=request.form['houseNo']
            address=request.form['address']
            city=request.form['city']
            state=request.form['state']
            ifsc=request.form['ifscode']
            actNo=request.form['acntNo']
            bank=request.form['bankName']
            branch=request.form['branch']
            pan=request.form['panNo']
            quali=request.form['qualification']
            join=request.form['joinDate']
            salary=request.form['salary']
            contract=request.form['contactType']
            work=request.form['workSft']
            txt=dob.split('-')
            username=first+txt[0]
            cur = mysql.connection.cursor()
            sql= "INSERT INTO `useradmin` (`username`, `password`, `datetime`, `firstName`, `middleName`, `lastName`, `gender`, `dateOfBirth`, `mobileNo`, `emailID`, `designation`,\
            `pinCode`, `houseNo`, `address`, `city`, `state`, `ifscCode`, `accountNo`, `bankName`, `branchName`, `panNo`, `qualificaton`, `dateOfJoin`, `contractType`, `salary`, `workShift`, `permission`)\
            VALUES (%s, '111111', current_timestamp(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'user')"
            result = cur.execute(sql,(username,first,middle,last,gender,dob,mobile,email,desig,pincode,house,address,city,state,ifsc,actNo,bank,branch,pan,quali,join,contract,salary,work,))
            if result:
                mysql.connection.commit()
                cur.close()
                return 'success'
        return render_template('add-staff.html')
    return redirect('/')

@app.route('/add-student', methods=['GET','POST'])
def add_student():
    if 'sno' in session:
        if request.method=='POST':
            first=request.form['firstName']
            middle=request.form['middleName']
            last= request.form['lastName']
            fname=request.form['fatherName']
            gender=request.form['gender']
            dob=request.form['dateOfBirth']
            mobile=request.form['mobile']
            email=request.form['email']
            birthPlace=request.form['birthPlace']
            mother=request.form['motherName']
            admNo=request.form['admNo']
            pincode=request.form['pincode']
            house=request.form['houseNo']
            address=request.form['address']
            city=request.form['city']
            state=request.form['state']
            category=request.form['category']
            admDate=request.form['admDate'];
            blood=request.form['bloodGroup']
            religion=request.form['religion']
            nationality=request.form['nationality']
            fatheroccu=request.form['fatherOccupation']
            height=request.form['height']
            weight=request.form['weight']
            nationalid=request.form['nationalId']
            txt=dob.split('-')
            username=first+txt[0]
            cur = mysql.connection.cursor()
            sql="INSERT INTO `userstudent` (`username`, `password`, `firstName`, `middleName`, `lastName`, `fatherName`, `gender`, `dateOfBirth`, `birthPlace`, `mobileNo`, `email`, `motherName`, `admNo`, `pinCode`, `houseNo`, `address`, `city`, `state`, `category`, `admDate`, `bloodGroup`, `religion`, `nationality`, `fatherOccupation`, `height`, `weight`, `nationalIDno`, `dateTime`, `teacherId`, `photo`)\
            VALUES (%s, '111111', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp(), '23', 'satvik.jpg');"
            result=cur.execute(sql, (username,first,middle,last,fname,gender,dob,birthPlace,mobile,email,mother,admNo,pincode,house,address,city,state,category,admDate,blood,religion,nationality,fatheroccu,height,weight,nationalid,))
            if result:
                mysql.connection.commit()
                cur.close()
                return 'success'
            else: 
                return 'error'
        return render_template('add-student.html')
    return redirect('/')

@app.route('/delete-staff', methods=['GET','POST'])
def del_staff():
    if 'sno' in session:
        cur=mysql.connection.cursor()
        result = cur.execute("DELETE FROM `useradmin` WHERE `useradmin`.`sno` = %s",(int(request.args.get("id")),))
        if result:
            mysql.connection.commit()
            cur.close()
            return redirect("/view-staff")
        else:
            return 'fail'
    return redirect("/")

@app.route('/delete-student', methods=['GET','POST'])
def del_student():
    if 'sno' in session:
        cur=mysql.connection.cursor()
        result = cur.execute("DELETE FROM `userstudent` WHERE `userstudent`.`sNo` = %s",(int(request.args.get("id")),))
        if result:
            mysql.connection.commit()
            cur.close()
            return redirect("/view-student")
        else:
            return redirect('/view-student')
    return redirect("/")

@app.route('/edit-staff', methods=['GET','POST'])
def edit_staff():
    if 'sno' in session:
        if request.args.get("id"):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM userAdmin where userAdmin.sno=%s",(request.args.get("id"),))
            if result > 0:
                user = cur.fetchone()
                return render_template("add-staff.html", dta=user, updt=True)
        else:
            if request.method=='POST':
                first=request.form['firstName']
                middle=request.form['middleName']
                last= request.form['lastName']
                gender=request.form['gender']
                dob=request.form['dateOfBirth']
                mobile=request.form['mobileNo']
                email=request.form['email']
                desig=request.form['designation']
                pincode=request.form['pincode']
                house=request.form['houseNo']
                address=request.form['address']
                city=request.form['city']
                state=request.form['state']
                ifsc=request.form['ifscode']
                actNo=request.form['acntNo']
                bank=request.form['bankName']
                branch=request.form['branch']
                pan=request.form['panNo']
                quali=request.form['qualification']
                join=request.form['joinDate']
                salary=request.form['salary']
                contract=request.form['contactType']
                work=request.form['workSft']
                sno= request.form['sNo']
                txt=dob.split('-')
                username=first+txt[0]
                cur = mysql.connection.cursor()
                result = cur.execute("UPDATE `useradmin` SET `username`=%s, `firstName`=%s, `middleName`=%s, `lastName`=%s, `gender`=%s, `dateOfBirth`=%s, `mobileNo`=%s, `emailID`=%s, `designation`=%s,\
                `pinCode`=%s, `houseNo`=%s, `address`=%s, `city`=%s, `state`=%s, `ifscCode`=%s, `accountNo`=%s, `bankName`=%s, `branchName`=%s, `panNo`=%s, `qualificaton`=%s, `dateOfJoin`=%s, `contractType`=%s, `salary`=%s, `workShift`=%s WHERE `useradmin`.`sno` = %s; ",(username,first,middle,last,gender,dob,mobile,email,desig,pincode,house,address,city,state,ifsc,actNo,bank,branch,pan,quali,join,contract,salary,work,sno,))
                if result:
                    mysql.connection.commit()
                    cur.close()
                    msg="success"
                    return redirect(url_for("view_staff", msg=msg))
                else:
                    msg="fail"
                    return redirect(url_for("view_staff", msg=msg))
    return redirect("/")

@app.route('/edit-student', methods=['GET','POST'])
def edit_student():
    if 'sno' in session:
        if request.args.get("id"):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM userstudent where userstudent.sno=%s",(request.args.get("id"),))
            if result > 0:
                user = cur.fetchone()
                return render_template("add-student.html", dta=user, updt=True)
        else:
            if request.method=='POST':
                first=request.form['firstName']
                middle=request.form['middleName']
                last= request.form['lastName']
                fname=request.form['fatherName']
                gender=request.form['gender']
                dob=request.form['dateOfBirth']
                mobile=request.form['mobile']
                email=request.form['email']
                birthPlace=request.form['birthPlace']
                mother=request.form['motherName']
                admNo=request.form['admNo']
                pincode=request.form['pincode']
                house=request.form['houseNo']
                address=request.form['address']
                city=request.form['city']
                state=request.form['state']
                category=request.form['category']
                admDate=request.form['admDate'];
                blood=request.form['bloodGroup']
                religion=request.form['religion']
                nationality=request.form['nationality']
                fatheroccu=request.form['fatherOccupation']
                height=request.form['height']
                weight=request.form['weight']
                nationalid=request.form['nationalId']
                sno= request.form['sNo']
                txt=dob.split('-')
                username=first+txt[0]
                cur = mysql.connection.cursor()
                result = cur.execute("UPDATE `userstudent` SET `username`=%s, `firstName` = %s, `middleName` = %s, `lastName` = %s, `fatherName` = %s, `gender` = %s, `dateOfBirth` = %s,\
                 `birthPlace` = %s, `mobileNo` = %s, `email` = %s, `motherName` = %s, `admNo` = %s, `pinCode` = %s, `houseNo` = %s, `address` = %s, `city` = %s, `state` = %s,\
                  `category` = %s, `admDate` = %s, `bloodGroup` = %s, `religion` = %s, `nationality` = %s, `fatherOccupation` = %s, `height` = %s, `weight` = %s, `nationalIDno` = %s WHERE `userstudent`.`sNo` = %s;\
                   ",(username,first,middle,last,fname,gender,dob,birthPlace,mobile,email,mother,admNo,pincode,house,address,city,state,category,admDate,blood,religion,nationality,fatheroccu,height,weight,nationalid,sno,))
                if result:
                    mysql.connection.commit()
                    cur.close()
                    msg="success"
                    return redirect(url_for("view_student", msg=msg))
                else:
                    msg="fail"
                    return redirect(url_for("view_student", msg=msg))
    return redirect("/")

@app.route('/bulk-data', methods=['GET','POST'])
def bulk_data():
    if 'sno' in session:
        if request.method == 'POST':
            file = request.form['upload-file']
            data = pd.read_excel(file)
            dic = []
            result=data.to_dict()
            for i in range(0,2):
                d = []
                for key,value in result.items():
                    d.append(value[i])
                dic.append(d)
            cur = mysql.connection.cursor()
            for i in dic:
                txt=i[4].strftime('%d-%m-%y')
                txt=txt.split('-')
                username = i[0]+"20"+txt[2]
                sql= "INSERT INTO `useradmin` (`username`, `password`, `datetime`, `firstName`, `middleName`, `lastName`, `gender`, `dateOfBirth`, `mobileNo`, `emailID`, `designation`,\
                `pinCode`, `houseNo`, `address`, `city`, `state`, `ifscCode`, `accountNo`, `bankName`, `branchName`, `panNo`, `qualificaton`, `dateOfJoin`, `contractType`, `salary`, `workShift`, `permission`)\
                VALUES (%s, '111111', current_timestamp(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'user')"
                result = cur.execute(sql,(username,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],))
            mysql.connection.commit()
            cur.close()
        return render_template('bulk-data.html')

@app.route('/bulk-data-student', methods=['GET','POST'])
def bulk_data_student():
    if 'sno' in session:
        if request.method == 'POST':
            file = request.form['upload-file']
            data = pd.read_excel(file)
            dic = []
            result=data.to_dict()
            for i in range(0,2):
                d = []
                for key,value in result.items():
                    d.append(value[i])
                dic.append(d)
            cur = mysql.connection.cursor()
            for i in dic:
                txt=i[5].strftime('%d-%m-%y')
                txt=txt.split('-')
                username = i[0]+"20"+txt[2]
                sql="INSERT INTO `userstudent` (`username`, `password`, `firstName`, `middleName`, `lastName`, `fatherName`, `gender`, `dateOfBirth`, `birthPlace`, `mobileNo`, `email`, `motherName`, `admNo`, `pinCode`, `houseNo`, `address`, `city`, `state`, `category`, `admDate`, `bloodGroup`, `religion`, `nationality`, `fatherOccupation`, `height`, `weight`, `nationalIDno`, `dateTime`, `teacherId`, `photo`)\
                VALUES (%s, '111111', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, current_timestamp(), %s, 'satvik.jpg');"
                result=cur.execute(sql, (username,i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19],i[20],i[21],i[22],i[23],i[24],session['sno'],))
            mysql.connection.commit()
            cur.close()
        return render_template('bulk-data-student.html')


@app.route("/one-view", methods=['GET','POST'])
def view():
    if 'sno' in session:
        if request.args.get("id"):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM userAdmin where userAdmin.sno=%s",(request.args.get("id"),))
            if result > 0:
                user = cur.fetchone()
                return render_template("view.html", dta=user, view=True)
    return redirect("/")

@app.route("/view", methods=['GET','POST'])
def view_one():
    if 'sno' in session:
        if request.args.get("id"):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM userstudent where userstudent.sno=%s",(request.args.get("id"),))
            if result > 0:
                user = cur.fetchone()
                return render_template("view.html", dta=user, view=False)
        else:
            return "can not view this page";
    return redirect("/")

@app.route('/profile', methods=['GET','POST'])
def profile():
    return render_template("profile.html")

@app.route('/show')
def show():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM userAdmin")
    if result > 0:
        user = cur.fetchall()
        print(user)
    return "no entry in db"

@app.route('/logout')
def logout():
    session.pop('sno',None)
    session.clear()
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True, port=8000)