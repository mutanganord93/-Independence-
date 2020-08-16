class compareTo:
	def CompareTo(self,y1,y2):
		month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
		year1 = y1.split()
		year2 = y2.split()
		m1 = month[year1[1]]
		m2 = month[year2[1]]
		if int(year1[2]) > int(year2[2]):
			return 1
		elif int(year1[2]) < int(year2[2]):
			return -1
		elif m1 > m2:
			return 1
		elif m1 < m2:
			return -1
		elif int(year1[0]) > int(year2[0]):
			return 1
		elif int(year1[0]) < int(year2[0]):
			return -1
		return 0