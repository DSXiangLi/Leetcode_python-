<<<<<<< HEAD
'''
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) l = [1, 1, 1]
Output:
    (int) 1



Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
Output:

    (int) 3
'''

## Exceed time limit
def answer(l):
    if(len(l)<3):
        return 0
    if(len(l)==3):
        return 1

    # find divide tuple
    divide_tuple = []
    hash_end = dict() ## key = {end},  value = {start}
    for i in range((len(l)-1),0,-1 ):
        for j in range(i-1,-1,-1):
            if (l[i] % l[j] == 0):
                divide_tuple.append((j,i))
    result = []
    for (start,end) in divide_tuple:
        if(start in hash_end.keys()):
            hash_end[start].append((start,end))
        else:
            hash_end[start] = [(start,end)]
        if(end in hash_end.keys()):
            for i in hash_end[end]:
                result.append((start,) + i)

    print(result)

    return len(result)

##
def answer(l):
     if len(l) < 3:
         return 0
     if len(l)==1:
         return 1
     count = 0
     for i in range(1, (len(l)-1)):
         count_start = len([x for x in l[:i] if l[i]%x ==0 ])
         count_end = len([x for x in l[(i+1):] if x%l[i]==0])
         count  += count_start * count_end
     return count
=======
'''
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) l = [1, 1, 1]
Output:
    (int) 1



Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
Output:

    (int) 3
'''

## Exceed time limit
def answer(l):
    if(len(l)<3):
        return 0
    if(len(l)==3):
        return 1

    # find divide tuple
    divide_tuple = []
    hash_end = dict() ## key = {end},  value = {start}
    for i in range((len(l)-1),0,-1 ):
        for j in range(i-1,-1,-1):
            if (l[i] % l[j] == 0):
                divide_tuple.append((j,i))
    result = []
    for (start,end) in divide_tuple:
        if(start in hash_end.keys()):
            hash_end[start].append((start,end))
        else:
            hash_end[start] = [(start,end)]
        if(end in hash_end.keys()):
            for i in hash_end[end]:
                result.append((start,) + i)

    print(result)

    return len(result)

##
def answer(l):
     if len(l) < 3:
         return 0
     if len(l)==1:
         return 1
     count = 0
     for i in range(1, (len(l)-1)):
         count_start = len([x for x in l[:i] if l[i]%x ==0 ])
         count_end = len([x for x in l[(i+1):] if x%l[i]==0])
         count  += count_start * count_end
     return count
>>>>>>> 8873f5b1fc4c1c3da41ae8936576f59ab0d7f967
