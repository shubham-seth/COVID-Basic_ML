# ITALY
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("daily-cases-covid-19.csv")
data = data.values.tolist()
data_italy = []
for d in data:
	if(d[0] == "Italy" and d[2][:3]!="Jan"):
		data_italy.append(d)
del data

for d in data_italy:
	if(d[2][:3] == "Apr"):
		d.append(40)
	elif(d[2][:3] == "Mar"):
		d.append(8)
	elif(d[2][:3] == "Feb"):
		d.append(-21)
	
	i=4
	sum = 0
	while(d[2][i] != ","):
		sum *= 10
		sum += int(d[2][i])
		i += 1

	d[4] += sum

x = []
y = []
for d in data_italy:
	x.append(d[4])
	y.append(d[3])
del data_italy

x = np.array(x)
y = np.array(y)

x_max = np.max(x)
y_max = np.max(y)

x = x/np.max(x)
y = y/np.max(y)

# Training
'''
a = np.random.random([1])
b = np.random.random([1])
c = np.random.random([1])
d = np.random.random([1])

learn_rate = 1e-4
reg = 0
loss = []
d = 0
best_mse = 5
for i in range(20000):
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

a = [0.11646576] 
b = [-0.91341163] 
c = [0.27586273] 
d = 0
best_pred = ((a*x)/(x**2+b*x+c)) + d
print(a, b, c, d)
for i in range(len(y)):
	plt.scatter(x*x_max,y*y_max,c='blue')
	plt.scatter(x*x_max,best_pred*y_max,c='red')
plt.title("Daily-New-Cases: ITALY")
plt.show()

# [0.11646576] [-0.91341163] [0.27586273] 0
