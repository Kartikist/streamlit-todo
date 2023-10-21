FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        
      
def complete_todos(dones):
    with open('dones.txt', 'a+') as done:
        done.writelines(dones)

def get_done_todos():
    with open('dones.txt', 'r') as file_local:
        
        done_todos_local = file_local.readlines()
        # top5 = done_todos_local[:5]
    return done_todos_local

if __name__ == "__main__":
    print("Hello")
    print(get_todos())