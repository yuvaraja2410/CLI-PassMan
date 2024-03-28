import openpyxl
import argparse
import sqlite3
import os

def logoDisplayer():
    print(" _____              __  __             \n|  __ \            |  \/  |            \n| |__) |_ _ ___ ___| \  / | __ _ _ __  \n|  ___/ _` / __/ __| |\/| |/ _` | '_ \ \n| |  | (_| \__ \__ \ |  | | (_| | | | |\n|_|   \__,_|___/___/_|  |_|\__,_|_| |_|\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")  

def argumentManager():
    parser = argparse.ArgumentParser() 

    parser.add_argument("-n", "--name", default=None, help="Name of the app or Website for that username and password to be stored" ,action='count')
    parser.add_argument("-u", "--user", default=None, help="Enter the username of mail address", action='count')
    parser.add_argument("-p", "--password", default=None, help="Enter the password for the specified app or website", action='count')
    parser.add_argument("-ex", "--exportfile", help="To export your password as xlsx file", action="count")
    parser.add_argument("-d", "--display", default=None, help="To display the stored password", action="count")
    parser.add_argument("-up", "--update", default=None, help="To update the password", action="count")

    argument = parser.parse_args()

    dbase = sqlite3.connect("PassMan.db")
    snum = 1
    sno = open("num.txt",'a')
    sno.write(str(snum))
    try:
        dbase.execute('''create table PassMan(
                sno text,
                name text,
                username text,
                password text
            );''')
    except:
        print("Table already exist")

    def update(dbase):
        dbase.execute('''insert into PassMan values('{}','{}','{}','{}');'''.format(sno,argument.name,argument.user,argument.password))
        snum = int()

    # if argument.update == 1 and  argument.display != 1:
    update(dbase)

    # if argument.display == 1 and argument.update != 1:
    #     display(dbase)

    

    def display(dbase):
        upd = dbase.execute('''select * from PassMan''')
        for i in upd:
            print(str(i[0])+"    "+str(i[1])+"   "+str(i[2])+"   "+str(i[3])) 

    sno.write(snum)

def main():
    logoDisplayer()
    argumentManager()

if __name__ == "__main__":
    main()