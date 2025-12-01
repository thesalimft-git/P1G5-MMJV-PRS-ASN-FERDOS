from datetime import datetime as dt

class BankAccountManagement:
    def __init__(self, accounts:dict):
        self.accounts = accounts
        
    def show_info(self):
        print(self.accounts)
        for id in self.accounts:
            print(f"{id}- {self.accounts[id]['name']} ({self.accounts[id]['balance']})")
   
    def add_user(self, name:str, first_amount:float):
        if not name:
            return {'status': 'error', 'msg': 'name is empty'}
            
        try:
            first_amount = float(first_amount)
        except:
            return {'status': 'error', 'msg': 'amount is not float'}
            
        id = len(self.accounts) + 1
        self.accounts.update({
            str(id): {
                    'name': name, 
                    'balance': first_amount, 
                    'history': [
                        {'time': dt.now().strftime('%Y-%m-%d %H:%M'), 'type': 'deposit', 'amount': first_amount},
                    ],
                    'status': 'active'     
                }
        })
        return {'status': 'ok'}
    
    def tranfer(self, from_who:str, to_whom:str, amount:str): 
        # convert and check data type 
        try:
            from_who = int(from_who)
            to_whom = int(to_whom)
            amount = float(amount)
        except:
            return {'status': 'error', 'msg': 'inputs type are not valid'}          
            
        # check if id exist:
        if from_who not in self.accounts:
            return {'status': 'error', 'msg': 'withdraw user does not exist'}
        if to_whom not in self.accounts:
            return {'status': 'error', 'msg': 'deposite user does not exist'}
        if self.accounts[from_who]['balance'] < amount:
            return {'status': 'error', 'msg': 'withdraw user does not have enough balance'}
           
        try: 
            self.accounts[from_who]['balance'] -= amount
            self.accounts[to_whom]['balance'] += amount
            
            self.accounts[from_who]['history'].append(
                {'time': dt.now().strftime('%Y-%M-%D %H:%M'), type: 'withdraw', 'amount': amount}
            )

            self.accounts[to_whom]['history'].append(
                {'time': dt.now().strftime('%Y-%M-%D %H:%M'), type: 'deposite', 'amount': amount}
            )
            return {'status': 'ok'}
            
        except:
            return {'status': 'error', 'msg': 'some error happend'}
    
    
    
    
    
    
    def deposit(self, id, amount):
        if id not in self.accounts:
            return {'status': 'error', 'msg': 'id does not exist'}
        try: 
            self.accounts[id]['balance'] += amount
        except:
            return {'status': 'error', 'msg': 'something wrong happend'}
        
        return {'status': 'ok'}

       
       
       
       
    def withdraw(self, id, amount):
        if id not in self.accounts:
            return {'status': 'error', 'msg': 'id does not exist'}
        
        if self.accounts[id]['balance'] < amount:
            return {'status': 'error', 'msg': 'insufficient'}
            
        try: 
            self.accounts[id]['balance'] -= amount
        except:
            return {'status': 'error', 'msg': 'something wrong happend'}
        
        return {'status': 'ok'}    
            
