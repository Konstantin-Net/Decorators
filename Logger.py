def log_file_path(way):     # Функция принимает путь куда записывать лог-файл

    def logger(old_function):       # Функци декоратор-логер
        import time

        def new_function(*args, **kwargs):      # Функция-обёртка
            something = old_function(*args, **kwargs)
            with open(f"{way}\\logs.txt", "a", encoding='utf-8') as f:
                f.write(f"Время вызова: {time.ctime()}\n")
                f.write(f"Имя функции: {old_function.__name__}\n")
                f.write(f"Аргументы функции: {args}\n")
                f.write(f"Возвращаемое значение: {something}\n\n")
        return new_function
    return logger


file_way = input("Введите путь для записи логов:\n")     # Задаваемый путь для записи логов


@log_file_path(file_way)
def func_1(x, y):
    return x + y


@log_file_path(file_way)
def func_2(x, y):
    return x - y


@log_file_path(file_way)
def func_3(x, y):
    return x * y


res1 = func_1(4, 3)
res2 = func_2(45, 14)
res3 = func_3(12, 13)
print("Лог записан")
