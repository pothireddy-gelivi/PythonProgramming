def singleTon(clsarg):
    L=[]
    def inner():
        if len(L)==0:
            L.append(clsarg())
        return L[0]
    return inner

@singleTon
class multiflex():
    def __init__(self):
        self.tickets=300
