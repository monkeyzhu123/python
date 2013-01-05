#!/usr/bin/env python
'make_or_read_file.py--------make or read file'
import os

def makefile(fname):
    #function makefile------create text file
    ls=os.linesep
    
    # get file content lines
    all=[]
    #print("\nEnter lines ('.' by itself quit)\n")
    # loop until user terminates input
    while True:
        entry=input('>')
        if entry=='.':
            break
        else:
            all.append(entry)
    # write lines to file with proper line-ending
    fobj=open(fname,'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print("done")

def readfile(fname):
    for lines in f:
        print(lines,end='')
    f.close()

############## BEGIN main ##############
print('-'*15+"the python script can do"+'-'*15)
print('-'*15+"if the file is not exit --->create it")
print('-'*15+"if the file is exist    --->display it")
print()
fname=input('input your filename:')
if os.path.exists(fname):
    try:
        f=open(fname)
    except (IOError,e):
        print("open %s for IOerror" % fname)
    else:
        readfile(fname)
else:
    print("the %s not exists" % fname)
    yes_or_no=input("create %s?(y/n)" % fname)
    if yes_or_no=='y':
        makefile(fname)
    else:
        print("nothing to do!")
