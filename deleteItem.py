#!C:/Users/vargh/AppData/Local/Programs/Python/Python312/python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback
cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
item_id = form.getvalue('id')

if item_id:
    try:
        myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"  # Your database name
        )
        myCursor = myDb.cursor()

        # Delete item from the database
        sql = "DELETE FROM item WHERE id = %s"
        myCursor.execute(sql, (item_id,))
        myDb.commit()

        print("<h2>Item deleted successfully!</h2><a href='readItems.py'>View Items</a>")

    except Exception as e:
        print(e)
    finally:
        myDb.close()
else:
    print("<h2>Item ID not provided!</h2><a href='readItems.py'>Back</a>")
