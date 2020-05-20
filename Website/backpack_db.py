import sqlite3

DATABASE_FILE = "list.db"

'''Functions'''
def show_backpack(connection):
    '''print the backpack info'''
    try:
        cursor = connection.cursor()
        sql = "SELECT * FROM Contents"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"\n{'Name':<20}{'Descriptiom':<60}")
        for item in results:
            print(f"{item[1]:<20} {item[2]:<60}")
    except:
        print ("Something went wrong with the connection, try again.")

def add_item(connection, item_name, item_definition):
    '''add item to backpack database'''
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Contents(name, definition) VALUES(?,?)"
        cursor.execute(sql,(item_name,item_definition))
        connection.commit()
    except:
        print ("Something went wrong, couldn't add that item.")

def delete_item(connection, item_name):
    ''' delete an item by name from the database'''
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM Contents WHERE name = ?"
        cursor.execute(sql,(item_name,))
        nums_rows_affected = cursor.rowcount
        if nums_rows_affected == 0:
            print ("Can't find item")
        else:
            connection.commit()
    except:
        print ("Something went wrong, that item doesn't exist.")

def update_definition(connection, item_name, new_definition):
    try:
        cursor = connection.cursor()
        sql = "UPDATE Contents SET definition = ? WHERE name = ?"
        cursor.execute(sql,(new_definition,item_name))
        nums_rows_affected = cursor.rowcount
        if nums_rows_affected == 0:
            print ("Can't update item")
        else:
            connection.commit()
    except:
        print ("Something went wrong, couldn't update that item.")

with sqlite3.connect(DATABASE_FILE) as connection:
    #main loop
    while True:
        #got user option
        user_input = input("\nWhat do you want to do?\n1. Print items\n2. Add item\n3. Delete an item by name\n4. Update item's definition\n5. Exit\n")
        #deal with printing
        if user_input == "1":
            show_backpack(connection)
        #now the adding
        elif user_input == "2":
            name = input("Item name: \n")
            definition = input("definition: \n")
            add_item(connection,name,definition)
        #now the deleting an item by name
        elif user_input == "3":
            name = input("Item name: \n")
            delete_item(connection,name)
        #and now the exiting
        elif user_input == "4":
            name = input("Item name: \n")
            definition = input("definition: \n")
            update_definition(connection,name,definition)
        elif user_input == "5":
            print("\n\nGoodbye\n\n")
            break
