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
             cur.execute("SELECT * FROM questions WHERE unum IN ('1', '3')")
             rows = cur.fetchall()
             list_qn = []
             list_qno = []
             list_ans = []
             for row in rows:
                   list_qno.append(row["unum"])
                   list_qn.append(row["ques"])
                   list_ans.append(row["ans"])
             print(list_qno)
             print(list_qn)
             print(list_ans)
             return render_template("qgen.html", rows = rows) 
       else:
             cur.execute("SELECT * FROM questions WHERE unum IN ('2', '4')")
             rows = cur.fetchall()
             return render_template("qgen1.html", rows = rows) 

       
       '''return render_template("qgen.html", rows = rows)'''


if __name__ == '__main__':
   app.run(debug = True)