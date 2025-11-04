import random

path = 'session16/part02/data.txt'
wincard = { 'p': 's', 'r': 'p', 's': 'r' }
counter = 0
pcwin = 0
hwin = 0

with open(path, 'w') as f:
    while True:
        pc_choice = random.choice([item for item in wincard.keys()])
        h_choice = input('select from r/p/s: ')

        if h_choice == 'end':
            break
        elif h_choice == pc_choice:
            print('the same, try again')
            continue
        elif h_choice not in [item for item in wincard.keys()]:
            print('is not valid, try again')
            continue
        elif h_choice == wincard.get(pc_choice):
            print('win')
            hwin += 1
        else:
            print('loss')
            pcwin += 1
            
        counter += 1
        f.write(f'{counter}- pc: {pc_choice}, h: {h_choice}\n')
    f.write(f'\n\n\npc: {pcwin}, h: {hwin}\n')
            
            
            
            
            

