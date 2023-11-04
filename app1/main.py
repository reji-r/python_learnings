# print() function takes input from the user and prints it to the screen
# input() function takes input from the user and returns it as a string.
# type() function takes input from the user and returns data type as a string.
user_input = "Enter a todo: "
print("Type of user input: ", type(user_input))
# Multiple todos
todo1 = input(user_input)
todo2 = input(user_input)
todo3 = input(user_input)

todos = [todo1, todo2, todo3, "Hello"]
print(todos)
print("Type of todos: ", type(todos))