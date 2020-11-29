import csv
class readcsv:
	def readcsv(self):
		tweets=[]
		with open('tweets.csv', newline='') as csvfile:
			data = csv.DictReader(csvfile)
			
			for row in data:
				#print(row['text'])
				#tweets.append(row['Tweet Content'])
				tweets.append(row['text'])
			return tweets
