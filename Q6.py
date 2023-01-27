class student:

    def _init_(self,input):
        self.id = input
        print("Id: ",self.id)

    def student_class(self,input):
        self.student_class = input
        print("Class: ", self.student_class)

    def student_name(self,input):
        self.student_name = input
        print("Name: ", self.student_name)

a = student(12)
a.student_name("John")
a.student_class("10A")
