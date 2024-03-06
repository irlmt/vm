from sympy import symbols, simplify, Function, solve, MatrixSymbol
from numpy import arange, array
from numpy import linalg as LA
from docx import Document
from docx.oxml.ns import nsdecls
doc = Document()
table = doc.add_table(rows=1, cols=3)
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
    for step in range(0, len(p_step)-1):
        b = p_step[step]
        e = p_step[step+1]
        s = b
        print("interval ", b, "; ", e)
        for p4 in arange(b, e, s):  # диапазон по р4
            x1 = symbols('x1')
            f = Function('f')
            f = (-p1*(x1**2-x1+p4*x1*p2)/(p1-x1) - (x1**3-x1**2+p4*x1*x1*p2) /
                 (p1-x1) + p5*x1/(1 + p4))/p3 + p4*(p6 - (x1**2-x1+p4*x1*p2)/(p1-x1))
            x1_solution = array(solve(f, x1), dtype=complex)
            x1_solve_temp = [x1_solution[0].real,
                             x1_solution[1].real, x1_solution[2].real]
            for x1_temp in x1_solve_temp:
                x2_temp = (x1_temp**2-x1_temp+p4*x1_temp*p2)/(p1-x1_temp)
                x3_temp = (x1_temp/(1 + p4))
                if (x1_temp <= 0 or x2_temp <= 0 or x3_temp <= 0):
                    print("skip: <= 0")
                else:
                    cells = table.add_row().cells
                    dx1 = (p1 * x2_temp - x1_temp*x2_temp +
                           x1_temp - x1_temp**2) / p2 - p4*x1_temp
                    dx2 = (-p1*x2_temp - x1_temp*x2_temp +
                           p5*x3_temp)/p3 + p4*(p6 - x2_temp)
                    dx3 = x1_temp - x3_temp - p4*x3_temp
                    tmp = []
                    tmp.append(dx1)
                    tmp.append(dx2)
                    tmp.append(dx3)
                    for j in range(3):
                        cells[j].text = str(tmp[j])

doc.save('check_root.doc')
