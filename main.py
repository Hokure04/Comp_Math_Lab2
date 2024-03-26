from sympy import *
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


def choose_function():
    print('1. x**3 - x  + 4')
    print('2. x**3 - 2.92*(x**2) + 1.435*x + 0.791')
    print('3. sin(x) + 0.1')
    func_number = int(input('Введите номер функции: '))
    return func_number


def choose_system():
    print('1. x**2 + y**2 = 4 \n\t y = 3*x**2 ')
    print('2. -0.1*x**2 - 0.2*y**2 + 0.3 \n\t -0.2*x**2 - 0.1*x*y + 0.7')
    system_number = int(input('Введите номер системы: '))
    return system_number


def func(number, x):
    if number == 1:
        return x ** 3 - x + 4
    elif number == 2:
        return x ** 3 - 2.92 * (x ** 2) + 1.435 * x + 0.791
    elif number == 3:
        return np.sin(x) + 0.1


def system(number, x, y):
    if number == 1:
        first_line = 4 - x ** 2 - y ** 2
        second_line = 3 * x ** 2 - y
        return first_line, second_line
    elif number == 2:
        first_line = -0.1*x**2 - 0.2*y**2 + 0.3
        second_line = -0.2*x**2 - 0.1*x*y + 0.7
        return first_line, second_line


def diff_system(number, x, y):
    if number == 1:
        df_dx = 2 * x
        df_dy = 2 * y
        dg_dx = -6 * x
        dg_dy = 1
        return df_dx, df_dy, dg_dx, dg_dy
    if number == 2:
        df_dx = -0.2*x
        df_dy = -0.4*y
        dg_dx = -0.4*x-0.1*y
        dg_dy = -0.1*x
        return df_dx, df_dy, dg_dx, dg_dy


def diff_func(number, x):
    if number == 1:
        return 3 * x ** 2 - 1
    elif number == 2:
        return 3 * x ** 2 - 5.84 * x + 1.435
    elif number == 3:
        return np.cos(x)


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
    a = float(input("Введите точку a: "))
    b = float(input("Введите точку b: "))
    if a > b:
        print('Сначала должно быть введено значение расположенное левее, попробуйте ещё раз')
        while a > b:
            a = float(input("Введите точку a: "))
            b = float(input("Введите точку b: "))
    e = float(input("Введите точночть: "))
    if e < 0:
        while e < 0:
            print('Точность не может быть меньше нуля, попробуйте ещё раз')
            e = float(input("Введите точночть: "))
    return a, b, e


def draw_graph(number, a, b):
    if abs(b - a) > 1.9:
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


def get_method():
    max_iteration = 50
    while True:
        print('\t', '1: Метод половинного деления.')
        print('\t', '2: Метод секущих.')
        print('\t', '3: Метод простой итерации.')
        print('\t', '4: Метод Ньютона.')
        param = int(input('Введите номер метода, который хотите использовать: '))
        try:
            if param == 1:
                number = choose_function()
                a, b, e = get_parameter(number)
                half_division_method(number, a, b, e, max_iteration)
            elif param == 2:
                number = choose_function()
                a, b, e = get_parameter(number)
                secant_method(number, e, a, b, max_iteration)
            elif param == 3:
                number = choose_function()
                a, b, e = get_parameter(number)
                simple_iteration_method(number, a, b, e, max_iteration)
            elif param == 4:
                number = choose_system()
                a, b, e = get_system_parameter()
                # equation1 = input("Введите первое уравнение системы: ")
                # equation2 = input("Введите второе уравнение системы: ")
                newton_method(number, a, b, e, max_iteration)
        except TypeError:
            print('Ошибка: вы ввели некорректный параметр')
        except ValueError:
            print('Ошибка: значение параметра не может быть пустым')


def half_division_method(number, a, b, e, max_iteration):
    iteration = 0
    draw_graph(number, a, b)
    table = []
    while abs(a - b) > e:
        x_val = (a + b) / 2
        f_a = float(func(number, a))
        f_b = float(func(number, b))
        f_x = float(func(number, x_val))

        if (f_a < 0 and f_x < 0 and f_b > 0) or (f_a > 0 and f_x > 0 and f_b < 0):
            a = x_val
        elif (f_a < 0 and f_x > 0 and f_b > 0) or (f_a > 0 and f_x < 0 and f_b < 0):
            b = x_val
        iteration += 1
        row = [iteration, a, b, x_val, f_a, f_b, f_x, abs(a - b)]
        table.append(row)
        if iteration > max_iteration:
            print("Количество итераций превысило лимит: " + str(iteration))
            return
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
    # Удаляем пробелы из ввода уравнений
    # equation1 = equation1.replace(" ", "")
    # equation2 = equation2.replace(" ", "")

    # Проверяем, в каком уравнении находится равно и меняем стороны уравнения
    # if "=" in equation1:
    #     parts = equation1.split("=")
    #     equation1 = parts[0] + "-(" + parts[1] + ")"
    # else:
    #     parts = equation1.split("=")
    #     equation1 = parts[1] + "-" + parts[0]
    #
    # if "=" in equation2:
    #     parts = equation2.split("=")
    #     equation2 = parts[0] + "-(" + parts[1] + ")"
    # else:
    #     parts = equation2.split("=")
    #     equation2 = parts[1] + "-" + parts[0]
    # x, y = symbols('x y')
    # func1 = sympify(equation1)
    # func2 = sympify(equation2)
    df_dx, df_dy, dg_dx, dg_dy = diff_system(number, a, b)
    print(str(df_dx) + "   " + str(df_dy) + "   " + str(dg_dx) + "   " + str(dg_dy))
    # delta_x, delta_y = symbols('delta_x, delta_y')d
    # first_line = df_dx * delta_x + df_dy * delta_y
    # second_line = dg_dx * delta_x + dg_dy * delta_y
    # print(first_line)
    # print(second_line)
    first_line, second_line = system(number, a, b)
    print(first_line)
    print(second_line)
    left_side = np.array([[df_dx, df_dy], [dg_dx, dg_dy]])
    right_side = np.array([first_line, second_line])
    delta_x, delta_y = np.linalg.inv(left_side).dot(right_side)
    print(delta_x)
    print(delta_y)
    x_0 = a
    y_0 = b
    x_i = x_0 + delta_x
    y_i = y_0 + delta_y
    print(x_i)
    print(y_i)
    iteration = 0
    while abs(x_i - x_0) > e or abs(y_i - y_0) > e:
        x_0 = x_i
        y_0 = y_i
        iteration += 1
        df_dx, df_dy, dg_dx, dg_dy = diff_system(number, x_0, y_0)
        print(str(df_dx) + "   " + str(df_dy) + "   " + str(dg_dx) + "   " + str(dg_dy))

        first_line, second_line = system(number, x_0, y_0)
        print(first_line)
        print(second_line)
        left_side = np.array([[df_dx, df_dy], [dg_dx, dg_dy]])
        right_side = np.array([first_line, second_line])
        delta_x, delta_y = np.linalg.inv(left_side).dot(right_side)
        print(delta_x)
        print(delta_y)

        x_i = x_0 + delta_x
        y_i = y_0 + delta_y
        print(x_i)
        print(y_i)
        # first_right_part = -1 * func1
        # second_right_part = -1 * func2
        # first_right_part = first_right_part.subs(x, x_0)
        # first_right_part = float(first_right_part.subs(y, y_0))
        # second_right_part = second_right_part.subs(x, x_0)
        # second_right_part = float(second_right_part.subs(y, y_0))
        # # print(first_right_part)
        # # print(second_right_part)
        # first_left_part = first_line.subs(x, x_0)
        # first_left_part = first_left_part.subs(y, y_0)
        # second_left_part = second_line.subs(x, x_0)
        # second_left_part = second_left_part.subs(y, y_0)
        # # print(first_left_part)
        # # print(second_left_part)
        # parts = str(first_left_part).split(" + ")
        # if len(parts) == 1:
        #     parts = str(first_left_part).split(" - ")
        # var2 = sympify(parts[1])
        # final_delta_x = (first_right_part - var2) / df_dx.subs(x, x_0)
        # second_left_part = second_left_part.subs(delta_x, final_delta_x)
        # # print(second_left_part)
        # parts_2 = str(second_left_part).split(" + ")
        # if len(parts_2) == 1:
        #     parts_2 = str(second_left_part).split(" - ")
        # var2 = sympify(parts_2[1])
        # var1 = parts_2[0].split("*")
        # multiplier = var1[0]
        # final_delta_y = (second_right_part - var2) / float(multiplier)
        # final_delta_x = final_delta_x.subs(delta_y, final_delta_y)
        # x_i = a + final_delta_x
        # y_i = b + final_delta_y
        if iteration > max_iteration:
            print("Количество итераций превысило лимит")
            return
    print("Найденный корни уравнения: ")
    print(x_i)
    print(y_i)


get_method()
