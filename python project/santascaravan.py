''' This is a simple vaccine management system using SQLite. 
    It demonstrates the capabilities of SQLite. It is not intended for production environments.
    For example, the changemade variable does not update once the program is started.
    So, if someone left the application open for a long time and made changes later, the data would not be accurate.
    '''
import sqlite3
#importing Error this way let's us refer to it by this name instead of sqlite3.Error
from sqlite3 import Error 
import datetime
#if you code is not connecting to the DB, uncomment the next three lines and read the comments. Also, you may need \ instead of / before the DB file name in windows
#import os
#path_root = os.path.dirname(os.path.abspath(__file__)) #grab the file system path to the current script file
#database_file_path = str(path_root)+"/myinventory.db" #construct the path to the database file (only necessary if the current working directory is not the same as the folder where this Python file is located.)
#if you uncomment the three lines above, be sure to comment out this next line
database_file_path = "scaravan.db"
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

def insert_data():
    pname = input("Enter Parents' Name: ")
    address = input("Enter Address: ")
    sub = input ("Enter Subdivision/Apt Name/Trailer Park: ")
    lot = input("Enter Lot/Apt #: ")
    gatecode = input("Gate Code y/n: ")
    gatecode1 = input("Enter Gate Code: ")
    phone = input("Enter Phone #: ")
    additcon = input("Enter Additional Contact Name: ")
    additconnum = input("Enter Additional Contact Phone #: ")
    work = input("What adults in this home are working full-time? ")
    otherfam = input("Are there other Camilies living with children in this home full-time? ")
    childnum = input("Enter Amount of children: ")
    child1name = input("Enter First Child's Name: ")
    child1age = input("Enter First Child's Age: ")
    child1gend = input("Enter First Child's Gender M/F: ")
    child1sch = input("Enter First Child's School: ")
    child1shirt = input("Enter First Child's Shirt Size: ")
    child1pant = input("Enter First Child's Pant Size: ")
    child1spec = input("Enter First Child's Specific Clothing Needs: ")
    child1not = input("Enter Any Additional Notes on First Child: ")
    child1non1 = input("Enter First Child Non-Clothing Request 1: ")
    child1non2 = input("Enter First Child Non-Clothing Request 2: ")
    child1non3 = input("Enter First Child Non-Clothing Request 3: ")
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO vaccines (name,ndc,location,availability,arrivaldate,expirationdate,changemade)\
            values("+"'"+ str(name) +"'" + ",'"+ str(ndc) +"', '"+ str(location) +"','"+ str (availability)+"','"+str(arrivaldate)+"','"+ str (expirationdate)+"','"+str(changemade)+"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass
                                 
def view_data():
    try:
        cursor = conn.execute ("SELECT id,name, ndc,location,availability,arrivaldate, expirationdate,changemade FROM vaccines" )
        alldata = []
        alldata.append(["ID","Name","NDC","Location","Availability","Arrival Date","Expiration Date","Last Update"])
        for row in cursor:
            thisrow=[]
            for x in range(8):
                thisrow.append(row[x])
            alldata.append(thisrow)
        return alldata
    except Error as e:
        print (e)
        pass

def update_data():
    for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    update_ID = input("Enter the ID of the data record to edit: ")
    print('''
        1 = edit name
        2 = edit ndc
        3 = edit location
        4 = edit availability
        5 = edit arrivaldate
        6 = edit expirationdate''')

    feature = input("Enter which feature of the data do you want to edit: ")
    update_value = input ("Editing "+feature+ ": enter the new value: ")

    if(feature == "1"):
        sql = "UPDATE vaccines set name = ? where id =  ?"
    elif (feature == "2"):
       sql = "UPDATE vaccines set ndc = ? where id =  ?" 
    elif (feature == "3"):
       sql = "UPDATE vaccines set location  = ? where id =  ?"
    elif (feature == "4"):
       sql = "UPDATE vaccines set availability  = ? where id =  ?"
    elif (feature == "5"):
       sql = "UPDATE vaccines set arrivaldate  = ? where id =  ?"
    elif (feature == "6"):
       sql = "UPDATE vaccines set expirationdate = ? where id =  ?"  
        
    try:
        #if we call the connection execute method it invisibly creates a cursor for us
        conn.execute(sql, (update_value,update_ID))
        #update the change made date log
        sql = "UPDATE vaccines set changemade = ? where id =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_ID)) 
        
    except Error as e:
        print(e)
        pass

def delete_data():
    id_  =  input("Enter the ID for the data record to delete:")
    cursor = conn.cursor() #This sets a spot in the database connection (cursor) for targeted retrieval
    cursor.execute("select name from vaccines where ID = "+id_) #create an object referencing the data
    delete_item = cursor.fetchall() # get the data
    confirm = input("Are you sure you want to delete " + id_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM vaccines WHERE id = ?"
            conn.execute(delete_sql,id_)
            result = conn.commit() #capture the result of the commit and use it to check the result
            if result == None:
                print (id_ + " " + str(delete_item[0]) + " deleted.")
            else:
                print ("Deletion failed during SQL execution.")
        except Error as e:
            print (e)
            pass
    else:
        print("Deletion aborted.")

conn = create_connection(database_file_path)
now = datetime.datetime.now()

if conn:
    print ("Connected to database: ",conn)  
else:
    print("Error connecting to database.")

while True:
    print("Welcome to the Vaccine Management System!")
    print("1 to view the data")
    print("2 to insert a new data record")
    print("3 to update a data record")
    print("4 to delete a data record")
    print("X to exit")
    name = input ("Choose an operation to perform: ")
    if (name =="1"):
        for row in view_data():
            thisrow = "  --> "
            for item in row:
                thisrow += str(item) + "  "
            print (thisrow)
    elif(name == "2"):
        insert_data()
    elif(name == "3"):
        update_data()
    elif(name == "4"):
        delete_data()
    elif(name == "X"):
        conn.close()
        break
