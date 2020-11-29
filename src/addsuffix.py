from tree import tree
def isnotchild(s,p):
	for i in p.child:
		if i.word==s:
			return False
	return True
def addtosuffix(s,p,root,b):
	#print(s)
	if(len(p.child)==0):
		p.child.append(tree(s,None))
		p.end=0
		return
	
	k=False
	for i in p.child:
		root.end=1
		if(s==i.word):
			if(p.end==1):
				i.end=1
			k=True
			addtosuffix(s,i,root,b)
		elif(len(i.child)==0):
			
			#i.end=0
			i.child.append(tree(s,None))
		elif i.end==1 and i.word==b:
			#print(" i am "+str(i.word)+"for "+str(s))

			#i.end=0
			addtosuffix(s,i,root,b)
			if isnotchild(s,i) :
				#print("i  am adding ")
				i.child.append(tree(s,None))
			
		else:
			i.end=0
			addtosuffix(s,i,root,b)
	if k==False and p==root:
		p.child.append(tree(s,None))