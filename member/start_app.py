from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/memberlist')
def memberlist():
    # DB 연동
    conn = sqlite3.connect("c:/webdb/webdb.db")
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute((sql))
    rs = cur.fetchall()
    conn.close()
    return render_template('memberlist.html', rs=rs)

@app.route('/register', methods = ['GET', 'POST'])
def register():

    if request.method == 'POST':
        # 데이터 가져오기(웹페이지)
        id = request.form['memberid']
        pwd = request.form['passwd']
        name = request.form['name']
        age = request.form['age']
        date = request.form['reg_date']

        # DB 연동
        conn = sqlite3.connect("c:/webdb/webdb.db")
        cur = conn.cursor()
        sql = "INSERT INTO member VALUES('%s', '%s', '%s', '%s', '%s')" % (id, pwd, name, age, date)
        cur.execute(sql)
        conn.commit()
        conn.close()

        return redirect(url_for('memberlist'))  # 강제로 주소(페이지)이동

    else:
        return render_template('register.html')

app.run()
