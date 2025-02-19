#optymalizacja rozmieszczenia zadan

#wersja proceduralna
def optimaizeTaskProcedura(tasks):
    #sortowanie zadań malejąco według wartości nagroda/czas
    tasks.sort(key=lambda x: -x['reward'] / x['time'])
    total_reward = 0
    total_time = 0
    task_order = []

    for task in tasks:
        task_order.append(task)
        total_time += task['time']
        total_reward += task['reward']

    return total_reward, task_order

tasks = [
    {'time': 3,'reward': 10},
    {'time': 2,'reward': 5},
    {'time': 1,'reward': 8},
    {'time': 4,'reward': 7}
]
print(optimaizeTaskProcedura(tasks))