todos = []

while True:
    user_action = input('Type "add", "show" or "exit": ')
    user_action = user_action.strip().lower()

    match user_action:  # match only for python 3.10+
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for todo in todos:
                print(todo)
        case 'exit':
            break

print("Bye!")
