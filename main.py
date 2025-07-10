from fastapi import FastAPI
from datetime import date
import mysql.connector
mydb=mysql.connector.connect(
    host ="localhost",
    user ="root",
    password ="admin",
    database = "fee_management",
    port =3308
)
mycursor = mydb.cursor()
app=FastAPI()
@app.get("/insert/")
def insert(spr:int,name:str,dept:str,year:int,phn:int,t_f:int,b_f:int,h_f:int,me_f:int,m_f:int):
    x = "insert into sd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    y = (spr,name,dept,year,phn,t_f,b_f,h_f,me_f,m_f)
    mycursor.execute(x, y)
    mydb.commit()
    return{"Message":"INSERTED SUCCESSFULLY"}
@app.patch("/update1/")
def update1(spr:int,dept:str):
    x = "update sd set dept = %s where spr = %s"
    y = (dept, spr)
    mycursor.execute(x, y)
    mydb.commit()
    return {"Message": " Department Updated SUCCESSFULLY"}
@app.patch("/update2/")
def update2(spr:int,year:int):
    x = "update sd set year = %s where spr = %s"
    y = (year,spr)
    mycursor.execute(x, y)
    mydb.commit()
    return {"Message": "Year Updated SUCCESSFULLY"}
@app.patch("/update3/")
def update3(spr: int, phn: int):
    x = "update sd set phn = %s where spr = %s"
    y = (phn, spr)
    mycursor.execute(x, y)
    mydb.commit()
    return {"Message": " Phn num Updated SUCCESSFULLY"}
@app.patch("/update4/")
def update4(spr:int,t_f:int):
    x="update sd set t_f = %s where spr = %s"
    y=(t_f, spr)
    mycursor.execute(x,y)
    mydb.commit()
    return {"Message": " Tuition fees Updated SUCCESSFULLY"}
@app.patch("/update5/")
def update5(spr:int,b_f:int):
    x="update sd set b_f = %s where spr = %s"
    y=(b_f,spr)
    mycursor.execute(x,y)
    mydb.commit()
    return {"Message": "Bus fees Updated SUCCESSFULLY"}
@app.patch("/update6/")
def update6(spr:int,h_f:int):
    x="update sd set h_f = %s where spr = %s"
    y=(h_f,spr)
    mycursor.execute(x,y)
    mydb.commit()
    return {"Message": "hostel fees Updated SUCCESSFULLY"}
@app.patch("/update7/")
def update7(spr:int,me_f:int):
    x="update sd set me_f = %s where spr = %s"
    y=(me_f, spr)
    mycursor.execute(x,y)
    mydb.commit()
    return {"Message": "Mess fees Updated SUCCESSFULLY"}
@app.patch("/update8/")
def update7(spr:int,m_f:int):
    x="update sd set m_f = %s where spr = %s"
    y=(m_f, spr)
    mycursor.execute(x,y)
    mydb.commit()
    return {"Message": "Mess fees Updated SUCCESSFULLY"}
@app.delete("/delete/")
def delete(a:int):
    b = input("Do you want to delete the record?:")
    if b == "yes":
        # a = int(input("Enter the stu_id:"))
        y = (a,)
        x = "delete from sd where id=%s"
        mycursor.execute(x, y)
        mydb.commit()
        return {"Message": "DATA is delected SUCCESSFULLY"}
    else:
        print("Thanks")
        return {"Message": "thanks"}
@app.get("/fees/")
def fees(spr:int,bill_date:date,details:str,amount:int):
    x = "insert into fd (spr,bill_date,details,amount) values(%s,%s,%s,%s)"
    y = (spr,bill_date,details,amount)
    mycursor.execute(x, y)
    mydb.commit()
    return{"message":"fees details is inserted"}
@app.get("/show/")
def fun(sd_or_fd:str):
    if sd_or_fd =="sd":
        y="select* from sd"
        mycursor.execute(y)
        b=mycursor.fetchall()
        return{"details":b}
    elif sd_or_fd =="fd":
        y="select* from fd"
        mycursor.execute(y)
        b = mycursor.fetchall()
        return {"details": b}
@app.get("/report/")
def report(spr:int ):
    x = "select sd.spr,sd.name,sd.dept,sd.year,sd.phn,sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f,sum(sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f)as total ,fd.bill_no,fd.bill_date,fd.details,fd.amount as paid,sum(fd.amount) as amt_pay ,(total-amt_pay) as bal from sd inner join fd on sd.spr=fd.spr where sd.spr=%s group by sd.spr,sd.name,sd.dept,sd.year,sd.phn,sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f,fd.bill_no,fd.bill_date,fd.details,fd.amount"
    y = (spr,)
    mycursor.execute(x, y)
    b = mycursor.fetchall()
    return{"Report":b}
@app.get("/report1/")
def report(bdate :date,edate:date):
    x = "select sd.spr,sd.name,sd.dept,sd.year,sd.phn,sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f,fd.bill_no,fd.bill_date,fd.details,fd.amount as paid from sd inner join fd on sd.spr=fd.spr where fd.bill_date between %s and %s group by sd.spr,sd.name,sd.dept,sd.year,sd.phn,sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f,fd.bill_no,fd.bill_date,fd.details,fd.amount"
    y = (bdate,edate)
    mycursor.execute(x, y)
    b = mycursor.fetchall()
    return {"Report": b}
@app.get("/bal/")
def bal(spr:int):
    x="select sd.spr,sd.name,sd.dept,sd.year,sd.phn,sd.t_f,sd.b_f,sd.h_f,sd.me_f,sd.m_f,(sd.t_f+sd.b_f+sd.h_f+sd.me_f+sd.m_f) as fullamt ,sum(fd.amount)as total,((sd.t_f+sd.b_f+sd.h_f+sd.me_f+sd.m_f)-sum(fd.amount)) as balance from sd inner join fd on sd.spr=fd.spr where sd.spr=%s group by sd.spr,sd.name,sd.dept,sd.year,sd.phn"
    y = (spr,)
    mycursor.execute(x, y)
    b = mycursor.fetchall()
    return {"Report": b}

   
