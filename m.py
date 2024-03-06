from sympy import symbols, simplify, Function, solve, MatrixSymbol
from numpy import arange, array
from numpy import linalg as LA
from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH

# создание пустого документа
doc = Document()
# добавляем пустую таблицу 2х2 ячейки
# f1 = (p1 * x2 - x1*x2 + x1 - x1**2) / p2 - p4*x1
# f2 = (-p1*x2 - x1*x2 + p5*x3)/p3 + p4*(p6 - x2)
# f3 = x1 - x3 - p4*x3
# x1, x2, x3 = symbols('x1 x2 x3')
# p1, p2, p3, p4, p5, p6 = symbols('p1 p2 p3 p4 p5 p6')
# f = Function('f')
# f = (-p1*x2 - x1*x2 + p5*x3)/p3 + p4*(p6 - x2)
# jacobian_matrix = MatrixSymbol('jacobian_matrix', 3, 3)
# jacobian_matrix = [[(-x2+1-2*x1)/p2 - p4, (p1-x1)/p2, 0],
#                    [-x2/p3, (-p1-x1)/p3-p4, p5/p3],
#                    [1, 0, -1-p4]]
# f = f.subs([(x3, x1/(1 + p4)), (x2, (x1**2-x1+p4*x1*p2)/(p1-x1))])
# params = [8.4e-6, 6.6667e-4, 1.7778e-5, 0, 2]
# p6Arr = [10, 100]

# f = f.subs([(p1, params[0]), (p2, params[1]),
#            (p3, params[2]), (p5, params[4])])
# p_step = [0.01, 0.1, 1, 10, 100, 1000]
# x1_solve = []
# x2_solve = []
# x3_solve = []
# p_step = [0.01, 0.1, 1, 10, 100, 1000]
# for p6_temp in p6Arr:
#     f = f.subs(p6, p6_temp)
#     print("p6 = ", p6_temp)
#     for step in range(0, len(p_step)-1):
#         b = p_step[step]
#         e = p_step[step+1]
#         s = b
#         print("interval ", b, ": ", e)
#         for p4_temp in arange(b, e, s):  # диапазон по р4
#             f = f.subs(p4, p4_temp)
#             x1_solve = solve(f, x1)
#             for x1_solve_temp in x1_solve:
#                 x2_solve.append(((x1**2-x1+p4*x1*p2)/(p1-x1)
#                                  ).subs([(x1, x1_solve_temp), (p4, p4_temp), (p2, params[1])]))
#                 x3_solve.append(
#                     (x1/(1 + p4)).subs([(x1, x1_solve_temp), (p4, p4_temp)]))
#             for i in range(0, 3):
#                 for j in range(0, 3):
#                     for r in range(0, 3):
#                         if not (isinstance(jacobian_matrix[i][j], int)):
#                             jacobian_matrix[i][j] = jacobian_matrix[i][j].subs([(x1, x1_solve[r]), (x2, x2_solve[r]), (p1, params[0]), (
#                                 p2, params[1]), (p3, params[2]), (p4, p4_temp), (p5, params[4])])
#             # wa, va = LA.eig(jacobian_matrix)
#             # print(wa)
#             # LA.det(jacobian_matrix)

#             print(jacobian_matrix)
#             # print(x1_solve)
#             print()
# print(f)
# устойчивые неустойчивые стац точки
# точки вещественной и комплексной бифуркации если они есть
# норма матрицы якоби должна быть меньше 1 чтобы все сходилось
# собств значения м якоби целая часть меньше 0 значит сходится
# графики зависиости решений от р4
# подумать как лучше организовать графики
# оставить мнимые решения или нет
# какой интервал р4 подходит лучше всего
# x1, x2, x3 = symbols('x1 x2 x3')
# p1, p2, p3, p4, p5, p6 = symbols('p1 p2 p3 p4 p5 p6')
# f = Function('f')


# def foo(x1, p4, p6):
#     p1 = 8.4e-6
#     p2 = 6.6667e-4
#     p3 = 1.7778e-5
#     p5 = 2
#     return (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
#             (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))


p1 = 8.4e-6
p2 = 6.6667e-4
p3 = 1.7778e-5
p5 = 2
p6_arr = [10, 100]
jacobian_matrix = []
# f = (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
#      (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))
# print(f)
# params = [8.4e-6, 6.6667e-4, 1.7778e-5, 0, 2]
# p6Arr = [10, 100]

# f = f.subs([(p1, params[0]), (p2, params[1]),
#            (p3, params[2]), (p5, params[4])])
# p_step = [0.01, 0.1, 1, 10, 100, 1000]
x1_solve = []
x2_solve = []
x3_solve = []
p_step = [0.01, 0.1, 1, 10, 100, 1000]
for p6 in p6_arr:  # разные значения p6
    print("p6 = ", p6)
    # for step in range(0, len(p_step)-1):
    for step in range(0, len(p_step)-1):
        b = p_step[step]
        e = p_step[step+1]
        s = b
        print("interval ", b, "; ", e)
        for p4 in arange(b, e, s):  # диапазон по р4
            # x1 = symbols('x1', real=True)
            x1 = symbols('x1')
            # f = Function('f')
            f = (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
                 (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))
            x1_solution = array(solve(f, x1), dtype=complex)
            x1_solve_temp = []
            # x1_solve.append(x1_solve_temp)
            # print(x1_solution[0].real,
            #       x1_solution[1].real, x1_solution[2].real)
            x1_solve_temp = [x1_solution[0].real,
                             x1_solution[1].real, x1_solution[2].real]
            x1_solve.append(x1_solve_temp)
            x2_solve_temp = []
            x3_solve_temp = []
            for x1_temp in x1_solve_temp:
                x2_solve_temp.append(
                    (x1_temp**2-x1_temp+p4*x1_temp*p2)/(p1-x1_temp))
                x3_solve_temp.append((x1_temp/(1 + p4)))
            x2_solve.append(x2_solve_temp)
            x3_solve.append(x3_solve_temp)
            # for temp_x1 in x1_solve_temp:
            #     for temp_x2 in x2_solve_temp:
            #         # if not (isinstance(jacobian_matrix[i][j], int)):
            #         jacobian_matrix = [[(-temp_x2+1-2*temp_x1)/p2 - p4, (p1-temp_x1)/p2, 0],
            #                            [-temp_x2/p3,
            #                             (-p1-temp_x1)/p3-p4, p5/p3],
            #                            [1, 0, -1-p4]]
            # wa, va = LA.eig(jacobian_matrix)
            # print(wa)
            # LA.det(jacobian_matrix)
            # for pr in jacobian_matrix:
            #     print(pr)
            # print()
            # print(jacobian_matrix)

            # print(jacobian_matrix)
            # print(x1_solve)
            # print()
        print()
        table = doc.add_table(rows=9, cols=3)
        table.style = 'Table Grid'
        for i in range(9):
            for j in range(3):
                cell = table.cell(i, j)
                if (x2_solve[i][j] <= 0):
                    cell.text = '-'
                else:
                    cell.text = str(x3_solve[i][j])

        table.add_row()
        # print(x1_solve)
        x1_solve = []
        x2_solve = []
        x3_solve = []
doc.save('res2.doc')
