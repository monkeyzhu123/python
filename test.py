#!/usr/bin/env python
#function for test return
def function_multi(a=1,b=1):
    return a*b

print ("the value is: %s" % function_multi(2,6))

#mark the grade
mark_is=int(input("enter the mark(int):"))
grade_is=['A','B','C','D','F']
if  mark_is in range(90,101):
    print ("the mark is %s grade" % grade_is[0])
elif mark_is in range(80,90):
    print ("the mark is %s grade" % grade_is[1])
elif mark_is in range(70,80):
    print ("the mark is %s grade" % grade_is[2])
elif mark_is in range(60,70):
    print ("the mark is %s grade" % grade_is[3])
elif mark_is in range(0,60):
    print ("the mark is %s grade" % grade_is[4])
else:
    print ("the mark: %s.but I can't handle" % mark_is)

#judge the year leap or not
def year_judge(year_s):
    if year_s%100 !=0:
        if year_s%4==0:
            return "leap year"
        else:
            return "not leap"
    else:
        if year_s%400==0:
            return "leap year"
        else:
            return "not leap"
try:
    year_s=int(input("enter the year for handling:"))
except (ValueError,e):
    print("***error***:%s" % e)
else:
    pass
    print (year_judge(year_s))

#display the string
s=input("enter strings:")
i=len(s)
while True:
    if i>0:
        print (s[0:i])
        i-=1
    else:
        break
    
