# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 07:38:53 2017

@author: sivagami
"""
#Functions
def double(x):
    return x*2
    
def apply_to_one(f):
    return f(1)
    
my_double=double
print apply_to_one(my_double)

#lambda
print apply_to_one(lambda x:x+10)

#strings
print "\t"
print r"\t" #rawstdring

#multiline
print """ hello
          world
          and python"""
          
#list
l1=[1,2,3,4,5,6]
l2=["hello",0.1,'a']
l3=[l1,l2,[]]
print l3

print l1[1:-1]
1 not in l1        
l1.extend([9,0])
l1
l1.append(10)
len(l1)
len(l1[1:-1])


x,y=[1,2]
_,k=[1,5]

#Tuples immutable list

my_tuple=(2,3)
try:
    my_tuple[1]=0
except TypeError :
   print "Cannot modify"
  
def sum_product(x,y):
    return x+y,x*y

sp=sum_product(4,5)
s,p=sum_product(5,6)
print sp ,s,p

#swapping
x,y=1,2
x,y=y,x
print x,y

#Dictionaries

dict={}
dict={"Padma":80,"Sai":100}


try:
    print dict["Sivgami"]
except KeyError:
    print "key Not Found"
    
"Sivagami" in dict

##default values
print dict.get("Siavgami",0)
print dict.get("Siavgami")


tweet={
"user":"Sivagami",
"text":"Begining of data Science",
"retweet_count" :100,
"hastags":["data","#Begining"]
}

print tweet.keys()
print tweet.items()
print tweet.values()

"Sivagami" in tweet.keys()
"Sivagami" in tweet.values()


#defaultdict initialises new key with "type" value

from collections import defaultdict

mydefault=defaultdict(int)
print mydefault["Sivagami"]
mydefault["Sivagami"]+=1

myDlist=defaultdict(list)
myDlist[2].append(2)
print myDlist
myDlist["Sivagami"].append(2)

#dd_dict=defaultdict(dict)	error
#myDdict["Padma"]["Job"]="Data Scientist"

myDpair=defaultdict(lambda:[0,0])
myDpair[2][1]=1
print myDpair

#Counter
from collections import Counter
myWordList=["padma","sai","padma","subha","sai","nambi","sai"]
print Counter(myWordList)

for word,count in Counter(myWordList).most_common(1):
    print word,count


#Sets
s=set()
s.add(1)
s.add(2)
s.add(2)
s
2 in s
list=[1,2,3,4,1,2,3]
print set(list)

#Control flow
x=10
parity="even" if x%2==0 else "odd"
    
#truthiness
print True is None
print False is None