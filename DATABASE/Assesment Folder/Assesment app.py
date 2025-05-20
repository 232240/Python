#docstring - Aayush Chand - Arenas database application
#import
import sqlite3
#import colours
from colorama import Fore, Style, init
init()

print(f"{Fore.GREEN}This will be green text!{Style.RESET_ALL}")

from text_colours import TextColours
t = TextColours()
#constants and variables
DATABASE = "CR_Arenas.db"

#funtions
def add_arena():
    Name = input("Arena name: ")
    Trophies = int(input("Trophies required: "))
    Number_of_rewards = int(input("Number of rewards: "))
    Reward_types = (input("Reward types: "))

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "INSERT INTO Arenas (Name, Trophies_required, Number_of_rewards, Reward_types) VALUES (?, ?, ?, ?);"
    cursor.execute(sql, (Name, Trophies, Number_of_rewards, Reward_types))
    db.commit()
    db.close()
def delete_arena():
    name = input("Enter the name of the arena to delete: ")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "DELETE FROM Arenas WHERE Name = ?"
    cursor.execute(sql, (name,))
    db.commit()
    if cursor.rowcount > 0:
        print("Arena deleted")
    else:
        print("Arena not found")
    db.close()
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
    5. Add an arena to the table
    6. Delete an arena from the table
    7. Exit
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
       add_arena()
    elif user_input == "6":
       delete_arena()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")