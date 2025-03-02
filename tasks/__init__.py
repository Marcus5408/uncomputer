import os
import importlib
import random

def get_random_task():
    # Get all Python files in tasks directory except __init__.py
    tasks_dir = os.path.dirname(__file__)
    task_files = [f[:-3] for f in os.listdir(tasks_dir) 
                 if f.endswith('.py') and f != '__init__.py']
    
    print(task_files)
    
    if not task_files:
        return None
        
    # Select and import random task
    task_name = random.choice(task_files)
    task_module = importlib.import_module(f'tasks.{task_name}')
    return task_module.create_task_window

if __name__ == '__main__':
    task = get_random_task()
    if task:
        task(None)
    else:
        print("No tasks available")