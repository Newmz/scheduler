#Main File
import Schedule as s
import Employee as e

#Parse Input
def parse(filename):
	filename += '.txt'
	f = open(filename)
	temp = []
	Employees = []
	f.readline() #get rid of header
	for line in f:
		temp.append(line.strip().split())
		
		#index 0: first name
		#index 1: last name
		#index 2: min hours
		#index 3: max hours
		#index 4: primary shift time
		#index 5: secondary shift time
		#index 6: monday off?
		#index 7: tuesday off?
		#.....
		#index 12: sunday off?
	return temp
	

#def fill schedule(schedule, employees, day, shift):
#	check if the schedule is full:
# 	 if it is, return true
#   if it is not, iterate through the list of employees to find one that can work the shift.
#		if an employee can work a shift, place the employee in the shift and call fill schedule again on the next shift.
#	   if the shift is the last of the day move to the next day
#		if that returns false, remove the last employee from the shift and continue to iterate through the employees
#  if at the end of the list of employees the shift is not filled, return false and remove the previously placed employee
#	
def valid_shift(shift, employee):
	#
	if employee.valid(shift) and shift.full() == False:
		return True
	return False

def fill(Schedule, Employees, day, shift, debug):
	debug += "  "
	
	if Schedule.full() or day >= 7:
		return True
	else:
		for employee in Employees:
			if valid_shift( Schedule.getShift(day, shift), employee):
				#put employee on shift.
				Schedule.fillshift(employee, day, shift)
				#move to the next employee and the next shift and call fill again.
				if (shift + 1) >= 14: #len(Schedule.getDay(day).):
					if (fill(Schedule, Employees, day+1, 0, debug)):
						return True
					else:
						Schedule.clearshift(employee, day, shift)
						#remove employee from shift, next employee
						continue
				else:
					if (fill(Schedule, Employees, day, shift+1, debug)):
						return True
					else:
						Schedule.clearshift(employee, day, shift)
						#remove employee from shift, next employee
						continue
			else:
				continue
		return False


#tests and what not

sched = s.Schedule()

time = s.Time(20, 17, 20)
temp1 = parse("Text Sample")
emps = []
for i in range(len(temp1)):
		emps.append(e.Employee(temp1[i]))
		


fill(sched, emps, 0, 0, "--")
print sched
for e in emps:
	print e.info()



