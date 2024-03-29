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
    famnumb = input("Enter Assign Family a Number: ")
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
    otherfam = input("Are there other Families living with children in this home full-time? ")
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
    child2name = input("Enter Second Child's Name: ")
    child2age = input("Enter Second Child's Age: ")
    child2gend = input("Enter Second Child's Gender M/F: ")
    child2sch = input("Enter Second Child's School: ")
    child2shirt = input("Enter Second Child's Shirt Size: ")
    child2pant = input("Enter Second Child's Pant Size: ")
    child2spec = input("Enter Second Child's Specific Clothing Needs: ")
    child2not = input("Enter Any Additional Notes on Second Child: ")
    child2non1 = input("Enter Second Child Non-Clothing Request 1: ")
    child2non2 = input("Enter Second Child Non-Clothing Request 2: ")
    child2non3 = input("Enter Second Child Non-Clothing Request 3: ")
    child3name = input("Enter Third Child's Name: ")
    child3age = input("Enter Third Child's Age: ")
    child3gend = input("Enter Third Child's Gender M/F: ")
    child3sch = input("Enter Third Child's School: ")
    child3shirt = input("Enter Third Child's Shirt Size: ")
    child3pant = input("Enter Third Child's Pant Size: ")
    child3spec = input("Enter Third Child's Specific Clothing Needs: ")
    child3not = input("Enter Any Additional Notes on Third Child: ")
    child3non1 = input("Enter Third Child Non-Clothing Request 1: ")
    child3non2 = input("Enter Third Child Non-Clothing Request 2: ")
    child3non3 = input("Enter Third Child Non-Clothing Request 3: ")
    child4name = input("Enter Fourth Child's Name: ")
    child4age = input("Enter Fourth Child's Age: ")
    child4gend = input("Enter Fourth Child's Gender M/F: ")
    child4sch = input("Enter Fourth Child's School: ")
    child4shirt = input("Enter Fourth Child's Shirt Size: ")
    child4pant = input("Enter Fourth Child's Pant Size: ")
    child4spec = input("Enter Fourth Child's Specific Clothing Needs: ")
    child4not = input("Enter Any Additional Notes on Fourth Child: ")
    child4non1 = input("Enter Fourth Child Non-Clothing Request 1: ")
    child4non2 = input("Enter Fourth Child Non-Clothing Request 2: ")
    child4non3 = input("Enter Fourth Child Non-Clothing Request 3: ")
    changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
    try:      
        sqlresult = conn.execute("INSERT INTO santascaravan (famnumb,pname,address,sub,lot,gatecode,gatecode1,phone,additcon,additconnum,work,otherfam,childnum,child1name,child1age,child1gend,child1sch,child1shirt,child1pant,child1spec,child1not,child1non1,child1non2,child1non3,child2name,child2age,child2gend,child2sch,child2shirt,child2pant,child2spec,child2not,child2non1,child2non2,child2non3,child3name,child3age,child3gend,child3sch,child3shirt,child3pant,child3spec,child3not,child3non1,child3non2,child3non3,child4name,child4age,child4gend,child4sch,child4shirt,child4pant,child4spec,child4not,child4non1,child4non2,child4non3,changemade)\
            values("+"'"+ str(famnumb) +"'" + ",'"+ str(pname) +"','"+ str(address) +"', '"+ str(sub) +"','"+ str (lot)+"','"+str(gatecode)+"','"+ str (gatecode1)+"','"+str(phone)+"','"+ str(additcon) +"','"+ str(additconnum) +"','"+ str(work) +"','"+ str(otherfam) +"','"+ str(childnum) +"','"+ str(child1name) +"','"+ str(child1age) +"','"+ str(child1gend) +"','"+ str(child1sch) +"','"+ str(child1shirt) +"','"+ str(child1pant) +"','"+ str(child1spec) +"','"+ str(child1not) +"','"+ str(child1non1) +"','"+ str(child1non2) +"','"+ str(child1non3) +"','"+ str(child2name) +"','"+ str(child2age) +"','"+ str(child2gend) +"','"+ str(child2sch) +"','"+ str(child2shirt) +"','"+ str(child2pant) +"','"+ str(child2spec) +"','"+ str(child2not) +"','"+ str(child2non1) +"','"+ str(child2non2) +"','"+ str(child2non3) +"','"+ str(child3name) +"','"+ str(child3age) +"','"+ str(child3gend) +"','"+ str(child3sch) +"','"+ str(child3shirt) +"','"+ str(child3pant) +"','"+ str(child3spec) +"','"+ str(child3not) +"','"+ str(child3non1) +"','"+ str(child3non2) +"','"+ str(child3non3) +"','"+ str(child4name) +"','"+ str(child4age) +"','"+ str(child4gend) +"','"+ str(child4sch) +"','"+ str(child4shirt) +"','"+ str(child4pant) +"','"+ str(child4spec) +"','"+ str(child4not) +"','"+ str(child4non1) +"','"+ str(child4non2) +"','"+ str(child4non3) +"','"+ str(changemade) +"')")
        result = conn.commit() #this actually runs the SQL and inserts the data into the database
        if result == None:
            print("*** Data saved to database. ***")
    except Error as e:
        print ("*** Insert error: ",e)
        pass
                                 
def view_data():
    try:
        cursor = conn.execute ("SELECT famnumb,pname,address,sub,lot,gatecode,gatecode1,phone,additcon,additconnum,work,otherfam,childnum,child1name,child1age,child1gend,child1sch,child1shirt,child1pant,child1spec,child1not,child1non1,child1non2,child1non3,child2name,child2age,child2gend,child2sch,child2shirt,child2pant,child2spec,child2not,child2non1,child2non2,child2non3,child3name,child3age,child3gend,child3sch,child3shirt,child3pant,child3spec,child3not,child3non1,child3non2,child3non3,child4name,child4age,child4gend,child4sch,child4shirt,child4pant,child4spec,child4not,child4non1,child4non2,child4non3,changemade FROM santascaravan" )
        alldata = []
        alldata.append(["Family Number","Parents' Name","Address","Subdivision/Apt Name/Trailer Park","Lot/Apt #","Gatecode y/n?","Gatecode #","Phone #","Additional Contact Name","Additional Contact #","What Adults in House Are Working","Other Families Living with Children y/n","Amount Of Children","First Child's Name","First Child's Age","First Child's Gender M/F","First Child's School","First Child's Shirt Size","First Child's Pant Size","First Child's Specific Clothing Needs","Additional Notes on First Child","First Child Non-Clothing Request 1","First Child Non-Clothing Request 2","First Child Non-Clothing Request 3","Second Child's Name","Second Child's Age","Second Child's Gender M/F","Second Child's School","Second Child's Shirt Size","Second Child's Pant Size","Second Child's Specific Clothing Needs","Additional Notes on Second Child","Second Child Non-Clothing Request 1","Second Child Non-Clothing Request 2","Second Child Non-Clothing Request 3","Third Child's Name","Third Child's Age","Third Child's Gender M/F","ThirdChild's School","Third Child's Shirt Size","Third Child's Pant Size","Third Child's Specific Clothing Needs","Additional Notes on Third Child","Third Child Non-Clothing Request 1","Third Child Non-Clothing Request 2","Third Child Non-Clothing Request 3","Fourth Child's Name","Fourth Child's Age","Fourth Child's Gender M/F","Fourth Child's School","Fourth Child's Shirt Size","Fourth Child's Pant Size","Fourth Child's Specific Clothing Needs","Additional Notes on Fourth Child","Fourth Child Non-Clothing Request 1","Fourth Child Non-Clothing Request 2","Fourth Child Non-Clothing Request 3","Last Update"])
        for row in cursor:
            thisrow=[]
            for x in range(58):
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
    update_famnumb = input("Enter the Family Number of the data record to edit: ")
    print('''
        1 = edit pname
        2 = edit address
        3 = edit sub
        4 = edit lot
        5 = edit gatecode
        6 = edit phone
        7 = edit additcon
        8 = edit additconnum
        9 = edit work
        10 = edit otherfam
        11 = edit childnum
        12 = edit child1name
        13 = edit child1age
        14 = edit child1gend
        15 = edit child1sch
        16 = edit child1shirt
        17 = edit child1pant
        18 = edit child1spec
        19 = edit child1not
        20 = edit child1non1
        21 = edit child1non2
        22 = edit child1non3
        23 = edit child2name
        24 = edit child2age
        25 = edit child2gend
        26 = edit child2sch
        27 = edit child2shirt
        28 = edit child2pant
        29 = edit child2spec
        30 = edit child2not
        31 = edit child2non1
        32 = edit child2non2
        33 = edit child2non3
        34 = edit child3name
        35 = edit child3age
        36 = edit child3gend
        37 = edit child3sch
        38 = edit child3shirt
        39 = edit child3pant
        40 = edit child3spec
        41 = edit child3not
        42 = edit child3non1
        43 = edit child3non2
        44 = edit child3non3
        45 = edit child4name
        46 = edit child4age
        47 = edit child4gend
        48 = edit child4sch
        49 = edit child4shirt
        50 = edit child4pant
        51 = edit child4spec
        52 = edit child4not
        53 = edit child4non1
        54 = edit child4non2
        55 = edit child4non3''')
        

    feature = input("Enter which feature of the data do you want to edit: ")
    update_value = input ("Editing "+feature+ ": enter the new value: ")

    if(feature == "1"):
        sql = "UPDATE santascaravan set pname = ? where famnumb =  ?"
    elif (feature == "2"):
       sql = "UPDATE santascaravan set address = ? where famnumb =  ?" 
    elif (feature == "3"):
       sql = "UPDATE santascaravan set sub  = ? where famnumb =  ?"
    elif (feature == "4"):
       sql = "UPDATE santascaravan set lot  = ? where famnumb =  ?"
    elif (feature == "5"):
       sql = "UPDATE santascaravan set gatecode  = ? where famnumb =  ?"
    elif (feature == "6"):
       sql = "UPDATE santascaravan set gatecode1 = ? where famnumb =  ?"
    elif (feature == "7"):
       sql = "UPDATE santascaravan set phone = ? where famnumb =  ?"
    elif (feature == "8"):
       sql = "UPDATE santascaravan set additcon = ? where famnumb =  ?"
    elif (feature == "9"):
       sql = "UPDATE santascaravan set additconnum = ? where famnumb =  ?"
    elif (feature == "10"):
       sql = "UPDATE santascaravan set work = ? where famnumb =  ?"  
    elif (feature == "11"):
       sql = "UPDATE santascaravan set otherfam = ? where famnumb =  ?"
    elif (feature == "12"):
       sql = "UPDATE santascaravan set childnum = ? where famnumb =  ?"
    elif (feature == "13"):
       sql = "UPDATE santascaravan set child1name = ? where famnumb =  ?"
    elif (feature == "14"):
       sql = "UPDATE santascaravan set child1age = ? where famnumb =  ?"
    elif (feature == "15"):
       sql = "UPDATE santascaravan set child1gend = ? where famnumb =  ?"
    elif (feature == "16"):
       sql = "UPDATE santascaravan set child1sch = ? where famnumb =  ?"
    elif (feature == "17"):
       sql = "UPDATE santascaravan set child1shirt = ? where famnumb =  ?"
    elif (feature == "18"):
       sql = "UPDATE santascaravan set child1pant = ? where famnumb =  ?"
    elif (feature == "19"):
       sql = "UPDATE santascaravan set child1spec = ? where famnumb =  ?"
    elif (feature == "20"):
       sql = "UPDATE santascaravan set child1not = ? where famnumb =  ?"
    elif (feature == "21"):
       sql = "UPDATE santascaravan set child1non1 = ? where famnumb =  ?"
    elif (feature == "22"):
       sql = "UPDATE santascaravan set child1non2 = ? where famnumb =  ?"
    elif (feature == "23"):
       sql = "UPDATE santascaravan set child1non3 = ? where famnumb =  ?"
    elif (feature == "24"):
       sql = "UPDATE santascaravan set child2name = ? where famnumb =  ?"
    elif (feature == "25"):
       sql = "UPDATE santascaravan set child2age = ? where famnumb =  ?"
    elif (feature == "26"):
       sql = "UPDATE santascaravan set child2gend = ? where famnumb =  ?"
    elif (feature == "27"):
       sql = "UPDATE santascaravan set child2sch = ? where famnumb =  ?"
    elif (feature == "28"):
       sql = "UPDATE santascaravan set child2shirt = ? where famnumb =  ?"
    elif (feature == "29"):
       sql = "UPDATE santascaravan set child2pant = ? where famnumb =  ?"
    elif (feature == "30"):
       sql = "UPDATE santascaravan set child2spec = ? where famnumb =  ?"
    elif (feature == "31"):
       sql = "UPDATE santascaravan set child2not = ? where famnumb =  ?"
    elif (feature == "32"):
       sql = "UPDATE santascaravan set child2non1 = ? where famnumb =  ?"
    elif (feature == "33"):
       sql = "UPDATE santascaravan set child2non2 = ? where famnumb =  ?"
    elif (feature == "34"):
       sql = "UPDATE santascaravan set child2non3 = ? where famnumb =  ?"
    elif (feature == "35"):
       sql = "UPDATE santascaravan set child3name = ? where famnumb =  ?"
    elif (feature == "36"):
       sql = "UPDATE santascaravan set child3age = ? where famnumb =  ?"
    elif (feature == "37"):
       sql = "UPDATE santascaravan set child3gend = ? where famnumb =  ?"
    elif (feature == "38"):
       sql = "UPDATE santascaravan set child3sch = ? where famnumb =  ?"
    elif (feature == "39"):
       sql = "UPDATE santascaravan set child3shirt = ? where famnumb =  ?"
    elif (feature == "40"):
       sql = "UPDATE santascaravan set child3pant = ? where famnumb =  ?"
    elif (feature == "41"):
       sql = "UPDATE santascaravan set child3spec = ? where famnumb =  ?"
    elif (feature == "42"):
       sql = "UPDATE santascaravan set child3not = ? where famnumb =  ?"
    elif (feature == "43"):
       sql = "UPDATE santascaravan set child3non1 = ? where famnumb =  ?"
    elif (feature == "44"):
       sql = "UPDATE santascaravan set child3non2 = ? where famnumb =  ?"
    elif (feature == "45"):
       sql = "UPDATE santascaravan set child3non3 = ? where famnumb =  ?"
    elif (feature == "46"):
       sql = "UPDATE santascaravan set child4name = ? where famnumb =  ?"
    elif (feature == "47"):
       sql = "UPDATE santascaravan set child4age = ? where famnumb =  ?"
    elif (feature == "48"):
       sql = "UPDATE santascaravan set child4gend = ? where famnumb =  ?"
    elif (feature == "49"):
       sql = "UPDATE santascaravan set child4sch = ? where famnumb =  ?"
    elif (feature == "50"):
       sql = "UPDATE santascaravan set child4shirt = ? where famnumb =  ?"
    elif (feature == "51"):
       sql = "UPDATE santascaravan set child4pant = ? where famnumb =  ?"
    elif (feature == "52"):
       sql = "UPDATE santascaravan set child4spec = ? where famnumb =  ?"
    elif (feature == "53"):
       sql = "UPDATE santascaravan set child4not = ? where famnumb =  ?"
    elif (feature == "54"):
       sql = "UPDATE santascaravan set child4non1 = ? where famnumb =  ?"
    elif (feature == "55"):
       sql = "UPDATE santascaravan set child4non2 = ? where famnumb =  ?"
    elif (feature == "56"):
       sql = "UPDATE santascaravan set child4non3 = ? where famnumb =  ?"
        
    try:
        #if we call the connection execute method it invisibly creates a cursor for us
        conn.execute(sql, (update_value,update_famnumb))
        #update the change made date log
        sql = "UPDATE santascaravan set changemade = ? where famnumb =  ?"
        changemade = str(now.year) +"/"+str(now.month) +"/"+str(now.day)
        conn.execute(sql, (changemade,update_famnumb)) 
        
    except Error as e:
        print(e)
        pass

def delete_data():
    famnumb_  =  input("Enter the Family Number for the data record to delete:")
    cursor = conn.cursor() #This sets a spot in the database connection (cursor) for targeted retrieval
    cursor.execute("select name from santascaravan where Family Number = "+famnumb_) #create an object referencing the data
    delete_item = cursor.fetchall() # get the data
    confirm = input("Are you sure you want to delete " + famnumb_ + " " + str(delete_item[0]) + "? (Enter 'y' to confirm.)")
    if confirm.lower() == "y":
        try:
            delete_sql = "DELETE FROM santascaravan WHERE famnumb = ?"
            conn.execute(delete_sql,famnumb_)
            result = conn.commit() #capture the result of the commit and use it to check the result
            if result == None:
                print (famnumb_ + " " + str(delete_item[0]) + " deleted.")
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
    print("Welcome to Santa's Carvan Database!")
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
