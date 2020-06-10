intext="we shall not flag or fail we shall go on to the end we shall fight in France we shall fight on the seas and oceans we shall fight with growing confidence and growing strength in the air we shall defend our island whatever the cost may be we shall fight on the beaches we shall fight on the landing grounds we shall fight in the fields and in the streets we shall fight in the hills we shall never surrender"
count={}
new_intext = intext.lower()
words = new_intext.split()
for word in words:
	if word in count:
		count[word] = count[word] + 1
	else:
		count[word] = 1
print(count)