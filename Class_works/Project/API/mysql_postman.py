# task1
# write a function to fetch data from sql table via api(postman)

from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'testineuron'

mysql = MySQL(app)


@app.route("/conn_mysql", methods=["GET", "POST"])
def handle_s_data():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM ineuron")
        user = cur.fetchall()
        return str(user)


if __name__ == '__main__':
    app.run()
