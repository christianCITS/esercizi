'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

For example:
Test 	Result

print(is_valid_parenthesis("()"))

	

True

print(is_valid_parenthesis("(]"))

	

False'''





"""from collections import Counter


l=[1,2,3,4]
c=Counter(l)

for i in enumerate(l):
    print(i)

for i in c:
    print (i)"""




'''from abc import ABC, abstractmethod
from typing import Any

class AbcAnimal(ABC):
    @abstractmethod
    def verso(self):
        pass



class Cane(AbcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome:str=nome

    def verso(self):
        print(f"miao")

class Gatto(AbcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome:str=nome

    def verso(self):
        print(f"BAU")


class Coccodrillo(AbcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome:str=nome

    def verso(self):
        print(f"raaaar")


    
cane1:Cane=Cane("pluto")

cane1.verso()
gatto1:Gatto=Gatto("silvestro")
coccodrillo1:Coccodrillo=Coccodrillo("gionny")
gatto1.verso()
coccodrillo1.verso()

    
l_animali:list[AbcAnimal]=[cane1,gatto1,coccodrillo1]

for i in l_animali:
    i.verso()






a:dict[str,str]= {
    "key1":"val1",
    "key2":"val2"
                  }'''

import unittest



class Calculations:
    def __init(self,a:float,b:float)-> None:
        self.a:float=a
        self.b:float=b



    
    def get_sum(self):
        return self.a+self.b
    
    def get_difference(self):
        return self.a-self.b
    
    def get_product(self):
        return self.a*self.b
    
    def get_quotient(self):
        return  self.a/self.b
