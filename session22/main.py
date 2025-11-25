from data import accounts
from bank_account_management import BankAccountManagement

def show_menu():
    print('\n\n\n------------------')
    print('1- Show All')
    print('2- Add user')
    print('3- Transfer')

def main():
    bam = BankAccountManagement(accounts)
    while True:
        show_menu()
        command = input('select from menu: ')
        match command:
            case '1':
                bam.show_info()
            case '2':
                pass
                
        
        
main()