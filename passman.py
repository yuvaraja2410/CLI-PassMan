import sqlite3
import argparse
import openpyxl

class DataBase():
    dbase = sqlite3.connect("PassMan.db")
    try:
        dbase.execute('''create table demo(name text,username text,password text);''')
    except:
        print()

    def save_data(self,name,user,password):
        dbase = sqlite3.connect("PassMan.db")
        dbase.execute('''insert into demo values('{}','{}',{});'''.format(name,user,password))
        dbase.commit()

        #E for displaying content in DB
        # upd = dbase.execute('''select * from demo''')
        # for i in upd:
        #     print(i[0]+"    "+str(i[1])+"   "+str(i[2])) 
    

class SaveCommand(DataBase):
     
    def __init__(self,args):
        print(args.user)
        db = DataBase()
        db.save_data(args.name,args.user,args.password)
    

def logo():
        print(" _____              __  __             \n|  __ \            |  \/  |            \n| |__) |_ _ ___ ___| \  / | __ _ _ __  \n|  ___/ _` / __/ __| |\/| |/ _` | '_ \ \n| |  | (_| \__ \__ \ |  | | (_| | | | |\n|_|   \__,_|___/___/_|  |_|\__,_|_| |_|\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n")  

def main():
    logo()

    parser = argparse.ArgumentParser(description="PassMan - The CLI Password Manager.")
    subparser = parser.add_subparsers(dest="command", help="Avilable command in PassMan.")

    #save mode
    save_subparser = subparser.add_parser("save", help="To save username and password for specific application or website.")
    save_subparser.add_argument("-n", "--name", help="Flage used to enter the name of the website or application",required=True)
    save_subparser.add_argument("-u", "--user", help="Flage used to enter the username used in website or application",required=True)
    save_subparser.add_argument("-p", "--password", help="Flage used to enter the name of the website or application",required=True)
    
    save_parser = parser.parse_args()

    #Save_Command_instance_creation
    save_command_object = SaveCommand(save_parser)
    

if __name__ == "__main__":
    main()