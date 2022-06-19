import random


def read_all_tasks(file_name):
    """Input: file name, Action: get all tasks and add to list, Output: list of tasks"""
    with open(file_name) as file:
        read_data = file.read()
        tasks_list = read_data.split('\n')
        good_tasks_list = []
        for task in tasks_list:
            if task != '':
                good_tasks_list.append(task)
        return good_tasks_list

# better solutions:
# Option 1
# def read_all_tasks_2(file_name):
#     """Input: file name, Action: get all tasks and add to list, Output: list of tasks"""
#     with open(file_name) as file:
#         tasks = []
#         for task in file:
#             task = task.strip()
#             if task != '':
#                 tasks.append(task)
#         return tasks
# Option 2
# def read_all_tasks_3(file_name):
#     """Input: file name, Action: get all tasks and add to list, Output: list of tasks"""
#     with open(file_name) as file:
#         return [task.strip() for task in file if task.strip() != '']



print(read_all_tasks('tasks.txt'))
task_list = read_all_tasks('tasks.txt')

def choose_random_task(task_list):
    """Input: list of tasks, Action: choose random task, Output: print selected task"""
    task = random.choice(task_list)
    print('Your task for today is ' + task + "!")

choose_random_task(task_list)