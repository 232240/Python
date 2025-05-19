#docstring - Aayush Chand - Arenas database application
#import
import sqlite3

#constants and variables
DATABASE = "CR_Arenas.db"

#funtions
def print_all_arenas():
    '''print all the arenas nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Arenas;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name              Trophies Required    Number of Rewards          Reward Types\n")
    for arena in results:
        print(f"{arena[1]:<30}{arena[2]:<20}{arena[3]:<20}{arena[4]:<30}")
    #loop finish here
    db.close()
def print_all_arenas_by_trophies():
    '''print all the arenas by trophies'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Arenas ORDER BY Trophies_required;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name              Trophies Required    Number of Rewards          Reward Types\n")
    for arena in results:
        print(f"{arena[1]:<30}{arena[2]:<20}{arena[3]:<20}{arena[4]:<30}")
    #loop finish here
    db.close()
def print_all_arenas_by_number_of_rewards():
    '''print all the arenas by number of rewards'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Arenas ORDER BY Number_of_rewards DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name              Trophies Required    Number of Rewards          Reward Types\n")
    for arena in results:
        print(f"{arena[1]:<30}{arena[2]:<20}{arena[3]:<20}{arena[4]:<30}")
    #loop finish here
    db.close()
def print_all_arenas_by_alphabet():
    '''print all the arenas in alphabetical order'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Arenas ORDER BY Name ASC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name              Trophies Required    Number of Rewards          Reward Types\n")
    for arena in results:
        print(f"{arena[1]:<30}{arena[2]:<20}{arena[3]:<20}{arena[4]:<30}")
    #loop finish here
    db.close()
#main code
while True:
    user_input = input("""
    What would you like to do?
    1. Print all arenas
    2. Print all arenas by trophies
    3. Print all arenas by number of rewards
    4. Print all arenas by alphabetical order
    5. Exit
    """)
    if user_input == "1":
       print_all_arenas()
    elif user_input == "2":
       print_all_arenas_by_trophies()
    elif user_input == "3":
       print_all_arenas_by_number_of_rewards()
    elif user_input == "4":
       print_all_arenas_by_alphabet()
    elif user_input == "5":
        break
    else:
        print("That was not an option\n")