from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/add/user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template('add_user.html')

    print(request.form)
    username = request.form.get("user")
    userpassword = request.form.get("pwd")
    mobile = request.form.get("mobile")

    # 1、连接mysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset='utf8', db='ermdb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2、执行sql语句
    sql = "insert into tb1(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, [username, userpassword, mobile])
    conn.commit()

    # 3、关闭连接
    cursor.close()
    conn.close()

    return "提交完成"


@app.route("/show/user")
def show_user():
    # 从数据库获得所有信息
    # 1、连接mysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", charset='utf8', db='ermdb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 2、执行sql语句
    sql = "select * from tb1"
    cursor.execute(sql)
    dataList = cursor.fetchall()

    # 3、关闭连接
    cursor.close()
    conn.close()

    print(dataList)

    return render_template('show_user.html', data_List = dataList)

if __name__ == '__main__':
    app.run()
