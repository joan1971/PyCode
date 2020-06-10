def FML(mylist):
	first=mylist[0]
	last=[-1]
	if len(mylist)>2:
		middle=mylist[int(len(mylist) / 2)]
	elif len(mylist)==2:
		middle=mylist[0]
	elif len(mylist)==1:
		last=mylist[0]
		middle=mylist[0]
	return(first,middle,last)
