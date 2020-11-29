class tree:
	def __init__(self,s,array):
		self.word=s
		self.end=0;
		if array:
			self.child=array
		else:
			self.child=[]
