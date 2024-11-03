#!C:/Users/vargh/AppData/Local/Programs/Python/Python312/python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback
cgitb.enable()

print("Content-type: text/html\n")

form = cgi.FieldStorage()
item_id = form.getvalue('id')
item_name = form.getvalue('item_name')
item_description = form.getvalue('item_description')

try:
    myDb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"  # Your database name
    )
    myCursor = myDb.cursor()

    if item_id and item_name and item_description:
        # Update item in the database
        sql = "UPDATE item SET name = %s, description = %s WHERE id = %s"
        myCursor.execute(sql, (item_name, item_description, item_id))
        myDb.commit()
        
        print(f"<h2>Item updated successfully!</h2><a href='readItems.py'>View Items</a>")
    else:
        # Display the update form
        myCursor.execute("SELECT * FROM item WHERE id = %s", (item_id,))
        item = myCursor.fetchone()
        if item:
            print(f"""
            <form action="updateItem.py?id={item_id}" method="post">
                <input type="text" name="item_name" value="{item[1]}" required>
                <input type="text" name="item_description" value="{item[2]}" required>
                <input type="submit" value="Update">
            </form>
            """)
        else:
            print("<h2>Item not found!</h2>")
            
except Exception as e:
    print(e)
finally:
    myDb.close()
