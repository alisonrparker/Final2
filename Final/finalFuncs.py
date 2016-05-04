class User:
	def __init__(self, district, income, persons):
		self.district = district
		self.income = income
		self.persons = persons

class Cost:	
	def __init__(self):
		self.subsidies = ['SoMA', 'Bayview', 'Dogpatch', "South Beach", "Yerba Buena"]
		self.medianI = {1:31860, 2:31860, 3:40180, 4:48500, 5:56820, 6: 65140, 7:73460, 8:81780}
		


def totalCost(cost, user):
	totalCost = 12000
	for i in range (len(cost.subsidies)):
		if user.district == cost.subsidies[i]:
			totalCost = totalCost - 800		
	
	numPeople = user.persons
	print numPeople
	medianIncome = cost.medianI[numPeople] #KeyError
	if user.income < medianIncome:
		totalCost = totalCost - 7000
	
	#for key, value in Cost.medianI:
	#	if key == User.persons:
			
	#		if int(User.income) < int(key.value):
				
	return totalCost
				
places = {'Richmond': 4.12, 'Marina':4.59, 'North Beach':4.58, 'Parkside':4.12, 'Hayes Valley':4.61, 'SoMa':4.82, 'Midtown Terrace':4.12, 'Bayview':4.44, 'Portola':4.5, 'Visitacian Valley':4.79, 'Castro':4.41, 'Mission':4.58, 'South San Francisco': 5.04, 'Lake Shore':4.15, 'San Mateo':4.95, 'South Beach':4.64, 'Dogpatch':4.65, 'Alamo Square/Western Addition':3.79, 'Sunnyside':4.23, 'Union Square':4.30, 'Financial District':4.47, 'Yerba Buena':4.45, 'Embarcadero':4.83, 'Nopa':4.28}		
