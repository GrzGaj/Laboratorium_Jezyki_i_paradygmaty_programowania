#optymalizacja rozmieszczenia zadan

#wersja funkcyjne
def optimaizeTaskFunctional(tasks):

    key_func = lambda task: -task['reward'] / task['time']
    sorted_tasks = sorted(tasks, key=key_func)

    total_reward  = sum(map(lambda task: task['reward'], sorted_tasks))


    return total_reward, sorted_tasks

tasks = [
    {'time': 3,'reward': 10},
    {'time': 2,'reward': 5},
    {'time': 1,'reward': 8},
    {'time': 4,'reward': 7}
]
print(optimaizeTaskFunctional(tasks))