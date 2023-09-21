class User:
    def log_in(self):
        print("User.log_in() called.")
        self.logged_in = True

class Student(User):
    def log_in(self):
        print("Student.log_in() called.")
        super().log_in()
        self.in_class = True

oneil = Student()
oneil.log_in()