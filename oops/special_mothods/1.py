class Employee:
    company_name='PSP'
    company_location='Bangalore'
    emp_count=0

    def __init__(self,en,es,ej,ex):
        self.ename=en
        self.esal=es
        self.ejob=ej
        self.eexp=ex
        Employee.emp_count+=1

    def __del__(self):
        Employee.emp_count-=1

reddy=Employee("pothireddy",10000,"Web developer",1)
charan=Employee("charan",15000,"fullstackdeveloper",2)
sahoo=Employee("sahoo",11200,"python developer",3)

print(sahoo.emp_count)
del charan
print(sahoo.emp_count)
