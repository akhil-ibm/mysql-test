import mysql.connector
from flask import Flask, json, jsonify



app = Flask(__name__)

@app.route('/mysqlTest')
def sample():

    # Replace these values with your actual database information
    host = "mysql-openshift-mysql-test.itzroks-6670006ggk-j21buf-6ccd7f378ae819553d37d5f2ee142bd6-0000.us-south.containers.appdomain.cloud:80"
    user = "user1"
    password = "mypa55"
    database = "testdb"

    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Get data from a table
    cursor.execute("select * from sample001")
    data = cursor.fetchall()
    print(data)

        
    # Close the cursor and connection
    cursor.close()
    connection.close()


    return data

if __name__ == '__main__':
    app.run(debug=True)




