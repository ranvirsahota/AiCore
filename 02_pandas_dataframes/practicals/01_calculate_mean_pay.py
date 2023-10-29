import pandas as pd

salaries = pd.read_csv('Salaries.csv')

#Fire Department
fire_dept = salaries.loc[salaries['JobTitle'].str.contains('FIRE DEPARTMENT', regex=True)]

#Police Department
police_dept = salaries.loc[salaries['JobTitle'].str.contains('POLICE DEPARTMENT', regex=True)]

#What is the ratio between people in the fire department over people in the police department? 
# Fire Department   :    Police Department
# 88                :                       116
# 22                :                       29
# GCF = 4
fire_dept_count = len(fire_dept)
police_dept_count = len(police_dept)
print(f'{fire_dept_count} : {police_dept_count}')

lower_department = lambda x, y: x if x < y else y
for num in reversed(range(lower_department(fire_dept_count, police_dept_count) + 1)):
    if (fire_dept_count % num == 0 and police_dept_count % num == 0):
        print(f'{round(fire_dept_count/num)} : {round(police_dept_count/num)}')
        break

#What is the mean salary of the police department? Use the BasePay column.
# Answer = 151947.28689655173
print(police_dept['BasePay'].mean())

#What is the mean salary of the fire department? Use the BasePay column.
print(fire_dept['BasePay'].mean())
