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
				
		
