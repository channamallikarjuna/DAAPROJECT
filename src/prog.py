from readfile import readfiles as rd
from tree import tree
from readcsv import readcsv
import addsuffix as add
import re
import string
import nltk
import itertools
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
l=0
array=[]
ka=[]
def convert(lst): 
    return (lst[0].split())
def isnotchild(s,p):
	for i in p.child:
		if i.word==s:
			return False
	return True

def common_member(a, b): 
    if(a==None or b==None):
        return None
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        return a_set & b_set
    else: 
        return None 



def printcommon(p,s):
	global l,array
	if(p.word!=None):
		s=s+" "+str(p.word)
	if(len(p.child)==0):
		#print(p.word)
		return [int(p.word)]
	if(p.word!=None and p.word.isnumeric()):
		#print(p.word)
		return [int(p.word)]
	k=set()
	for i in p.child:
		k.update(printcommon(i,s))
		#print(k)
	#print(k)
	pairs=set(list(itertools.combinations(k, 2)))
	#print(pairs)
	#print(len(pairs))
	for i in pairs:
		if(len(str(array[i[0]][i[1]]))<len(s)):
			
			array[i[0]][i[1]]=s
			
			array[i[1]][i[0]]=s

	"""if(len(k)>1):
		#print("common between " + str(k) + " " +str(s))
		#if(l<len(s)):
		l=len(s)
		print("common between " + str(k) + " " +str(s))"""

	
	return k


def printcommondocment(p,s):
	global l
	if(p.word!=None):
		s=s+" "+str(p.word)
	if(len(p.child)==0):
		#print(p.word)
		return [int(p.word)]
	if(p.word!=None and p.word.isnumeric()):
		#print(p.word)
		return [int(p.word)]
	k=set()
	for i in p.child:
		k.update(printcommondocment(i,s))
		#print(k)
	#print(k)
	if(len(k)>1):
		#print("common between " + str(k) + " " +str(s))
		if(l<len(s)):
			l=len(s)
			print("common between " + str(k) + " " +str(s))

	
	return k		



def printallsuffixes(p,s):
	if(p.word!=None):
		s=s+" "+str(p.word)
	if(len(p.child)==0):
		print(s)
		return
	
	for i in p.child:

		printallsuffixes(i,s)

def printthetree(p):
	print("for "+str(p.word))
	for i in p.child:
		print(i.word)
	for i in p.child:
		printthetree(i)


def docmentsearch():
	global l1
	treeobj=tree("mallu",[])
	#print(treeobj.word)
	r=rd()
	
	mallu = r.readfile("txt1.txt")
	#mallu=mallu.lower()
	mallu=mallu.lower()

	
	ramu=r.readfile("txt2.txt")
	#ramu=ramu.lower()
	ramu=ramu.lower()
	mallu =re.sub(r'\d+' ,'', mallu)
	ramu =re.sub(r'\d+' ,'', ramu)
	mallu = mallu.strip()
	ramu = ramu.strip()
	mallu = mallu.translate(str.maketrans("","", string.punctuation))
	ramu = ramu.translate(str.maketrans("","", string.punctuation))

	stemmer= PorterStemmer()
	mall=word_tokenize(mallu)
	mallu=""
	for word in mall:
		mallu=mallu+" "+stemmer.stem(word)

	ram=word_tokenize(ramu)
	ramu=""
	for word in ram:
		ramu=ramu+" "+stemmer.stem(word)
	

	stop_words = set(stopwords.words('english'))
	
	tokens = word_tokenize(mallu)
	mallu = [i for i in tokens if not i in stop_words]
	tokens = word_tokenize(ramu)
	ramu = [i for i in tokens if not i in stop_words]
	mallu.append("1")
	ramu.append("2")
	
	root=tree(None,None)
	
	print(len(root.child))
	for i in range(len(mallu)):
		if(i>0):
			add.addtosuffix(mallu[i],root,root,mallu[i-1])
		else:
			add.addtosuffix(mallu[i],root,root,None)

	for i in range(len(ramu)):
		if(i>0):
			add.addtosuffix(ramu[i],root,root,ramu[i-1])
		else:
			add.addtosuffix(ramu[i],root,root,None)	
	
	#printthetree(root)
	#printallsuffixes(root,"")
	printcommondocment(root,"")
	#print(l)
	#print(sizeof(mallu))
def preprocess(mallu):
	mallu=mallu.lower()
	mallu =re.sub(r'\d+' ,'', mallu)
	mallu = mallu.strip()
	mallu = mallu.translate(str.maketrans("","", string.punctuation))
	stemmer= PorterStemmer()
	mall=word_tokenize(mallu)
	mallu=""
	for word in mall:
		mallu=mallu+" "+stemmer.stem(word)
	stop_words = set(stopwords.words('english'))
	
	tokens = word_tokenize(mallu)
	mallu = [i for i in tokens if not i in stop_words]
	return mallu

def tweetssearch():
	rc=readcsv()
	tweets=rc.readcsv()
	global array,ka
	for i in range(32):
		li=[]
		ki=[]
		for i in range(32):
			li.append("")
			ki.append(1)
		array.append(li)
		ka.append(ki)

	t=[]
	i=0;
	for tweet in tweets:
		k=preprocess(tweet)
		k.append(str(i))
		t.append(k)
		i=i+1
		if(i>30):
			break
	root=tree(None,None)
	#print(t)
	print(i)
	j=0;
	for mallu in t:
		print(mallu)
		for i in range(len(mallu)):
			if(i>0):
				add.addtosuffix(mallu[i],root,root,mallu[i-1])
			else:
				add.addtosuffix(mallu[i],root,root,None)
			
		j=j+1
		print(j)
		if(j>30):
			break

	#print("completede tree")
	printcommon(root,"")
	#print(l)
		




def main():
	global array,ka
	choice=input("Enter \n1.document similarity \n 2.tweets similarity" )
	if(int(choice)==1):
		docmentsearch()
	elif(int(choice)==2):
	
		tweetssearch()
		#print(array)
		for i in range(len(array)):
			for j in range(len(array[i])):
				#print(len(array[i][j]))
				ka[i][j]=len(array[i][j])
		print(ka)
	else:
		print("sorry choose correct option")

	




	




