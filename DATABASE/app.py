#docstring- Aayush Chand- Cards database application
#import
import sqlite3

#constants and variables
DATABASE = "Cards.db"

#funtions
def print_all_cards():
    '''print all the cards nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Card;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name                       HP                   Rarity")
    for card in results:
        print(f"{card[1]:<30}{card[2]:<20}{card[3]:<20}")
    #loop finish here
    db.close()
def print_all_cards_by_rarity():
    '''print all the cards by rarity'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Card ORDER BY Rarity DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name                       HP                   Rarity")
    for card in results:
        print(f"{card[1]:<30}{card[2]:<20}{card[3]:<20}")
    #loop finish here
    db.close()
def print_all_cards_by_hp():
    '''print all the cards by hp'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Card ORDER BY hp DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print("    Name                       HP                   Rarity")
    for card in results:
        print(f"{card[1]:<30}{card[2]:<20}{card[3]:<20}")
    #loop finish here
    db.close()
#main code
while True:
    user_input = input("\nWhat would you like to do?\n1. Print all cards\n2. All cards by Rarity\n3. Show cards sorted by HP\n4. Exit\n")
    if user_input == "1":
       print_all_cards()
    elif user_input == "2":
       print_all_cards_by_rarity()
    elif user_input == "3":
       print_all_cards_by_hp()
    elif user_input == "4":
       break
    else:
        print("That was not an option\n")
        