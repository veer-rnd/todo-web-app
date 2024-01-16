FILE_PATH = "resource"
FILE_NAME = "todos.txt"


def get_todos(filepath=FILE_PATH, filename=FILE_NAME):
    with open(f"{filepath}/{filename}", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def update_todos(updated_todos, filepath=FILE_PATH, filename=FILE_NAME):
    with open(f"{filepath}/{filename}", 'w') as file_new:
        file_new.writelines(updated_todos)
