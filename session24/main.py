from data_manager import DataManager
from bank_account_management import BankAccountManagement

dm = DataManager()
try: 
    accounts = dm.get()
except:
    accounts = dict()
    
bam = BankAccountManagement(accounts)

def show_menu():
    print('\n\n\n------------------')
    print('1- Show All')
    print('2- Add user')
    print('3- Transfer')
    print('4- Deposite')
    print('5- Withdraw')
    print('6- Exit')
  

def add_user():
    name = input('insert name: ')
    first_amount = input('insert amount: ')
    result = bam.add_user(name, first_amount)
    if result['status'] == 'ok':
        print(f"{name} is addedd successfully")
        
    if result['status'] == 'error':
        print(result['msg'])    

def transfer():
    from_who = input('from who: ')
    to_whom = input('to whom: ')
    amount = input('amont: ')
    
    result = bam.tranfer(from_who, to_whom, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        print('transfer is done')

def deposit():
    id = input('account id: ')
    amount = input('amount: ')
    
    result = bam.deposit(id, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        print('transfer is done')

def withdraw():
    id = input('account id: ')
    amount = input('amount: ')
    
    result = bam.withdraw(id, amount)
    if result['status'] == 'error':
        print(result['msg'])
    else:
        print('transfer is done')

def main():
    while True:
        show_menu()
        dm.set(accounts)
        command = input('select from menu: ')
        if command == '1':
            bam.show_info()
        elif command == '2':
            add_user()
        elif command == '3':
            transfer()
        elif command == '4':
            deposit()
        elif command == '5':
            withdraw()
        elif command == '6':
            break
        else:
            print('wring choice, try again')
            


                
        
        
main()