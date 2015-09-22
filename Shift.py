import Time as T
class Shift(object):
	def __init__(self, t1, t2, day):
		self.start = t1
		self.end = t2
		self.length = t2.Length(t1)
		self.filled = False
		self.worker = "no worker yet" #wil contain Employee object
		self.d = day

	def __str__(self):
		temp = "Start: "
		temp += str(self.start) + " "
		temp += "End: " + str(self.end) + " Employee: " + str(self.worker) + " Length: " + str(self.length)
		return temp

	def getDay(self):
		return self.d

	def fill(self, employee):
		#placeholder
		employee.addshift(self)
		self.worker = employee
		self.filled = True
		return

	def clear(self, employee):
		employee.clrshift()
		self.worker = "no worker yet"
		self.filled = False
		return

	def full(self):
		return self.filled

	def concurrent(self, other):
		if self.d != other.d:
			#if the shifts are not on the same day, they are not concurrent.
			return False
		else:
			if self.d == other.d and other.length > 4:
				#if they ARE on the same day, but one is longer than four hours, the employee can't take another shift that day anyway, so return false
				return True
			elif self.start >= other.start and self.start <= other.end:
				return True
			elif self.end >= other.start and self.end <= other.end:
				return True
			elif self.start <= other.start and self.end >= other.end:
				return True
			else:
				return False