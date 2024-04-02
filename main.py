import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def choose_function():
    print('1. x**3 - x  + 4')
    print('2. x**3 + 4.81x**2 - 17.37x + 5.38')
    print('3. sin(x) + 0.1')
    print('4. sin(x) + cos(2x) + 1')
    func_number = int(input('Введите номер функции: '))
    if func_number > 4 or func_number < 1:
        return -1
    return func_number


def choose_system():
    print('1. x**2 + y**2 = 4 \n\t y = 3*x**2 ')
    print('2. 2*x*y + 3*y**2 - 5 \n\t x + 3*y**2 - 7')
    system_number = int(input('Введите номер системы: '))
    if system_number > 4 or system_number < 1:
        return -1
    return system_number


def func(number, x):
    if number == 1:
        return x ** 3 - x + 4
    elif number == 2:
        return x ** 3 + 4.81 * (x ** 2) - 17.37 * x + 5.38
    elif number == 3:
        return np.sin(x) + 0.1
    elif number == 4:
        return math.sin(x) + math.cos(2 * x) + 1


def system(number, x, y):
    if number == 1:
        first_line = 4 - x ** 2 - y ** 2
        second_line = 3 * x ** 2 - y
        return first_line, second_line
    elif number == 2:
        first_line = 5 - 2 * x * y - 3 * y ** 2
        second_line = 7 - x - 3 * y ** 2
        return first_line, second_line
    else:
        return -1


def diff_system(number, x, y):
    if number == 1:
        df_dx = 2 * x
        df_dy = 2 * y
        dg_dx = -6 * x
        dg_dy = 1
        return df_dx, df_dy, dg_dx, dg_dy
    elif number == 2:
        df_dx = 2 * y
        df_dy = 2 * x + 6 * y
        dg_dx = 1
        dg_dy = 6 * y
        return df_dx, df_dy, dg_dx, dg_dy


def diff_func(number, x):
    if number == 1:
        return 3 * x ** 2 - 1
    elif number == 2:
        return 3 * x ** 2 + 9.62 * x - 17.37
    elif number == 3:
        return np.cos(x)
    elif number == 4:
        return math.cos(x) - 2 * math.sin(2 * x)


def get_parameter(number):
    a = float(input("Введите точку a: "))
    b = float(input("Введите точку b: "))
    if a > b:
        print('Сначала должно быть введено значение расположенное левее, попробуйте ещё раз')
        while a > b:
            a = float(input("Введите точку a: "))
            b = float(input("Введите точку b: "))
    if func(number, a) * func(number, b) > 0:
        print('На данном интервале более одного корня, либо их вовсе нет')
        print()
        return
    e = float(input("Введите точночть: "))
    if e < 0:
        while e < 0:
            print('Точность не может быть меньше нуля, попробуйте ещё раз')
            e = float(input("Введите точночть: "))
    return a, b, e


def get_system_parameter():
    x = float(input("Введите точку x: "))
    y = float(input("Введите точку y: "))
    e = float(input("Введите точночть: "))
    if e < 0:
        while e < 0:
            print('Точность не может быть меньше нуля, попробуйте ещё раз')
            e = float(input("Введите точночть: "))
    return x, y, e


def draw_graph(number, a, b):
    if abs(b - a) > 5:
        print('Отрезок слишком велик, попробуйте уменьшить границы отрезка')
    fig, ax = plt.subplots()
    ax.set_title('График функции')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    x = np.linspace(a - 3, b + 3)
    y = []
    for val in x:
        y.append(func(number, val))
    ax.plot(x, y)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()


def draw_system(number, x_min, x_max):
    if number == 1:
        fig, ax = plt.subplots()
        ax.set_title('График функции')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        x = np.linspace(x_min - 3, x_max + 3)
        y_1 = []
        for val in x:
            if 4 - val ** 2 >= 0:
                y_1.append(math.sqrt(4 - val ** 2))
            else:
                y_1.append(np.nan)
        ax.plot(x, y_1)
        y_2 = []
        for val in x:
            y_2.append(3*val**2)
        ax.plot(x, y_2)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.show()
    if number == 2:
        fig, ax = plt.subplots()
        ax.set_title('График функции')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        x = np.linspace(x_min - 3, x_max + 3)
        y_1 = []
        for val in x:
            y_1.append(-val/3-math.sqrt(val**2+15)/3)
        ax.plot(x, y_1)
        y_2 = []
        for val in x:
            y_2.append(math.sqrt(7-val)/3)
        ax.plot(x, y_2)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        plt.show()


def get_method():
    max_iteration = 50
    while True:
        print('\t', '1: Метод половинного деления.')
        print('\t', '2: Метод секущих.')
        print('\t', '3: Метод простой итерации.')
        print('\t', '4: Метод Ньютона.')
        try:
            param = int(input('Введите номер метода, который хотите использовать: '))
            if param == 1:
                number = choose_function()
                if number == -1:
                    print('Функции с таким номером нет')
                    get_method()
                a, b, e = get_parameter(number)
                half_division_method(number, a, b, e, max_iteration)
            elif param == 2:
                number = choose_function()
                if number == -1:
                    print('Функции с таким номером нет')
                    get_method()
                a, b, e = get_parameter(number)
                secant_method(number, e, a, b, max_iteration)
            elif param == 3:
                number = choose_function()
                if number == -1:
                    print('Функции с таким номером нет')
                    get_method()
                a, b, e = get_parameter(number)
                simple_iteration_method(number, a, b, e, max_iteration)
            elif param == 4:
                number = choose_system()
                if number == -1:
                    print('Системы с таким номером нет')
                    get_method()
                a, b, e = get_system_parameter()
                # equation1 = input("Введите первое уравнение системы: ")
                # equation2 = input("Введите второе уравнение системы: ")
                newton_method(number, a, b, e, max_iteration)
        except TypeError:
            print('Ошибка: вы ввели некорректный параметр')
        # except ValueError:
        #     print('Ошибка: значение введено неверно')


def half_division_method(number, a, b, e, max_iteration):
    iteration = 0
    draw_graph(number, a, b)
    table = []
    while abs(a - b) > e:
        x_val = (a + b) / 2
        division = abs(a - b)
        f_a = float(func(number, a))
        f_b = float(func(number, b))
        f_x = float(func(number, x_val))
        if (f_a < 0 and f_x < 0 and f_b > 0) or (f_a > 0 and f_x > 0 and f_b < 0):
            a = x_val
        elif (f_a < 0 and f_x > 0 and f_b > 0) or (f_a > 0 and f_x < 0 and f_b < 0):
            b = x_val
        iteration += 1
        row = [iteration, a, b, x_val, f_a, f_b, f_x, division]
        table.append(row)
        if iteration > max_iteration:
            print("Количество итераций превысило лимит: " + str(iteration))
            return
    if abs(a - b) < e:
        x_val = (a + b) / 2
        division = abs(a - b)
        f_a = float(func(number, a))
        f_b = float(func(number, b))
        f_x = float(func(number, x_val))
        if (f_a < 0 and f_x < 0 and f_b > 0) or (f_a > 0 and f_x > 0 and f_b < 0):
            a = x_val
        elif (f_a < 0 and f_x > 0 and f_b > 0) or (f_a > 0 and f_x < 0 and f_b < 0):
            b = x_val
        iteration += 1
        row = [iteration, a, b, x_val, f_a, f_b, f_x, division]
        table.append(row)
    headers = ["№ итерации", "a", "b", "x", "F(a)", "F(b)", "F(x)", "|a-b|"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))


def secant_method(number, e, x_prev, x_i, max_iteration):
    x_next = 0
    iteration = 0
    draw_graph(number, x_prev, x_i)
    table = []
    while abs(x_next - x_i) > e:
        if iteration != 0:
            x_prev = x_i
            x_i = x_next
        iteration += 1
        f_x = float(func(number, x_i))
        f_x_prev = float(func(number, x_prev))
        x_next = x_i - ((x_i - x_prev) / (f_x - f_x_prev)) * f_x
        row = [iteration, x_prev, x_i, x_next, f_x, abs(x_next - x_i)]
        table.append(row)
        if iteration > max_iteration:
            print("Количество итераций превысило лимит: " + str(iteration))
            return
    headers = ["№ итерации", "x_prev", "x", "x_next", "F(x_next)", "|a-b|"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))


def simple_iteration_method(number, a, b, e, max_iteration):
    f_a = float(diff_func(number, a))
    f_b = float(diff_func(number, b))
    draw_graph(number, a, b)
    method_lambda = -1 / max(f_a, f_b)
    table = []
    left_interval_check = float(method_lambda * diff_func(number, a) + 1)
    right_interval_check = float(method_lambda * diff_func(number, b) + 1)
    # print(left_interval_check)
    # print(right_interval_check)
    if (left_interval_check < 1) and (right_interval_check < 1):
        print('условие сходимости выполняется!')
        x_i = a
        x_next = float(method_lambda * func(number, x_i) + x_i)
        iteration = 0
        while abs(x_next - x_i) > e:
            fi = float(method_lambda * func(number, x_next) + x_next)
            if iteration != 0:
                x_i = x_next
                x_next = fi
            f_value = float(func(number, x_next))
            row = [iteration, x_i, x_next, fi, f_value, abs(x_next - x_i)]
            table.append(row)
            iteration += 1
            if iteration > max_iteration:
                print("Количество итераций превысило лимит: " + str(iteration))
                return
    headers = ["№ итерации", "x", "x_next", "ф", "F(x_next)", "|a-b|"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))


def newton_method(number, a, b, e, max_iteration):
    x_0 = 0
    y_0 = 0
    x_i = a
    y_i = b
    iteration = 0
    draw_system(number, a-1, a+1)
    while abs(x_i - x_0) > e or abs(y_i - y_0) > e:
        x_0 = x_i
        y_0 = y_i
        iteration += 1
        df_dx, df_dy, dg_dx, dg_dy = diff_system(number, x_0, y_0)
        print(f'df/dx = {str(df_dx)}  df/dy = {str(df_dy)}  dg/dx = {str(dg_dx)}  dg/dy = {str(dg_dy)}')

        first_line, second_line = system(number, x_0, y_0)
        # print(first_line)
        # print(second_line)
        left_side = np.array([[df_dx, df_dy], [dg_dx, dg_dy]])
        right_side = np.array([first_line, second_line])
        delta_x, delta_y = np.linalg.inv(left_side).dot(right_side)
        print(f'Δx = {delta_x}')
        print(f'Δy = {delta_y}')

        x_i = x_0 + delta_x
        y_i = y_0 + delta_y
        # print(x_i)
        # print(y_i)
        if iteration > max_iteration:
            print("Количество итераций превысило лимит")
            return
    print("Количество итерации: " + str(iteration))
    print(f'В итоге значение x = {x_i}')
    print(f'В итоге значение y = {y_i}')


get_method()
