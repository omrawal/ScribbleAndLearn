import math
import random
class Problem:
    num=[0,1,2,3,4,5,6,7,8,9]
    opt=['+','-','*','/']   
    def __init__(self):
        self.level=0
    def check_int(self,a):
        if(eval(a)%2==0 and eval(a)>=0 and eval(a)<10):
            return False
        else:
            return True
    def createprob(self):
        exp=[]
        if(self.level<5):
            exp.append(str(random.choice(self.num)))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            a=''.join(exp)
            return a
        elif(self.level<10):
            exp.append(str(random.choice(self.num)))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            a=''.join(exp)
            return a
        elif(self.level<15):
            exp.append(str(random.choice(self.num)))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            exp.append(random.choice(self.opt))
            exp.append(str(random.choice(self.num[1:])))
            a=''.join(exp)
            return a
    def get_ans(self):
        go=True
        while(go):
            a=self.createprob()
            go=self.check_int(a)
        ans=eval(a)
        return a,ans