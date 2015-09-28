class Employee(object):
	#Organization:
	#	NameF - first name
	#	NameL - last name
	#	HoursMin - minimum hours per week
	#	HoursMax - maximum hours per week
	#	Shift1 - primary shift
	#	Shift2 - secondary shift
	#	DaysOff - list of 7 booleans. True means that the day is taken off. False means it can be scheduled.
	#	DaysOn - list of shifts 
	def __init__(self, data):
		#if len(data) != 13:
			#exit program/throw exception
		#	print "idk"
		#else:
		self.NameF = data[0]
		self.NameL = data[1]
		self.HoursMin = int(data[2])
		self.HoursMax = int(data[3])
		self.Shift1 = data[4]
		self.Shift2 = data[5]
		self.DaysOff = [data[6], data[7], data[8], data[9], data[10], data[11], data[12]]
		self.shifts = []
		self.scheduled_hours = 0
		#self.DaysOn = []
		#for i in range(len(DaysOff)):
		#if DaysOff[i] != True:

	def __str__(self):
		return self.NameF + self.NameL

	def info(self):
		totalstring = ""
		temp = self.NameF + " " + self.NameL
		totalstring += "Employee: "
		totalstring += temp
		totalstring += '\n'
		temp = str(self.HoursMin)
		temp += " Max Hours: "
		temp += str(self.HoursMax)
		totalstring += "Min Hours: "
		totalstring += temp
		totalstring += '\n'
		temp = "Preferred Shift: "
		temp += self.Shift1
		temp += " Secondary Shift: "
		temp += self.Shift2
		totalstring += temp
		#totalstring += "Preferred Shift: " + self.Shift1, "Secondary Shift: " + self.Shift2
		totalstring += '\n'
		daysoff = "Days Taken Off:"
		for i in range(len(self.DaysOff)):
			if self.DaysOff[i] == "y":
				if i == 0:
					daysoff += " Monday"
				elif i == 1:
					daysoff += " Tuesday"
				elif i == 2:
					daysoff += " Wednesday"
				elif i == 3:
					daysoff += " Thursday"
				elif i == 4:
					daysoff += " Friday"
				elif i == 5:
					daysoff += " Saturday"
				elif i == 6:
					daysoff += " Sunday"
				else:
					print " error in days taken off. please check input"
					continue
			else:
				continue
		totalstring += daysoff
		totalstring += "\n"
		totalstring += "Scheduled Hours: " + str(self.scheduled_hours) + "\n"
		totalstring += "Scheduled Shifts:\n"
		for shift in self.shifts:
			totalstring += "\t" + str(shift) + '\n'
		totalstring += '\n'
		return totalstring

	def addshift(self, shift):
		#placeholder - to be added later
		self.shifts.append(shift)
		self.scheduled_hours += shift.length
		return

	def clrshift(self):
		#any shift being removed will be the last shift added 
		#(because the function is only being used in context of a modified depth-first search).
		self.scheduled_hours -= self.shifts[len(self.shifts)-1].length
		self.shifts.pop()
		return

	def name(self):
		return self.NameF + self.NameL

	def valid(self, shift):
		#if times don't conflict, they didn't take the day off, and their hour limit has not been reached
		#placeholder
		if ((self.scheduled_hours + shift.length) > self.HoursMax):
			return False
		else:
			for scheduled_shift in self.shifts:
				#this check also takes care of if they have been scheduled already on that day
				if shift.concurrent(scheduled_shift):
					return False
			#if in days off
			if shift.getDay() == "Monday" and self.DaysOff[0] == "y":
				return False
			elif shift.getDay() == "Tuesday" and self.DaysOff[1] == "y":
				return False
			elif shift.getDay() == "Wednesday" and self.DaysOff[2] == "y":
				return False
			elif shift.getDay() == "Thursday" and self.DaysOff[3] == "y":
				return False
			elif shift.getDay() == "Friday" and self.DaysOff[4] == "y":
				return False
			elif shift.getDay() == "Saturday" and self.DaysOff[5] == "y":
				return False
			elif shift.getDay() == "Sunday" and self.DaysOff[6] == "y":
				return False	
		return True





