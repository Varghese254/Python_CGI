#!C:/Users/vargh/AppData/Local/Programs/Python/Python312/python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback
cgitb.enable()

# Print the necessary headers
print("Content-type: text/html\n")

# Fetch form data
form = cgi.FieldStorage()
item_name = form.getvalue('item_name')
item_description = form.getvalue('item_description')

if item_name and item_description:
    try:
        myDb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"  # Your database name
        )
        myCursor = myDb.cursor()
        
        # Insert new item into MySQL table
        sql = "INSERT INTO item (name, description) VALUES (%s, %s)"
        myCursor.execute(sql, (item_name, item_description))
        myDb.commit()

        print(f"""
        <html>
        <body>
            <h2>Item added successfully!</h2>
            <p>Item Name: {item_name}</p>
            <p>Description: {item_description}</p>
            <a href="index.html">Back</a>
        </body>
        </html>
        """)

    except Exception as e:
        print(e)
    finally:
        myDb.close()
