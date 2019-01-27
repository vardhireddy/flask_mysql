# flask_mysql
Step1: docker pull mysql
Step2: docker run --name mysql -d -p 3306:3306 -p 33060:33060 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=test mysql
Step3: Install the mysql shell for windows
Step4: Run the mysql shell client
Step5: Establish the connection - 
\connect root@192.168.33.10 or \connect mysqlx://root@192.168.33.10

Step6: Install and create a flask app to display the databases
pip install flask
pip install flask_mysql
app.py

from flaskext.mysql import MySQL
from flask import Flask,json
app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = '192.168.33.10'
app.config['auth_plugin']='mysql_native_password'
mysql.init_app(app)

conn = mysql.connect()
@app.route("/")
def main():
    query = "show databases"
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    conn.close()
    return json.dumps(data)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)

step7: Run the flask app - flask app.py

Troublishooting:
     Problem1:  RuntimeError: cryptography is required for sha256_password or caching_sha2_password
	 Solution:   ALTER USER 'username' IDENTIFIED WITH mysql_native_password BY 'password';

