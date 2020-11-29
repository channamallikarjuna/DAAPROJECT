class readfiles:
	def readfile(self,filename):
		f = open(filename, "r")
		f1=f.read()
		f.close()
		#print(f1)
		return f1
