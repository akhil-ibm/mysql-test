import mysql.connector
from flask import Flask, json, jsonify



app = Flask(__name__)

@app.route('/mysqlTest')
def sample():

    # Replace these values with your actual database information
    host = "localhost"
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

    return data

if __name__ == '__main__':
    app.run(debug=True)



# # Get the list of tables in the database
# cursor.execute("SHOW TABLES")

# tables = cursor.fetchall()
# # 
# # Iterate through the tables and get details for each
# for table in tables:
#     table_name = table[0]

#     # Get the column names and data types for each table
#     cursor.execute(f"DESCRIBE {table_name}")
#     columns = cursor.fetchall()

#     print(f"Table: {table_name}")
#     print("Column Details:")
#     for column in columns:
#         print(f"  {column[0]} - {column[1]}")

#     print("\n")



# Close the cursor and connection
cursor.close()
connection.close()
