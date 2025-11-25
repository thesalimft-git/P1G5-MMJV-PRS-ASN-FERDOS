



from datetime import datetime as dt


class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts
        
    def add_user(self, name:str, first_amount:float):
        id = len(self.accounts) + 1
        self.accounts.update({
            id: {
                    'name': name, 
                    'balance': first_amount, 
                    'history': [
                        {'time': dt.now(), type: 'deposit', 'amount': first_amount},
                    ],
                    'status': 'active'     
                }
        })
        return True
    
    def record_tranfer(self, from_who, to_whom, amount):
        self.accounts
    