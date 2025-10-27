class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.width=b
        self.area=l*b
    
    def __gt__(self,other):
        return self.area > other.area
    
    def __lt__(self,other):
        return self.area< other.area
        
    def __eq__(self,other):
        return self.area == other.area

r1=Rectangle(12,10)
r2=Rectangle(13,10)
print(r1<r2)
    
        