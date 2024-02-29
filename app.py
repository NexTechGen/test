import sqlite3
from flask import *

app = Flask(__name__) 
# creat DB
'''conn = sqlite3.connect('Divisions.db')

c = conn.cursor()

c.execute("""CREATE TABLE customers(
            first_name text,
            last_name text,
            house_num text
            )""")


conn.commit()

conn.close()'''

@app.route('/')   
def main():   
    return render_template("index.html")

@app.route('/data', methods=["POST", "GET"])   
def data():   
    fname = request.form['fname']
    lname = request.form['lname']
    hnum = request.form['hnum']

    conn = sqlite3.connect('Divisions.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (fname, lname, hnum))

    print("Command executed succesfully...")
    conn.commit()
    conn.close()

    return redirect(url_for("sub"))

@app.route('/submit')   
def sub(): 
    conn = sqlite3.connect('Divisions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")   
    data = c.fetchall() 
    print(c.fetchall())

    return render_template("dat.html", data = data)

@app.route("/download")
def Download_File():
    PATH = "Divisions.db"
    return send_file(PATH, as_attachment=True)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)