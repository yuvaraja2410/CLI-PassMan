import sqlite3
import argparse
import openpyxl

class DataBase():
    try:
        dbase = sqlite3.connect("PassMan.db")
        dbase.execute('''create table demo(name text,username text,password text);''')
    except:
        print()

    def save_data(self,name,user,password):
        dbase = sqlite3.connect("PassMan.db")
        dbase.execute('''insert into demo values('{}','{}',{});'''.format(name,user,password))
        dbase.commit()
        print("Your credentials has been Stored successfully.\n")

    def display_data(self,name,all):
        dbase = sqlite3.connect("PassMan.db")
        
        if all == 1 and name == None:
            dis = dbase.execute('''select * from demo''')
            lenth = 0
            for i in dis:
                temp = "|"+i[0]+"  |  "+str(i[1])+"  |  "+str(i[2])+"|"
                lenth = len(temp)
                print("_"*lenth)
                print(temp)
            print("_"*lenth)
        
        if name != None and all == None:
            dis = dbase.execute('''select * from demo where name = '{}';'''.format(name))
            lenth = 0
            for i in dis:
                temp = "|"+i[0]+"  |  "+str(i[1])+"  |  "+str(i[2])+"|"
                lenth = len(temp)
                print("_"*lenth)
                print(temp)
            print("_"*lenth)
                 

 
    

class SaveCommand(DataBase):
    def __init__(self,args):
        db = DataBase()
        db.save_data(args.name,args.user,args.password)

class DisplayCommand(DataBase):
    def __init__(self,args):
        db = DataBase()
        db.display_data(args.name,args.all)

class Logo():
    def logo(self):
        print(" _____              __  __             \n|  __ \            |  \/  |            \n| |__) |_ _ ___ ___| \  / | __ _ _ __  \n|  ___/ _` / __/ __| |\/| |/ _` | '_ \ \n| |  | (_| \__ \__ \ |  | | (_| | | | |\n|_|   \__,_|___/___/_|  |_|\__,_|_| |_|\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")  


def main():
    logo = Logo()
    logo.logo()

    parser = argparse.ArgumentParser(description="PassMan - The CLI Password Manager.")
    subparser = parser.add_subparsers(dest="command", help="Avilable command in PassMan.")

    #save mode
    save_subparser = subparser.add_parser("save", help="To save username and password for specific application or website.")
    save_subparser.add_argument("-n", "--name", help="Flage used to enter the name of the website or application.",required=True)
    save_subparser.add_argument("-u", "--user", help="Flage used to enter the username used in website or application.",required=True)
    save_subparser.add_argument("-p", "--password", help="Flage used to enter the name of the website or application.",required=True)

    #dislpay mode
    display_subparser = subparser.add_parser("display", help="To display all the saved user credentials for all/specific application or website.")
    display_subparser.add_argument("-n", "--name", help="Flage used to display credentials like username and password for given name.",default=None)
    display_subparser.add_argument("-a", "--all", help="Flage used to display credentials like username and password for given name.", action="count")
    
    mode_parser = parser.parse_args()

    #Execution by mode
    if mode_parser.command == "save":
        save_command_object = SaveCommand(mode_parser)

    if mode_parser.command == "display":
        display_command_object = DisplayCommand(mode_parser)
    

if __name__ == "__main__":
    main()