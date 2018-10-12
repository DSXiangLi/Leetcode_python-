# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 07:29:31 2018

@author: xli
"""
'''
The cake is not a lie!
======================

Commander Lambda has had an incredibly successful week: she completed the first test run of her LAMBCHOP doomsday device, she captured six key members of the Bunny Rebellion, and she beat her personal high score in Tetris. To celebrate, she's ordered cake for everyone - even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone, you'll get in big trouble. 

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called answer(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) s = "abccbaabccba"
Output:
    (int) 2

Inputs:
    (string) s = "abcabcabcabc"
Output:
    (int) 4

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

'''


from timeit import default_timer as timer 

def answer1(mystr):
    count = 1 
    for gr in range(1, int(len(mystr)/2+1)):
        if (len(mystr)%gr ==0):
            flag =True
            for i in range(gr,len(mystr)):
                if mystr[i%gr] != mystr[i]:
                    flag = False
                    break
            if flag:
                count = int(len(mystr)/gr)
                break 
    return count

def answer2(mystr):
    count = 1
    val_count = dict()
    for i in range(len(mystr)):
        if(mystr[i] in val_count.keys()):
            val_count[mystr[i]] +=1
        else:
            val_count[mystr[i]] = 1
    
    for gr in range(1, int(len(mystr)/2+1)):
        if (len(mystr)%gr == 0 & sum([count % gr for count in val_count.values()])==0):
            flag =True
            for i in range(gr,len(mystr)):
                if mystr[i%gr] != mystr[i]:
                    flag = False
                    break
            if flag:
                count = int(len(mystr)/gr)
                break 
    return count


def main():
    mystr = input('Input your String here:')
    start = timer()
    answer1(mystr)
    end = timer()
    time1= end -start 
    
    start = timer()
    answer2(mystr)
    end = timer()
    time2= end -start
    
    print("Running Time for answer1 = {} for answer2 = {}".format(time1,time2))

