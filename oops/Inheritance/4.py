class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    
    def show_person_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

    def is_adult(self):
        if self.age>=18:
            print("Adult : Yes")

class Employee(Person):
    def __init__(self, n, a,i,s):
        super().__init__(n, a)
        self.emp_id=i
        self.salary=s

    def employee_info(self):
        super().show_person_info()
        print(f"Emp-id : {self.emp_id}")
        print(f"Monthly Salary : {self.salary}")

    def annual_salary(self):
        print(f"Annual salary is {self.salary*12}")

class Manager(Employee):
    def __init__(self, n, a, i, s,d,ts):
        super().__init__(n, a, i, s)
        self.department=d
        self.team_size=ts
    def manager_details(self):
        print(f"Department : {self.department}")
        print(f"Team Size : {self.team_size}")

    def all_details(self):
        super().employee_info()
        self.manager_details()

m1 = Manager("Reddy", 25, "E123", 80000, "IT",10)
m1.show_person_info()
m1.is_adult()
m1.employee_info()
m1.annual_salary()
m1.manager_details()