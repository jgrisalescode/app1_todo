todos = []

while True:
    user_action = input('Type "add", "show", "edit", "complete" or "exit": ')
    user_action = user_action.strip().lower()

    match user_action:  # match only for python 3.10+
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # Store a file object with open()
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
                file.close()

        case 'show' | 'display':  # OR Operator
            for index, item in enumerate(todos):
                # print(index, '-', item)
                print(f"{index + 1}-{item}")
        case 'edit':
            user_number = int(input('Number of the todo to edit: '))
            todo_number = user_number - 1
            new_todo = input("Enter new todo: ")
            todos[todo_number] = new_todo
        case 'complete':
            user_number = int(input('Number of the todo to complete: '))
            todos.pop(user_number - 1)
        case 'exit':
            break
        case _:  # You can call this variable as you want, _ is a convention
            print("Hey, you entered an unknown command")

print("Bye!")
