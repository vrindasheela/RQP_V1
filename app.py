from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/qgen', methods = ['POST', 'GET'])
def qgen():
       code = request.form['code']
       print(code)
       con = sql.connect('rqpmain.db')
       con.row_factory = sql.Row
       cur = con.cursor()
       if(code == '1'):
             cur.execute("SELECT * FROM questions WHERE unum = '1'")
             rows = cur.fetchall() 
       else:
             cur.execute("SELECT * FROM questions WHERE unum = '2'")
             rows = cur.fetchall() 

       
       return render_template("qgen.html", rows = rows)


'''@app.route('/enternew')
def new_student():
   return render_template('student1.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result1.html",msg = msg)
         con.close()'''

if __name__ == '__main__':
   app.run(debug = True)