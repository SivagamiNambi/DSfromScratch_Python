# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 10:17:32 2017

@author: sivagami
"""
#Sorting
x=[1,-59,0,2,6]
y=sorted(x)
y
x.sort(key=abs,reverse=True)

#list Comprehension
x={x:x*x for x in range(5)if x%2 == 0}
y=[x1 for x1 in range(10)if x1%2==0]


#Random
import random
x=[random.random() for _ in range(4)]
random.seed(10)
random.random()


random.randrange(10)
random.randrange(3,6)
one2ten=range(10)
random.shuffle(one2ten)
#choose one
random.choice(["Padma","Sai","Nambi"])

#without replacement
random.sample(range(60),6)

#regular Expression
import re
re.match('a',"apple")
re.search("a","c0t")
re.split("b","carbs")
re.sub("[0-9]","-","HEllo1World32")


#OOPS
class Set:
    
    def __init__(self,values):
        self.dict={}
        if values is not None:
            for value in values:
                self.add(values)
                
    def add(self,value):
        self.dict[value]=True
    
    def contains(self,value):
        return value in self.dict
        
    def remove(self,value):
        del self.dict[value]
        
s=Set([1,2])
s.add(1)
s.contains(1)

values=[1,2,3,4]
for i, value in enumerate(values):
    print i