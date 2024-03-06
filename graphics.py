from sympy import symbols, simplify, Function, solve, MatrixSymbol
from numpy import arange, array
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import style
# style.use('ggplot')
# отдельно сделать массивы и построить графики на одном полотне х от р устойчивые и неустойчивые разных цветов
# проверка и если устойчивые в один если неуст в другой р4 так же
p1 = 8.4e-6
p2 = 6.6667e-4
p3 = 1.7778e-5
p5 = 2
p6_arr = [10, 100]
jacobian_matrix = []
jacobian_matrix_arr = []
x1_solve = []
x2_solve = []
x3_solve = []
y = []
p_step = [0.01, 0.1, 1, 10, 100, 1000]
x1_stable = []
x1_unstable = []
p4_stable = []
p4_unstable = []
x1_none = []
p4_none = []

x2_stable = []
x2_unstable = []
p42_stable = []
p42_unstable = []
x2_none = []
p42_none = []

x3_stable = []
x3_unstable = []
p43_stable = []
p43_unstable = []
x3_none = []
p43_none = []
for p6 in p6_arr:  # разные значения p6
    print("p6 = ", p6)
    j_temp = []
    j_temp_prev = []
    # for step in range(0, len(p_step)-1):
    for step in range(0, len(p_step)-1):
        b = p_step[step]
        e = p_step[step+1]
        s = b
        print("interval ", b, "; ", e)
        for p4 in arange(b, e, s):  # диапазон по р4
            # x1 = symbols('x1', real=True)
            x1 = symbols('x1')
            f = Function('f')
            f = (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
                 (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))
            x1_solution = array(solve(f, x1), dtype=complex)
            # for ch in x1_solution:
            #     if (ch <= complex(0, 0)):
            #         print("skip: x1 <= 0")
            #         continue
            x1_solve_temp = []
            # x1_solve.append(x1_solve_temp)
            # print("x1: ", round(x1_solution[0], 20), round(
            #     x1_solution[1], 20), round(x1_solution[2], 20))
            x1_solve_temp = [x1_solution[0].real,
                             x1_solution[1].real, x1_solution[2].real]
            # if (x1_solve_temp[0] < 0 or x1_solve_temp[1] < 0 or x1_solve_temp[2] < 0):
            #     print("skip: x1 <= 0")
            #     continue
            x1_solve.append(x1_solve_temp)
            x2_solve_temp = []
            x3_solve_temp = []

            for x1_temp in x1_solve_temp:
                x2_solve_temp.append(
                    (x1_temp**2-x1_temp+p4*x1_temp*p2)/(p1-x1_temp))
                x3_solve_temp.append((x1_temp/(1 + p4)))
            x2_solve.append(x2_solve_temp)
            x3_solve.append(x3_solve_temp)
            for i in range(3):
                curr_st = ""
                past_st = "stable"
                if (x1_solve_temp[i].real <= 0 or x2_solve_temp[i].real <= 0 or x3_solve_temp[i].real <= 0):
                    print("skip: <= 0")
                    jacobian_matrix_arr.append([0, 0, 0, "none"])
                    x1_none.append(x1_solve_temp)
                    p4_none.append([p4, p4, p4])
                    x2_none.append(x2_solve_temp)
                    p42_none.append([p4, p4, p4])
                    x3_none.append(x3_solve_temp)
                    p43_none.append([p4, p4, p4])
                    continue
                else:
                    jacobian_matrix = array([[(-x2_solve_temp[i]+1-2*x1_solve_temp[i])/p2 - p4, (p1-x1_solve_temp[i])/p2, 0],
                                            [-x2_solve_temp[i]/p3,
                                            (-p1-x1_solve_temp[i])/p3-p4, p5/p3],
                                            [1, 0, -1-p4]], dtype=complex)
                    # for pr in jacobian_matrix:
                    #     print(pr)
                    wa, va = LA.eig(jacobian_matrix)
                    # for i in range(1, 4):
                    #     cells[i].text = str(wa[i])
                    if (wa[0].real < 0 and wa[1].real < 0 and wa[2].real < 0):
                        j_temp = [wa[0], wa[1], wa[2], "stable"]
                        x1_stable.append(x1_solve_temp)
                        p4_stable.append([p4, p4, p4])
                        x2_stable.append(x2_solve_temp)
                        p42_stable.append([p4, p4, p4])
                        x3_stable.append(x3_solve_temp)
                        p43_stable.append([p4, p4, p4])
                    elif (wa[0].real > 0 or wa[1].real > 0 or wa[2].real > 0):
                        j_temp = [wa[0], wa[1], wa[2], "unstable"]
                        x1_unstable.append(x1_solve_temp)
                        p4_unstable.append([p4, p4, p4])
                        x2_unstable.append(x2_solve_temp)
                        p42_unstable.append([p4, p4, p4])
                        x3_unstable.append(x3_solve_temp)
                        p43_unstable.append([p4, p4, p4])
                    # else:
                    #     j_temp = [wa[0], wa[1], wa[2], "check"]
                    print(j_temp)
                    jacobian_matrix_arr.append(j_temp)
                    curr_st = j_temp[3]
                    # добавить вывод шага
                    # if ((curr_st == "stable" and past_st == "unstable") or (curr_st == "unstable" and past_st == "stable")):

                    # else:

                    # past_st = curr_st
        print()
# plt.scatter(p4_none, x1_none, color='y')
plt.figure(1)
plt.scatter(p4_stable, x1_stable, color='b')
plt.scatter(p4_unstable, x1_unstable, color='g')
plt.xlabel('p4')
plt.ylabel('x1')
plt.figure(2)
plt.scatter(p42_stable, x2_stable, color='b')
plt.scatter(p42_unstable, x2_unstable, color='g')
plt.xlabel('p4')
plt.ylabel('x2')
plt.figure(3)
plt.scatter(p43_stable, x3_stable, color='b')
plt.scatter(p43_unstable, x3_unstable, color='g')
plt.xlabel('p4')
plt.ylabel('x3')
plt.show()
# import matplotlib.pyplot as plt
# import numpy as np


# if __name__ == '__main__':
#     # Интервал изменения переменной по оси X и количество точек на этом интервале
#     xmin = -20.0
#     xmax = 20.0
#     count = 200

#     # Создадим список координат по оси X на отрезке [xmin; xmax], включая концы
#     x = np.linspace(xmin, xmax, count)

#     # Вычислим значение функции в заданных точках
#     y1 = np.sinc(x / np.pi)
#     y2 = np.sinc(x / np.pi * 0.2)
#     y3 = np.sinc(x / np.pi * 2.0)

#     # !!! Нарисуем график в первом окне
#     plt.figure(1)
#     plt.plot(x, y1, label="f(x)")

#     # !!! Нарисуем график во втором окне
#     plt.figure(2)
#     plt.plot(x, y2, label="f(x * 0.2)")
#     plt.legend()

#     # !!! Нарисуем еще один график в первом окне
#     plt.figure(1)
#     plt.plot(x, y3, label="f(x * 2)")
#     plt.legend()

#     # Покажем окна с нарисованными графиками
#     plt.show()
