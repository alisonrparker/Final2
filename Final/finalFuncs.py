class User:
	def __init__(self, District, Income, Persons):
		self.district = District
		self.income = Income
		self.persons = Persons

class Cost:	
	def __init__(self):
		self.subsidies = ['SoMA', 'Bayview', 'Dogpatch', "South Beach", "Yerba Buena"]
		self.medianI = {1:31860, 2:31860, 3:40180, 4:48500, 5:56820, 6: 65140, 7:73460, 8:81780}
		


def totalCost(Cost, User):
	totalCost = 12000
	for i in range (len(Cost.subsidies)):
		if User.district == Cost.subsidies[i]:
			totalCost = totalCost - 800		
	
	numPeople = User.persons
	#medianIncome = Cost.medianI #something is wrong
	if User.income < medianIncome:
		totalCost = totalCost - 7000
	
	#for key, value in Cost.medianI:
	#	if key == User.persons:
			
	#		if int(User.income) < int(key.value):
				
	return totalCost
				
			
		