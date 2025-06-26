class PA: 
    def __init__(self,marks):
        self.marks = marks
    def percentage(self):
        return (self.marks /20) * 100
    def average(self,marks):
        # Assuming the total marks for PA is 200 (20 marks per subject for 10 subjects)
        return (marks / 200) * 100

class Term:
    def __init__(self,marks):
        self.marks = marks
    def percentage(self):
        return (self.marks / 80) * 100
    def average(self,marks):
        return (marks / 800) * 100


subjects = ["English", "Bengali", "Maths", "Physics", "History", "Civics", "Geography", "Chemistry", "Biology", "Economics"]


a=input("Is this a PA or Term? ").lower()
if a == "pa":
    total = 0
    print("Enter the marks for the 10 subjects: ")
    for subject in subjects:
            marks = int(input(f"Enter the marks for {subject}: "))
            p = PA(marks)
            print(f"Percentage for subject {subject} is: ", p.percentage())
            total += marks
    print(f"Your grand total average is:{p.average(total)}")
elif a == "term":
    total = 0
    print("Enter the marks for the 10 subjects: ")
    for subject in subjects:
            marks = int(input(f"Enter the marks for {subject}: "))
            t = Term(marks)
            print(f"Percentage for subject {subject} is: ", t.percentage())
            total += marks
    print(f"Your grand total average is:{t.average(total)}")
else:
    print("Invalid input")
    exit()
# This code calculates the percentage of marks obtained in a PA or Term exam.