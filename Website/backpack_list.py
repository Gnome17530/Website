""" This is a list that stores items the can either be
viewed, added or removed by the user of the code."""

'''Functions'''
def show_backpack():
    '''print the backpack info'''
    print(f"{'Index':<8}{'Name':<20}{'Descriptiom':<60}")
    i = 0
    for item in backpack:
        print(f"{i:<8}{item[0]:<20} {item[1]:<60}")
        i+=1

def get_item():
    '''get item and describe to user'''
    item = input("Name?")
    description = input("Description?")
    backpack.append((item, description))

def add_item(item_name, item_description):
    '''add an item and description to the backpack'''
    backpack.append((item_name, item_description))

def delete_item(item_index):
    '''delete an item from backpack by index'''
    try:
        del backpack[item_index]
    except:
        print("That item does not excist")


#this is the main backpack list
backpack = list()



#main loop
while True:
    #got user option
    user_input = input("\nWhat do you want to do?\n1. Print backpack content\n2. Add item\n3. Delete an item\n4. Exit\n")
    #deal with printing
    if user_input == "1":
        show_backpack()
    #now the adding
    elif user_input == "2":
        get_item()
    #now the deleting
    elif user_input == "3":
        item = input("\nWhat item index do you want to delete?\n")
        delete_item(item)
    #and now the exiting
    elif user_input == "4":
        print("\n\nGoodbye!\n\n")
        break


