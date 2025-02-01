class StudentDetails:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no  

    def get_details(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}"

    def __str__(self):  
        return self.get_details()

s = StudentDetails("Ammulu", 5474)
s1 = StudentDetails("Hgt", 32)

print(s)   
print(s1)
