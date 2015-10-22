import sqlite3

conn = sqlite3.connect('dogrecord.db')

def createTable():
    conn.execute("CREATE TABLE if not exists DOG_INFO( \
ID INTEGER PRIMARY KEY AUTOINCREMENT, \
NAME TEXT, \
GENDER TEXT, \
MICROCHIP INT, \
BREED TEXT \
);")


def printData(data):
    for row in data:
        print "Id:", row[0]
        print "Name:", row[1]
        print "Gender:", row[2]
        print "Microchip:", row[3]
        print "Breed:", row[4], "\n"


def newDog():
    print '\nAdding a new dog...'

    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Microchip: ')
    occupation = raw_input('Breed: ')

    #create values part of sql command
    val_str = "'{}', '{}', {}, '{}'".format(\
    name, gender, age, occupation)

    sql_str = "INSERT INTO DOG_INFO \
    (NAME, GENDER, MICROCHIP, BREED) \
    VALUES ({});".format(val_str)
    print sql_str

    conn.execute(sql_str)
    conn.commit()
    print "Number of changes:", conn.total_changes


def viewAll():
    #create sql string
    sql_str = "SELECT * from DOG_INFO"
    cursor = conn.execute(sql_str)


    #get data from cursor in array
    rows = cursor.fetchall()
    print rows

def viewDetails():
    print "\nViewing dog records"

    # take name input
    name = raw_input("Enter the dog name: ")
    sql_str = "SELECT * from DOG_INFO where NAME='{}'".format(name)

    cursor = conn.execute(sql_str)
    
    #Get data in array form
    rows = cursor.fetchall()

    #if no data in array, print the data
    if len(rows) == 0:
        print 'No records found'
    else:
        printData(rows)

def deleteDog():
    print "\nDeleting a Dog"

    # take name input
    name = raw_input("Enter the dog name: ")
    sql_str = "SELECT * from DOG_INFO where NAME='{}'".format(name)

    cursor = conn.execute(sql_str)
    
    #Get data in array form
    rows = cursor.fetchall()
    # ID to change
    change_id = 0
    
    #if no data in array, print the data
    if len(rows) == 0:
        print 'No records found'
        #End the function
        return
    elif len(rows) == 1:
        print 'One record found'
        #Select row
        row = rows[0]
        #Select id
        change_id = row[0]
        printData(rows)
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input('Type the ID of the dog to delete: ')

    print "Change ID:", change_id

    delete = raw_input("Confirm dog deletion (y/n): ")

    if delete == "y":
        sql_str = "DELETE from DOG_INFO where ID={}".format(change_id)
        conn.execute(sql_str)
        conn.commit()
        print "Number of changes: ", conn.total_changes

def options():
    #print out the options
    print '\nWhat would you like to do?'
    print '1. Add a new dog'
    print '2. View all dogs'
    print '3. Search for a dog'
    print '4. Delete a dog'
    print '5. Exit'

    #ask user what they want to do
    response = raw_input('Enter your option number: ')

    #check the user response
    if response == '1':
        newDog()
    elif response == '2':
        viewAll()
    elif response == '3':
        viewDetails()
    elif response == '4':
        deleteDog()
    else:
        print 'Exiting...'
        return

def mainLoop():
    in_loop = True
    while in_loop == True:
        #run options function
        options()
        #ask user if they want to continue
        again = raw_input(\
            'Return to Menu? (y/n) ')
        # if answer does not equal 'y', exit loop
        if again != 'y':
            in_loop = False
    
    
createTable()
#newDog()
#viewAll()
#viewDetails()
#deleteDog()
mainLoop()
