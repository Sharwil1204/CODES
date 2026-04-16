class Student:
    def Set_data(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

S1 = Student()
S2 = Student()

S1.Set_data("Sharwil")
S2.Set_data("Shantanu")

S1.show()
S2.show()