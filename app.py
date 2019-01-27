from flaskext.mysql import MySQL
from flask import Flask,render_template,json
app = Flask(__name__)

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
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
