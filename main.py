todos = []

while True:
    user_action = input('Type "add", "show" or "exit": ')

    match user_action: # match only for python 3.10+
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Bye!")
