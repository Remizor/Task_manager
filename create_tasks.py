
# create new task
# def input_new_task():
#     new_task = input('Enter your task here: ')
#     return new_task

def write_to_file(task):
    """input: task text, action: add task text to the file, output: nothing"""
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')

def add_next_task():
    """input: nothing, action: ask user about the next task, if yes, read and add to the file, output: nothing"""
    next_task_question = 'yes'
    while next_task_question == 'yes':
        task = input('Enter your task here: ')
        write_to_file(task)
        next_task_question = input('Do you want to add another task? yes/no >>> ')


if __name__ == "__main__":
    add_next_task()
