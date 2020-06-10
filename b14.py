def specialDivisors():
	result = set()
	for i in range(2000,3207):
		if(i%7==0) and (i%5!=0):
			result.add(i)
	return(result)