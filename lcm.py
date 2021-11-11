x= int(input())
y = int(input())
#  num = 1
#  but using num form 1 will increase the memory space 
if (x>y):
    num = y
else:
    num =x
while(num>0):
    if(num%x==0 and num%y==0):
        print(num)
        break
    num +=1
