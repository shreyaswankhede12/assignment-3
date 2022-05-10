import numpy as np
import pandas as pd
from sympy import false
import statistics as stat

def f(x,y):
    return x*y

A = pd.read_excel(r"C:\Users\SHREYAS\Desktop\Book2.xlsx",'Sheet1')
B = np.array(pd.DataFrame(A,columns=['salary']))
C = np.array(pd.DataFrame(A,columns=['frequency']))
D = pd.DataFrame(f(B,C))
D.to_excel(excel_writer=r'C:\Users\SHREYAS\Desktop\book3.xlsx',header=false, index=false)
sum_freq = int(np.sum(C))
sum_salary = int(np.sum(D))
print("Mean salary of workers is: ",sum_salary/sum_freq)

salary=np.array([5000,5000,5000,5000,15000])
median=stat.median(salary)
print("the median of salaries is: ",median)

mode=stat.mode(salary)
print("the mode of salaries is: ",mode)