dic = {}
input_str = "viswas follows krishna,deepak,teja\nTeja follows viswas, deepak"
a = input_str.split("\n")
for i in a:
	b = i.split(" follows ")
	c = b[1].split(",")
	for j in c:
		if b[0] in dic:
			dic[b[0]].append(j)
		else:
			dic[b[0]] = [j]
			
print(dic)
	
