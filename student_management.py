
students = []
def add_student():
	name = input("Entr your name: ")
	roll = input("Enter your roll nunber:")
	marks = int(input("Enter your marks: "))


	student = {
	"name": name,
	"roll": roll,
	"marks": marks
	}

	students.append(student)
	print("Student added successfully")


def view_student():
	if len(students) == 0:
		print("No student found")
	else:
		for s in students:
			print(s)

def search_student():
	roll = input("Enter roll number to seach: ")
	for s in students: 
		if s["roll"] == roll:
			print(s)
			return

	print("Student not found")

def check_student():
	roll = input("Enter roll number:")


	for s in students:
		if s["roll"] ==roll:
			marks = s["marks"]


			if marks>=90:
				grade = "A"
			elif marks>=75:
				grade = "B"
			elif marks>=50:
				grade = "C"
			else: 
				grade = "Fail"

			print("Name:",s["name"])
			print("Marks:",marks)
			print("Grade:" , grade)
			return
		print("Student not found")

while True:
	print("/n---Student management System---")
	print("1. Add student")
	print("2. view student")
	print("3. search student")
	print("4. check student")
	print("5. Exit")

	choice = input("Enter choice: ")

	if choice=="1":
		add_student()
	elif choice== "2":
		view_student()
	elif choice== "3":
		search_student()
	elif choice =="4":
		check_student()
	elif choice == "5":
		print("Thank you")
		break 
	else:
		print("Invalid choice")


