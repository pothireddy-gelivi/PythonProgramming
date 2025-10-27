class Father:
    def __init__(self,fn,fa,fo,fh):
        self.fname=fn
        self.fage=fa
        self.foccupation=fo
        self.fhobby=fh
    def show_father_info(self):
        print(f"Father Name : {self.fname}")
        print(f"Father Age : {self.fage}")
        print(f"Father Occuation : {self.foccupation}")
    
    def father_hobby(self):
        print(f"Father Hobby : {self.fhobby}")
class Mother():
    def __init__(self,mn,ma,mo,mh):
        self.mname=mn
        self.mage=ma
        self.moccupation=mo
        self.mhobby=mh

    def show_mother_info(self):
        print(f"Mother Name : {self.mname}")
        print(f"Mother Age : {self.mage}")
        print(f"Mother Occuation : {self.moccupation}")

    def mother_hobby(self):
        print(f"Mother Hobby : {self.mhobby}")
        

class Child(Father,Mother):
    def __init__(self,fn,fa,fo,fh,mn,ma,mo,mh,cn,ca,cs,ch):
        Father.__init__(self,fn,fa,fo,fh)
        Mother.__init__(self,mn,ma,mo,mh)
        self.cname=cn
        self.cage=ca
        self.cschool=cs
        self.chobby=ch
    def child_info(self):
        super().show_father_info()
        super().father_hobby()
        super().show_mother_info()
        super().mother_hobby()
        print(f"Name : {self.cname}")
        print(f"Age : {self.cage}")
        print(f"school : {self.cschool}")
    def child_hobby(self):
        print(f"Child Hobby : {self.chobby}")

student1=Child("Padmanabha Reddy",52,"Farming","Gardening","Mamatha",48,"House-Wife","Watching tv","Pothireddy",23,"BSR MPL HIGH School","Coding")
student1.child_info()
student1.child_hobby()
