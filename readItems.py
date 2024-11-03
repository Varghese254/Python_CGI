#!C:/Users/vargh/AppData/Local/Programs/Python/Python312/python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback
cgitb.enable()

# Print the necessary headers
print("Content-type: text/html\n")

try:
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"  # Your database name
    )
    myCursor = myDb.cursor()

    # Fetch all items from the database
    myCursor.execute("SELECT * FROM item")
    items = myCursor.fetchall()

    print("<html><body><h2>Items List</h2><ul>")
    for item in items:
        print(f"<li>{item[1]}: {item[2]} <a href='updateItem.py?id={item[0]}'>Update</a> <a href='deleteItem.py?id={item[0]}'>Delete</a></li>")
    print("</ul><a href='index.html'>Back</a></body></html>")

except Exception as e:
    print(e)
finally:
    myDb.close()
