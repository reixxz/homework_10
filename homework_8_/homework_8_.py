import time

def task_to_measure():

    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sorted(my_list)
    print("Відсортований список:", sorted_list)

def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Час виконання функції:", execution_time, "секунд")

measure_time(task_to_measure)
