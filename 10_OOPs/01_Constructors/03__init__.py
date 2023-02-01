class student:
    def __init__(self,course):
        self.name=input("Enter Name:")
        self.course=course
        self.institute="quastech"
        self.fees = int(input("Enter fees:"))
    def display(self):
        print(self.name," ",self.course," ",self.institute)
        print("fees: ",self.fees)

#create Object
s1=student("python")
s1.display()
