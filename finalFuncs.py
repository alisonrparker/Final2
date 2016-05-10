class User:
	
	def __init__(self, district, income, persons):
		self.district = district
		self.income = income
		self.persons = persons

class Info:	
	
	def __init__(self):
		#neighborhoods with $800 subsidy
		self.subsidies = ['SoMA', 'Bayview', 'Dogpatch', "South Beach", "Yerba Buena"]
		#median income by num in household
		self.medianI = {1:31860, 2:31860, 3:40180, 4:48500, 5:56820, 6: 65140, 7:73460, 8:81780}
		#neighborhoods and their solar generating potential in kWh per meter squared
		self.places = {'Sunset':4.12,'Richmond': 4.12, 'Marina':4.59, 'North Beach':4.58, 'Parkside':4.12, 'Hayes Valley':4.61, 'SoMa':4.82, 'Midtown Terrace':4.12, 'Bayview':4.44, 'Portola':4.5, 'Visitacion Valley':4.79, 'Castro':4.41, 'Mission':4.58, 'South San Francisco': 5.04, 'Lake Shore':4.15,'South Beach':4.64, 'Dogpatch':4.65, 'Alamo Square/Western Addition':3.79, 'Sunnyside':4.23, 'Union Square':4.30, 'Financial District':4.47, 'Yerba Buena':4.45, 'Embarcadero':4.83, 'Nopa':4.28}
		#average annual kWh consumed per capita by neighborhood
		self.electricity = {'Sunset':1634, 'Richmond': 1945, 'Marina': 2314, 'North Beach':1634, 'Parkside':1634, 'Hayes Valley':1391, 'SoMa':2993, 'Midtown Terrace':2314, 'Bayview':1391, 'Portola':1391, 'Visitacion Valley':1391, 'Castro':2314, 'Mission':1391, 'South San Francisco': 1391, 'Lake Shore':1634, 'South Beach':1945, 'Dogpatch':1945, 'Alamo Square/Western Addition':1945, 'Sunnyside':1391, 'Union Square':1945, 'Financial District':1634, 'Yerba Buena':1945, 'Embarcadero':1391, 'Nopa':1945}
		


def totalCost(info, user):
	
	total = 12000
	#deduct any automatic subsidies
	for i in range (len(info.subsidies)):
		if user.district == info.subsidies[i]:
			total = total - 800	
	
	#deduct any income based subsidies
	numPeople = user.persons
	medianIncome = info.medianI[numPeople] 
	if user.income < medianIncome:
		total = total - 7000
	
	return total
				

def conditions(cost, info, user):
	
	home = user.district
	family = user.persons
	solar = info.places[home]
	utility = info.electricity[home]
	average = 4.46
	if solar >= average: #for neighborhoods in the upper half of solar generating potential
		if cost <= (((utility*family)*(.1534))*10): #if the cost of install is lower than the average family utility cost over 10 years
			ranking = 'an excellent'
		if cost > (((utility*family)*(.1534))*10): #if the cost of install is higher than the average family utility cost over 10 years
			ranking = 'a below average'
	if solar < average: #for neighborhoods in the lower half of solar generating potential
		if cost <= (((utility*family)*(.1534))*10):
			ranking = 'an average'
		if cost > (((utility*family)*(.1534))*10):
			ranking = 'a poor' 
		
	return ranking
