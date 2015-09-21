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