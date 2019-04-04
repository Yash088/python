# with self coz making constructor
class C():
        def add(self,a,b):
                return a+b
        def sub(self,a,b):
                return a-b
        def mul(self,a,b):
                return a*b
        def divi(self,a,b):
                return a/b

c=C().add(2,3)
d=C().sub(6,3)
print(c)
print(d)

