fruits=['apple','orange','peach','banana']
amount=[5,8,4,6]
cost=[1.0,1.5,2.30,1.80]
header = ['Fruit','Amount','Cost per item','Total Cost per Fruit']
print('{:20}{:20}{:20}{:30}'.format(*header)+'\n')
for row in zip(fruits, amount, cost, (cost[i]*amount[i] for i in range(len(cost)))):
	print('{:20}{:6}{:27}{:27}'.format(*row))
print('\n'+'Total Cost:',sum(cost[i]*amount[i] for i in range(len(cost))))