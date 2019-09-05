import numpy as np
import matplotlib.pyplot as plt
from datetime import date
 

# data to plot
n_groups = 1
f = open("SumOfIncome.txt","r")
sum_of_income = float(f.readline())
f.close()
 
f = open("SumOfOutcome.txt","r")
sum_of_outcome = float(f.readline())
f.close()

balance = sum_of_income - sum_of_outcome

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, sum_of_income, bar_width,
alpha=opacity,
color='g',
label='Income')
 
rects2 = plt.bar(index + bar_width, sum_of_outcome, bar_width,
alpha=opacity,
color='r',
label='Outcome')

if(balance < 0):
    rects3 = plt.bar(index + bar_width*2, balance, bar_width,
    alpha=opacity,
    color='black',
    label='Balance')
elif(balance >= 0):
    rects3 = plt.bar(index + bar_width*2, balance, bar_width,
    alpha=opacity,
    color='blue',
    label='Balance')
    
 
plt.xlabel('Date')
plt.ylabel('CAD')
plt.title('Summary of Current Balance')
today = date.today()
plt.xticks(index + bar_width, [str(today)])
plt.legend()
 
plt.tight_layout()
plt.show()