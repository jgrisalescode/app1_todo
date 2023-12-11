todos = []

while True:
    user_action = input('Type "add", "show", "edit" or "exit": ')
    user_action = user_action.strip().lower()

    match user_action:  # match only for python 3.10+
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':  # OR Operator
            for todo in todos:
                print(todo)
        case 'edit':
            user_number: int(input('Number of the todo to edit: '))
            todo_number = user_number - 1
            new_todo = input("Enter new todo: ")
            todos[todo_number] = new_todo
        case 'exit':
            break
        case _:  # You can call this variable as you want, _ is a convention
            print("Hey, you entered an unknown command")

print("Bye!")
