class Student:
	school = "RC public School"
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

	def result(self):
		if (self.marks > 90):
			print(f"🤴Congratulation {self.name}, you are top in {self.school}.")

		elif (self.marks > 60):
			print(f"🎉Congratulation {self.name}, you are pass in {self.school}")

		elif (self.marks > 40):
			print(f"🤦‍♂️oh {self.name} , you are second in {self.school}")

		else:
			print(f"😒Oh {self.name}, you are fail in {self.school}.")


s2 = Student("Nalayak Singer", 95)
s2.result()

s1 = Student("Bawal Singh", 85)
s1.result()

s3 = Student("Rohan Dabang", 55)
s3.result()

s4 = Student("Baba tillu", 35)
s4.result()
