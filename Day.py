import Shift as S
from Time import Time
class Day(object):
	def __init__(self, day):
		#Day has a list of shifts, an hour total for the day (total hours worked), and a bool saying whether the day is fully
		#scheduled or not.
		#The list inside the class object behaves very much like a stack in terms of how it is used.
		self.shifts = []
		self.hourtotal = 0
		#as I progress through the project these shifts will become dynamic.
		for i in range(2):
			self.shifts.append(S.Shift(Time(4, 0, 0), Time(12, 0, 0), day))
			self.hourtotal += self.shifts[len(self.shifts)-1].length
		for i in range(3):
			self.shifts.append(S.Shift(Time(6, 0, 0), Time(14, 0, 0), day))
			self.hourtotal += self.shifts[len(self.shifts)-1].length
		for i in range(2):
			self.shifts.append(S.Shift(Time(7, 0, 0), Time(14, 0, 0), day))
			self.hourtotal += self.shifts[len(self.shifts)-1].length
		for i in range(4):
			self.shifts.append(S.Shift(Time(14, 0, 0), Time(18, 0, 0), day))
			self.hourtotal += self.shifts[len(self.shifts)-1].length
		for i in range(2):
			self.shifts.append(S.Shift(Time(18, 0, 0), Time(22, 0, 0), day))
			self.hourtotal += self.shifts[len(self.shifts)-1].length
		self.shifts.append(S.Shift(Time(14, 0, 0), Time(19, 0, 0), day))
		self.hourtotal += self.shifts[len(self.shifts)-1].length
		print self.hourtotal
		#this day is a string for the Name of the day - i.e. 'Monday'
		self.day = day
		self.filled = False

	def __str__(self):
		#output the day of the week and each shift. Printing the shift shows it's start, end, length, and employee.
		output = "Day: " + self.day + '\n'
		output += "Shifts: \n"
		for i in range(len(self.shifts)):
			output += str(self.shifts[i]) + "\n"
		
		output += "\n"
		return output


	def Length(self):
		#returns number of shifts in the day. Useful for iterating when the implementation is no longer static.
		return len(self.shifts)

	def getShift(self, shift):
		#accessor for individual shifts in the day
		return self.shifts[shift]

	def fillshift(self, shift, employee):
		self.shifts[shift].fill(employee)
		#because shifts are filled from the front of the list to the back, this check will see whether or not the 
		#day is now fully scheduled simply by checking if this shift is the last in the list.
		#this check is constant time, and allows us to avoid writing a computationally expensive full() function to individually check each shift.
		if shift == len(self.shifts):
			self.filled = True
		return

	def clearshift(self, shift, employee):
		#this removes the employee from the last shift (i.e. the most recent addition).
		self.shifts[shift].clear(employee)
		self.filled = False
		return

	def full(self):
		#simple boolean check to see if day is filled
		return self.filled