class Employee:
    def _init_(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name: {self.name}, Employee ID: {self.emp_id}")

class Manager(Employee):
    def _init_(self, name, emp_id, department):
        Employee._init_(name, emp_id)
        self.department = department

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} department.")

class Developer(Employee):
    def _init_(self, name, emp_id, language):
        Employee._init_(name, emp_id)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")


d1=Developer("pothireddy",102,"python")
d1.code()