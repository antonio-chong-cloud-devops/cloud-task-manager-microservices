tasks = [
    {"id": 1, "title": "Primera tarea"},
    {"id": 2, "title": "Segunda tarea"}
]

def get_all_tasks():
    return tasks

def create_task(task):
    tasks.append(task.dict())
    return task