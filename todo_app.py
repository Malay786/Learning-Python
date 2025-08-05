#empty list
# todo_list = []
# isTrue = True
# while isTrue:
#     add_todo = input("Enter the task: ")
#     if add_todo == "NULL":
#         isTrue = False
#     todo_list.append(add_todo)
#     print(todo_list)
#
# isTrue = True
# while isTrue:
#     # view todo
#     view_todo = input("Enter the task you want to view: ")
#     if view_todo == "NULL":
#         isTrue = False
#
#     i = 0
#     for todo in todo_list:
#         if view_todo == todo_list[i]:
#             print(todo)
#         i = i+1


todoList = []
isTrue = True
while isTrue:
    inputForTodo = input("what you want to do in  a todo: 'add', 'view', 'quit' : ")
    if inputForTodo == "add":
        addTodo = input("Enter a todo: ")
        todoList.append(addTodo)

    elif inputForTodo == "view":
        i=0
        for todo in todoList:
            print(todoList[i])
            i = i+1

    elif inputForTodo == "quit":
        isTrue = False

    else:
        print("Command is not recognized!")

