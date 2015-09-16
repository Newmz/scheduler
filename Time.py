class Time(object):
	def __init__(self, h, m, s):\
		#little time class (displays and records hours, minutes, seconds)
		self.hour = h
		self.minute = m
		self.second = s
		if self.hour < 12:
			self.ToD = "am"
		else:
			self.ToD = "pm"

	def Length(self, other):
		#return length of shift in hours(float)
		t = other.second - self.second
		t /= 60
		t += other.minute - self.minute
		t /= 60
		t += other.hour - self.hour
		if t < 0:
			t = -1 * t
		return t

	def __str__(self):
		if self.hour > 12:
			temp = ""
			temp += str(self.hour - 12) + ":"
			if self.minute < 10:
				temp += "0" + str(self.minute) + ":"
			else:
				temp += str(self.minute) + ":"
			if self.second < 10:
				temp += "0" + str(self.second)
			else:
				temp += str(self.second)
			temp += "pm"
		elif self.hour == 12:
			temp = ""
			temp += str(self.hour) + ":"
			if self.minute < 10:
				temp += "0" + str(self.minute) + ":"
			else:
				temp += str(self.minute) + ":"
			if self.second < 10:
				temp += "0" + str(self.second)
			else:
				temp += str(self.second)
			temp += "pm"
		elif self.hour == 0 or self.hour == 24:
			temp = ""
			temp += str(12) + ":"
			if self.minute < 10:
				temp += "0" + str(self.minute) + ":"
			else:
				temp += str(self.minute) + ":"
			if self.second < 10:
				temp += "0" + str(self.second)
			else:
				temp += str(self.second)
			temp += "am"
		else:
			temp = ""
			temp += str(self.hour) + ":"
			if self.minute < 10:
				temp += "0" + str(self.minute) + ":"
			else:
				temp += str(self.minute) + ":"
			if self.second < 10:
				temp += "0" + str(self.second)
			else:
				temp += str(self.second)
			temp += "am"
		return temp