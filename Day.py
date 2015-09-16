import Shift as S
from Time import Time
class Day(object):
	def __init__(self, day):
		#morning contains 2 4-12, 3 6-2, 2 7-2 shifts
		self.shifts = []
		for i in range(2):
			self.shifts.append(S.Shift(Time(4, 0, 0), Time(12, 0, 0), day))
		for i in range(3):
			self.shifts.append(S.Shift(Time(6, 0, 0), Time(14, 0, 0), day))
		for i in range(2):
			self.shifts.append(S.Shift(Time(7, 0, 0), Time(14, 0, 0), day))
		

		#afternoon contains 4 2-6, 1 2-7, 2 6-10 shifts
		

		for i in range(4):
			self.shifts.append(S.Shift(Time(14, 0, 0), Time(18, 0, 0), day))
		for i in range(2):
			self.shifts.append(S.Shift(Time(18, 0, 0), Time(22, 0, 0), day))
		self.shifts.append(S.Shift(Time(14, 0, 0), Time(19, 0, 0), day))

		self.day = day
		self.filled = False

	def __str__(self):
		output = "Day: " + self.day + '\n'
		output += "Shifts: \n"
		for i in range(len(self.shifts)):
			output += str(self.shifts[i]) + "\n"
		
		output += "\n"
		return output


	def Length(self):
		return len(self.shifts)

	def getShift(self, shift):
		return self.shifts[shift]

	def fillshift(self, shift, employee):
		# 
		self.shifts[shift].fill(employee)
		if shift == len(self.shifts):
			self.filled = True
		return

	def clearshift(self, shift, employee):
		self.shifts[shift].clear(employee)
		self.filled = False
		return

	def full(self):
		return self.filled