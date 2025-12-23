import json
import random
import string
from pathlib import Path

class Bank:
    # transfer the data from json to dummy 
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exist")
    except Exception as err:
        print(f"An exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        aplha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = aplha+ num + spchar
        random.shuffle(id)
        return "".join(id)


    def Createaccount(self):
        info = {
            "name" : input("Tell your name: "),
            "age" : int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("Tell your pin")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0        
        }
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()
    
    def depositemoney(self):
        accnumber = input("Please tell ypur account number")
        pin = int(input("Please tell your pin"))
        

user = Bank()    
print("Press 1 for creating account")
print("Press 2 for depositing money in the bank")
print("Press 3 for withdrawing the money")
print("Press 4 for deatils")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

check = int(input("Tell your response:- "))

if check==1:
    user.Createaccount()

if check ==2:
    user.depositemoney()

