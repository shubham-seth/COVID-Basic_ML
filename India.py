# INDIA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("daily-cases-covid-19.csv")
data = data.values.tolist()
data_india = []
data_india.append(['India', 'IND', 'Mar 1, 2020', 0])
data_india.append(['India', 'IND', 'Mar 2, 2020', 0])
for d in data:
	if(d[0] == "India" and d[2][:3]!="Feb" and d[2][:3]!="Jan"):
		data_india.append(d)
del data

for d in data_india:
	if(d[2][:3] == "Apr"):
		d.append(31)
	elif(d[2][:3] == "Mar"):
		d.append(0)
	elif(d[2][:3] == "May"):
		d.append(61)
	
	i=4
	sum = 0
	while(d[2][i] != ","):
		sum *= 10
		sum += int(d[2][i])
		i += 1
	d[4] += sum

x = []
y = []
for d in data_india:
	x.append(d[4])
	y.append(d[3])
del data_india

x = np.array(x)
y = np.array(y)

x_max = np.max(x)
y_max = np.max(y)

x = x/x_max
y = y/y_max

a = np.random.random([1])
b = np.random.random([1])
c = np.random.random([1])
d = np.random.random([1])

# Training
'''
learn_rate = 1e-3
reg = 1e-3
loss = []
d = 0
best_mse = 5
for i in range(15000):
	y_pred = ((a*x)/(x**2+b*x+c)) + d
	mse = np.sum((y-y_pred)**2) + (reg/2)*(a**2+b**2+c**2)
	m = 2*(y-y_pred)
	grad_a = -np.sum(m*(y_pred-d)/a)+reg*a
	grad_b = np.sum(m*((y_pred-d)**2/a))+reg*b
	grad_c = np.sum(m*((y_pred)**2/(a*x)))+reg*c
	# grad_d = -np.sum(m)

	a -= grad_a*learn_rate
	b -= grad_b*learn_rate
	c -= grad_c*learn_rate
	# d -= grad_d*learn_rate
	if(mse < best_mse):
		best_mse = mse
		best_pred = y_pred

	loss.append(mse)

plt.plot(loss)
plt.show()
'''

a = [0.3173847]
b = [-2.67588615]
c = [2.0180911] 
d = 0
x = np.arange(180)
x = x/x_max
best_pred = ((a*x)/(x**2+b*x+c)) + d
print(a, b, c, d)
plt.scatter(x[:len(y)]*x_max,y*y_max,c='blue')
for i in range(len(best_pred)):
	if(best_pred[i]*y_max < 1000):
		print(i)
	plt.scatter(x[i]*x_max,best_pred[i]*y_max,c='red')
plt.title("Daily-New-Cases: INDIA")
plt.show()

# [0.3173847] [-2.67588615] [2.0180911] 0