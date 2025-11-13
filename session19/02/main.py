from data_manager import DataManager

path = 'session19/02/data.json'
dt = DataManager(path)

try: 
    Tasks = dt.get()
except:
    Tasks = []


def show_menu():
    print("\n--------------------------")
    print("1. View Task")
    print("2. Add Task")
    print("3. Mark Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("\n")

def view_tasks():
    if len(Tasks) > 0:
        for index, task in enumerate(Tasks):
            if task.get('status') != 'deleted':
                print(f"({index}) {task.get('title')}", end = "")
                if task.get('status') == 'completed':
                    print(' (done)')
                if task.get('status') == 'pending':
                    print('')
    else:
        print('no task')


def add_task():
    task = input('insert a task: ')
    if len(task) > 2:
        Tasks.append({'title': task, 'status': 'pending'})
    else:
        print('task must be larger than 3 words')


def complete_task():
    view_tasks()
    try:
        task_id = input('which task to be completed: ')
        Tasks[task_id]['status'] = 'completed'
    except Exception as e:
        print('error: ', e)

def delete_task():
    view_tasks()
    task_id = input('which task to be delete: ')
    Tasks[task_id]['status'] = 'deleted'

def main():
    
    while True:
        show_menu()
        choice = input('select from menu: ')
        
        match choice:
            case '1':
                view_tasks()
            case '2':
                add_task()
            case '3':
                complete_task()
            case '4':
                delete_task()
            case '5':
                dt.set(Tasks)
                break
            case _:
                print('invalid, select only from menu')
        
    
    
    


main()