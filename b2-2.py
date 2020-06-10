def checkIfPalindrome(str):
	str=str.lower()
	newstr=''
	for i in range(0,len(str)):
		if str[i].isalpha() == True:
			newstr=newstr+str[i]
	str=newstr
	revstr=str[::-1]
	if revstr==str:
		return True
	return False
  
# main function 
#str = "kayak"
#answer = checkIfPalindrome(str) 
  
#if (answer): 
#    print("Yes") 
#else: 
#    print("No") 