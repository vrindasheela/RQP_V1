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
       else:
             cur.execute("SELECT * FROM questions WHERE unum IN ('2', '4')")
             rows = cur.fetchall() 

       
       return render_template("qgen.html", rows = rows)


if __name__ == '__main__':
   app.run(debug = True)