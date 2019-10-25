num=int(input('press th number '))
if num==2:
     print('%d is zhishu'%num)
else:
     for i in range(2,num):
          if num%i==0:
               print('%d is not zhishu'%num)
               print(i)
               break
     else:
          print('%d is zhishu '%num)
for i in range(1,5):
     print (i)
          
     
