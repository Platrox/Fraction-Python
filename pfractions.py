class Fraction:
    
    def __init__(self,n,d):
        if n*d>=0:
            n, d = abs(n), abs(d)
        elif d<0:
            n, d = -1*n, -1*d
        self.setNum(n)
        self.setDenom(d)
        
    def setNum(self,n):
        assert type(n)==int, "numérateur non entier"
        self.numerateur = n
        
    def setDenom(self,d):
        assert type(d)==int, "dénominateur non entier"
        assert d!=0, "division par zéro"
        self.denominateur = d
        
    def getNum(self):
        return self.numerateur
    
    def getDenom(self):
        return self.denominateur
    
    def __str__(self):
        fr = str(self.getNum())
        if self.getDenom()!=1 and self.getNum()!=0:
            fr += "/"+str(self.getDenom())
        return fr
    
    def PGCD(a,b):
        if b==0:
            return a
        else:
            return Fraction.PGCD(b,a%b)
        
    def simplifier(self):
        n, d = self.getNum(), self.getDenom()
        p = Fraction.PGCD(n,d)
        self.setNum(n//p)
        self.setDenom(d//p)
        
    
    def oppose(self):
        n, d = self.getNum(), self.getDenom()
        res = Fraction(-n,d)
        return res
        
    def inverse(self):
        n, d = self.getNum(), self.getDenom()
        res = Fraction(d,n)
        return res
        
    def __eq__(self,f):
        a, b, c, d = self.getNum(), self.getDenom(), f.getNum(), f.getDenom()
        return a*d==b*c
        
    def __add__(self, f):
        a, b, c, d = self.getNum(), self.getDenom(), f.getNum(), f.getDenom()
        res = Fraction(a*d+c*b,b*d)
        res.simplifier()
        return res
    
    def __mul__(self, f):
        a, b, c, d = self.getNum(), self.getDenom(), f.getNum(), f.getDenom()
        res = Fraction(a*c,b*d)
        res.simplifier()
        return res
    
    def __sub__(self, f):
        a, b, c, d = self.getNum(), self.getDenom(), f.getNum(), f.getDenom()
        res = Fraction(a*d-c*b,b*d)
        res.simplifier()
        return res
        
    def __truediv__(self, f):
        res = self*f.inverse()
        res.simplifier()
        return res
    
    def __pow__(self, exp):
        a, b = self.getNum(), self.getDenom()
        res = Fraction(a**exp,b**exp)
        return res
    
    def lire(expr):
        pass
        
    def evaluer(expr):
        chiffres = "0123456789"
        signes = "-+"
        operateurs = "-+*/"
        num,nb = False,""
        nbr = [None,None]
        fractions = []
        operations = []
        for c in expr:
            if c in chiffres and num:
                nb += c
            elif c in chiffres:
                num = True
                nb += c
            elif num and (c in operateurs):
                num = False
                if c=="/" and nbr[0] is None:
                    nbr[0]=int(nb)
                    num=False
                    c = None
                    nb=""
                elif c=="/":
                    if nbr[1] is None:
                        nbr[1]=int(nb)
                        fractions.append(Fraction(nbr[0],nbr[1]))
                        nbr=[None,None]
                        num=False
                        nb=""
                    else:
                        operations.append(c)
                elif nbr[0] is None:
                    nbr[0]=int(nb)
                    nbr[1]=1
                    fractions.append(Fraction(nbr[0],nbr[1]))
                    nbr=[None,None]
                    nb=""
                else:
                    nbr[1]=int(nb)
                    fractions.append(Fraction(nbr[0],nbr[1]))
                    nbr=[None,None]
                    nb=""
                if c is not None: operations.append(c)
            elif c in operateurs:
                if c in signes:
                    num=True
                    nb += c
                else:
                    raise TypeError("expression mal formée")
        if num and nbr[0] is None:
            nbr[0]=int(nb)
            nbr[1]=1
            fractions.append(Fraction(nbr[0],nbr[1]))
        elif num and nbr[1] is None:
            nbr[1]=int(nb)
            fractions.append(Fraction(nbr[0],nbr[1]))
        f = None
        for op in operations:
            if f is None : 
                f1 = fractions.pop(0)
                f = "ok"
            f2 = fractions.pop(0)
            if op=="+":
                f1 = f1+f2
            elif op=="-":
                f1 = f1-f2
            elif op=="*":
                f1 = f1*f2
            elif op=="/":
                f1 = f1/f2
        return f1
'''
__________.__          __                       
\______   \  | _____ _/  |________  _______  ___
 |     ___/  | \__  \\   __\_  __ \/  _ \  \/  /
 |    |   |  |__/ __ \|  |  |  | \(  <_> >    < 
 |____|   |____(____  /__|  |__|   \____/__/\_ \
                    \/                        \/
 '''
