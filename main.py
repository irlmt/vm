from sympy import symbols, simplify, Function, solve, MatrixSymbol
from numpy import arange, array
from numpy import linalg as LA
p1 = 8.4e-6
p2 = 6.6667e-4
p3 = 1.7778e-5
p5 = 2
p6_arr = [10, 100]
jacobian_matrix = []
x1_solve = []
x2_solve = []
x3_solve = []
p_step = [0.01, 0.1, 1, 10, 100, 1000]
for p6 in p6_arr:  # разные значения p6
    print("p6 = ", p6)
    for step in range(0, len(p_step)-1):
        b = p_step[step]
        e = p_step[step+1]
        s = b
        print("interval ", b, ": ", e)
        for p4 in arange(b, e, s):  # диапазон по р4
            # x1 = symbols('x1', real=True)
            x1 = symbols('x1')
            f = Function('f')
            f = (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
                 (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))
            x1_solution = solve(f, x1)
            x1_solve_temp = []
            print("x1:", x1_solution)
            # x1_solve.append(x1_solve_temp)
            # print(round(x1_solve_temp[0], 20), round(
            #     x1_solve_temp[1], 20), round(x1_solve_temp[2], 20))
            # x1_solve_temp = [round(x1_solution[0], 20), round(
            #     x1_solution[1], 20), round(x1_solution[2], 20)]
            # x1_solve.append(x1_solve_temp)
            x1_solve.append(x1_solution)
            x2_solve_temp = []
            x3_solve_temp = []
            # for x1_temp in x1_solve_temp:
            #     x2_solve_temp.append(
            #         (x1_temp**2-x1_temp+p4*x1_temp*p2)/(p1-x1_temp))
            #     x3_solve_temp.append((x1_temp/(1 + p4)))
            for x1_temp in x1_solution:
                x2_solve_temp.append(
                    (x1_temp**2-x1_temp+p4*x1_temp*p2)/(p1-x1_temp))
                x3_solve_temp.append((x1_temp/(1 + p4)))
            x2_solve.append(x2_solve_temp)
            x3_solve.append(x3_solve_temp)
            # for temp_x1 in x1_solve_temp:
            for temp_x1 in x1_solution:
                for temp_x2 in x2_solve_temp:
                    # if not (isinstance(jacobian_matrix[i][j], int)):
                    jacobian_matrix = [[(-temp_x2+1-2*temp_x1)/p2 - p4, (p1-temp_x1)/p2, 0],
                                       [-temp_x2/p3,
                                        (-p1-temp_x1)/p3-p4, p5/p3],
                                       [1, 0, -1-p4]]
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
