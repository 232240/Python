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

#main code
while True:
    user_input = input("What would you like to do? \n1. Print all cards \n2. Exit")
    if user_input == "1":
        print_all_cards()
    if user_input == "2":
        break
    else:
        print("That was not an option.")
        