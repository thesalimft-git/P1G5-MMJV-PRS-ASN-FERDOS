





class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts
        
    def add_user(self, name:str, first_amount:float):
        id = len(self.accounts) + 1
        self.accounts.update({
            id: {
                    'owner': name, 
                    'balance': first_amount, 
                    'transactions': [
                        {'time': '202 ???? ', type: 'deposit', 'amount': first_amount},
                    ],
                    'status': 'active'     
                }
        })
    
    