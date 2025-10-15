import time


def control_time(func):
    def wrapper(*args, **kwargs):
        time_begin = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        time_result = time_end - time_begin
        print(f'Время выполнения: {time_result:.9f} секунд')
    return wrapper


@control_time
def add(a, b):
    result = a + b
    print(f'Итоговая сумма двух чисел: {result}')


def work_with_files():
    with open("input.txt", "r") as f:
        numbers = f.read().split()

    a, b = map(float, numbers)
    result = a + b

    with open("output.txt", "w") as f:
        f.write(str(result))


add(3,4)
work_with_files()
