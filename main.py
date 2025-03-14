from sympy import symbols
import pandas as pd
from matplotlib import pyplot as plt

# Вариант 3
k, T, C, L = symbols('k C T L')

#Контейнер расчета
# 1 способ
C_ost=120000
Am_lst=[]
C_ost_lst=[]
for i in range(10):
  Am = (C-L)/T
  C_ost -= Am.subs({C: 120000, T:10, L:0})
  Am_lst.append(round(Am.subs({C: 120000, T:10, L:0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst )

# 2 способ
Aj=0
C_ost=120000
Am_lst_2=[]
C_ost_lst_2=[]
for i in range(10):
  Am = k * 1/T * (C - Aj)
  C_ost -= Am.subs({C: 120000, T:10, k:2})
  Am_lst_2.append(round(Am.subs({C: 120000, T:10, k:2}), 2))
  Aj += Am
  C_ost_lst_2.append(round(C_ost, 2))
print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)

#Контейнер табличного вывода
Y = range(1, 11)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)

#Контейнер визуализации
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns = ['Y', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns = ['Y', 'Am_lst_2'])

plt.bar(tfame['Y'], tfame2['Am_lst_2'])
plt.show()

# Сосед сделал всё правильно