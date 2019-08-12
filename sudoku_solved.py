import pandas as pd
import numpy as np
sudo=pd.read_excel('fuck.xlsx').values
ludo=pd.read_excel('fuck.xlsx').values
#print(sudo)

block1=[]
block2=[]
block3=[]
block4=[]
block5=[]
block6=[]
block7=[]
block8=[]
block9=[]
collection=[]



def sudoku():      
    global block1,block2,block3,block4,block5,block6,block7,block8,block9,sudo
    arr=zip(*np.where(sudo==0))
    loc=[]
    for points in arr:
        loc+=[(points)]
    current=[1,2,3,4,5,6,7,8,9]    
    for x,y in loc:
        sample=sudo[:,y]
        for item in sample:
            counter=0
            for num in current:
                if item!=0 and num==item:
                    current[counter]=0
                counter+=1
        sample=sudo[x,:]
        for item in sample:
            counter=0
            for num in current:
                if item!=0 and num==item:
                    current[counter]=0
                counter+=1
        if x<3 and y<3:
    #        print('({},{})\t'.format(x,y),current)
            block1+=current
        elif 2<x<6 and y<3:
      #      print('({},{})\t'.format(x,y),current)
            block2+=current
        elif 5<x and y<3:
    #        print('({},{})\t'.format(x,y),vertical)
            block3+=current
        elif x<3 and 2<y<6:
    #        print('({},{})\t'.format(x,y),vertical)
            block4+=current
        elif 2<x<6 and 2<y<6:
     #       print('({},{})\t'.format(x,y),current)
            block5+=current
        elif 5<x and 2<y<6:
    #        print('({},{})\t'.format(x,y),vertical)
            block6+=current
        elif x<3 and 5<y:
    #        print('({},{})\t'.format(x,y),vertical)
            block7+=current
        elif 2<x<6 and 5<y:
    #       print('({},{})\t'.format(x,y),current)
            block8+=current
        elif 5<x and 5<y:
    #        print('({},{})\t'.format(x,y),current)
            block9+=current
            
        current=[1,2,3,4,5,6,7,8,9]   
        
def substitute(m,n,o,p,block):
    global sudo,block1,block2,block3,block4,block5,block6,block7,block8,block9
    # blocks are declared global only because we need to set them to null in the end, nothing else
    l=[]
    
    temp=globals()['sudo']
    for k in sudo[m:n,o:p]:
                l+=list(k)
    arr1=zip(*np.where(temp[m:n,o:p]==0))
    loc1=[]
#    finding indexes of blank spaces
    for points in arr1:
       loc1+=[(points)]
    for i in block:
        if block.count(i)==1 and i!=0:
            
            if l.count(i)==1:
                continue
            else:
                j=block.index(i) #index of the potential num
                j=int(j/9)
                a,b=loc1[j]
                sudo[m+a,o+b]=i
                
# setting the blocks to null
    block1=[]
    block2=[]
    block3=[]
    block4=[]
    block5=[]
    block6=[]
    block7=[]
    block8=[]
    block9=[]
#    print(sudo)
#step-1 We need to fill in the inevitable values in each block

for y in range(0,20):
    sud1=[]
    sudoku()
    
    substitute(0,3,0,3,block1)
    
    sudoku()
    substitute(3,6,0,3,block2)
    sudoku()
    substitute(6,9,0,3,block3)
    sudoku()
    substitute(0,3,3,6,block4)

    sudoku()
    substitute(3,6,3,6,block5)

    sudoku()
    substitute(6,9,3,6,block6)
    sudoku()
    substitute(0,3,6,9,block7)
    sudoku()
    substitute(3,6,6,9,block8)
    sudoku()
    substitute(6,9,6,9,block9)
#    if sudo==sud1
#    sudo=sudo1
print(sudo)