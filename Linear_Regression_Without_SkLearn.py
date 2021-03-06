# -*- coding: utf-8 -*-
"""LinearRegressionWithoutSklearn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L976P9mq-GsgzlGo2HO_gKA4FmnJbYQf
"""

import matplotlib.pyplot as plt

x_yrs_of_exp=[3,8,9,13,3,6,11,21,1,16]
y_salary=[30,57,64,72,36,43,59,90,20,83]

mean_x=sum(x_yrs_of_exp)/len(x_yrs_of_exp)
mean_x

mean_y=sum(y_salary)/len(y_salary)
mean_y

G=[]
L=[]
prod=[]
for m in x_yrs_of_exp:
  X=m-mean_x
  G.append(X)
for n in y_salary:
  Y=n-mean_y
  L.append(Y)
for m in range(0,len(x_yrs_of_exp)):
  a=round(G[m]*L[m],2)
  prod.append(a)
prod

sum_prod=sum(prod)
sum_prod

sqr=[round(m**2,2) for m in G]
print(sqr)
sum_sqr=round(sum(sqr),2)
print(sum_sqr)

w1=round(sum_prod/sum_sqr,2)
print(w1)

w0=mean_y-w1*mean_x
print(w0)

prediction=[]
#y_eq=w0+w1*x hypothesis equation
for x in x_yrs_of_exp:
  y_pred=w0+w1*x
  prediction.append(y_pred)

plt.scatter(x_yrs_of_exp, y_salary, color = "red")
plt.plot(x_yrs_of_exp, prediction, color = "green")
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()