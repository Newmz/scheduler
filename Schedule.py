import Day as D
from Time import Time

class Schedule(object):
	#implementation:
	#list of days.
	#days are maps/dictionaries of size [NUM_SHIFTS], mapping a FirstName+LastName to a shift. a shift is a list of two Time objects, a start and an end.
	def __init__(self):
		self.week = []
		self.week.append(D.Day("Sunday"))
		self.week.append(D.Day("Monday"))
		self.week.append(D.Day("Tuesday"))
		self.week.append(D.Day("Wednesday"))
		self.week.append(D.Day("Thursday"))
		self.week.append(D.Day("Friday"))
		self.week.append(D.Day("Saturday"))
		self.finished = False

	def __str__(self):
		#the big one. print out an ASCII art schedule
		for day in self.week:
			print day
		return ""

	def addDay(self, day):
		#day is a Day object 
		if len(self.week) >= 7:
			return
		self.week += D.Day(day)
		return

	def getDay(self, day):
		return self.week[day]

	def getShift(self, day, shift):
		return self.week[day].getShift(shift)

	def fillshift(self, employee, day, shift):
		#day is the index for which day of the week
		#shift is the index for which shift of that day - e.g. self.week[day][shift] is the shift being filled
		#employee is an Employee object
		self.week[day].fillshift(shift, employee)
		return

	def clearshift(self, employee, day, shift):
		self.week[day].clearshift(shift, employee)
		#same concept as above but removing a name and opening up the shift
		return

	def full(self):
		#placeholder
		for day in self.week:
			if day.full() == False:
				return False
		return True













