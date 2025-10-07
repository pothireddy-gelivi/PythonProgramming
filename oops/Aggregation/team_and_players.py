class player:
    def __init__(self,pn,pa,pc,pm,pr,pw):
        self.pname=pn
        self.page=pa
        self.pcountry=pc
        self.pmatches=pm
        self.pruns=pr
        self.pwickets=pw
    
    def player_details(self):
        print(f"he is {self.pname} and he is from {self.pcountry}.he is {self.page} old player.he played around {self.pmatches} matches all over world and scored {self.pruns} runs.he is a batter but takes {self.pwickets} wickets.")
    
class team:
    def __init__(self,nop):
        self.nop=nop
        self.pl=[]
        for i in range(self.nop):
            pn=input("Enter the player name: ")
            pa=int(input("Enter the player age: "))
            pc=input("Enter the player country: ")
            pm=int(input("Enter the matches: "))
            pr=int(input("Enter the runs of player: "))
            pw=int(input("Enter the wickets of player: "))

            po=player(pn,pa,pc,pm,pr,pw)
            self.pl.append(po)
    def maxRunScorer(self):
        mrso=self.pl[0]
        for po in self.pl:
            if po.pruns>mrso.pruns:
                mrso=po
        return mrso.pname

    def maxWicketTacker(self):
        mwto=self.pl[0]
        for po in self.pl:
            if po.pwickets>mwto.pwickets:
                mwto=po
        return mwto.pname

india=team(2)
print(india.maxRunScorer())
print(india.maxWicketTacker())