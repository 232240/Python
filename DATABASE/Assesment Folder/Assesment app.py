#docstring - Aayush Chand - Arenas database application
#import
import sqlite3
#import colours
from colorama import init, Fore, Style
# Initialize Colorama
init()
#constants and variables
DATABASE = "CR_Arenas.db"

#funtions
def find_arena_by_trophies():
    '''search for the qarena the user is in from their input trophies amount'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    try:
        trophies = int(input("Enter your current trophy count: "))
        sql = "SELECT * FROM Arenas WHERE Trophies_Required <= ? ORDER BY Trophies_Required DESC LIMIT 1;"
        cursor.execute(sql, (trophies,))
        results = cursor.fetchone()
        for arena in results:
            print(f"{Fore.LIGHTGREEN_EX}You're currently in: {arena[1]}{Style.RESET_ALL}")
        if trophies:
            print("No matching arena found.")
    except ValueError:
        print("Please enter a valid number.")
    db.close()
def compare_arenas():
    '''Compare the stats of 2 arenas'''
    #take arena names
    a1 = input("Enter first arena name: ")
    a2 = input("Enter second arena name: ")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Name, Trophies_Required, Number_of_rewards, Reward_types FROM Arenas WHERE Name COLLATE NOCASE IN (?, ?)"
    cursor.execute(sql, (a1, a2))
    results = cursor.fetchall()
    #loop through all the results
    print(f"{Fore.GREEN}Arena Comparison:\n")
    for arena in results:
        print(f"{Fore.LIGHTGREEN_EX}{arena[0]:<30}{Fore.LIGHTYELLOW_EX}{arena[1]:<20}{Fore.LIGHTRED_EX}{arena[2]:<20}{Fore.LIGHTCYAN_EX}{arena[3]:<30}{Style.RESET_ALL}")
    #loop finish here
    db.close()
def add_arena():
    '''add an arena to the database'''
    #take in the information provided by the user
    Name = input(f"{Fore.GREEN}Arena name: {Style.RESET_ALL}")
    Trophies = int(input(f"{Fore.YELLOW}Trophies required: {Style.RESET_ALL}"))
    Number_of_rewards = int(input(f"{Fore.LIGHTGREEN_EX}Number of rewards: {Style.RESET_ALL}"))
    Reward_types = (input(f"{Fore.CYAN}Reward types: {Style.RESET_ALL}"))
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #code to add the arena
    sql = "INSERT INTO Arenas (Name, Trophies_required, Number_of_rewards, Reward_types) VALUES (?, ?, ?, ?);"
    cursor.execute(sql, (Name, Trophies, Number_of_rewards, Reward_types))
    #save and close
    db.commit()
    db.close()
def delete_arena():
    '''remove an arena from the database'''
    #take the name
    name = input(f"{Fore.RED} Enter the name of the arena to delete: {Style.RESET_ALL}")
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    #code to delete it from the database and save it
    sql = "DELETE FROM Arenas WHERE Name = ?"
    cursor.execute(sql, (name,))
    db.commit()
    #check if the entered arena exists and if the deletion was successful
    if cursor.rowcount > 0:
        print(f"{Fore.RED}Arena deleted{Style.RESET_ALL}")
    else:
        print(f"{Fore.LIGHTBLUE_EX}Arena not found{Style.RESET_ALL}")
    db.close()
def print_all_arenas():
    '''print all the arenas nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Arenas;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"\n{Fore.LIGHTGREEN_EX}    Name              {Fore.LIGHTYELLOW_EX}Trophies Required    {Fore.LIGHTRED_EX}Number of Rewards          {Fore.LIGHTCYAN_EX}Reward Types{Style.RESET_ALL}\n")
    for arena in results:
        print(f"{Fore.LIGHTGREEN_EX}{arena[1]:<30}{Fore.LIGHTYELLOW_EX}{arena[2]:<20}{Fore.LIGHTRED_EX}{arena[3]:<20}{Fore.LIGHTCYAN_EX}{arena[4]:<30}{Style.RESET_ALL}")
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
    print(f"\n{Fore.LIGHTGREEN_EX}    Name              {Fore.LIGHTYELLOW_EX}Trophies Required    {Fore.LIGHTRED_EX}Number of Rewards          {Fore.LIGHTCYAN_EX}Reward Types{Style.RESET_ALL}\n")
    for arena in results:
        print(f"{Fore.LIGHTGREEN_EX}{arena[1]:<30}{Fore.LIGHTYELLOW_EX}{arena[2]:<20}{Fore.LIGHTRED_EX}{arena[3]:<20}{Fore.LIGHTCYAN_EX}{arena[4]:<30}{Style.RESET_ALL}")
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
    print(f"\n{Fore.LIGHTGREEN_EX}    Name              {Fore.LIGHTYELLOW_EX}Trophies Required    {Fore.LIGHTRED_EX}Number of Rewards          {Fore.LIGHTCYAN_EX}Reward Types{Style.RESET_ALL}\n")
    for arena in results:
        print(f"{Fore.LIGHTGREEN_EX}{arena[1]:<30}{Fore.LIGHTYELLOW_EX}{arena[2]:<20}{Fore.LIGHTRED_EX}{arena[3]:<20}{Fore.LIGHTCYAN_EX}{arena[4]:<30}{Style.RESET_ALL}")
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
    print(f"\n{Fore.LIGHTGREEN_EX}    Name              {Fore.LIGHTYELLOW_EX}Trophies Required    {Fore.LIGHTRED_EX}Number of Rewards          {Fore.LIGHTCYAN_EX}Reward Types{Style.RESET_ALL}\n")
    for arena in results:
        print(f"{Fore.LIGHTGREEN_EX}{arena[1]:<30}{Fore.LIGHTYELLOW_EX}{arena[2]:<20}{Fore.LIGHTRED_EX}{arena[3]:<20}{Fore.LIGHTCYAN_EX}{arena[4]:<30}{Style.RESET_ALL}")
    #loop finish here
    db.close()
#main code
while True:
    user_input = input(f"""
    {Fore.MAGENTA}What would you like to do?{Style.RESET_ALL}
    {Fore.LIGHTGREEN_EX}1. Print all arenas
    2. Print all arenas by trophies
    3. Print all arenas by number of rewards
    4. Print all arenas in alphabetical order{Style.RESET_ALL}
    {Fore.LIGHTBLUE_EX}5. Add an arena to the table
    6. Find your current arena{Style.RESET_ALL}
    {Fore.BLUE}7. Compare two arenas{Style.RESET_ALL}
    {Fore.LIGHTRED_EX}8. Delete an arena from the table
    9. Exit{Style.RESET_ALL}
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
        find_arena_by_trophies()
    elif user_input == "7":
       compare_arenas()
    elif user_input == "8":
        delete_arena()
    elif user_input == "9":
        break
    else:
        print("That was not an option\n")
