num=30
guess=0
cr=True
while cr:
     guess = int(input('press the possible number'))
     if guess!= num:
          if guess >num:
               print('too big')
          if guess<num:
               print('too small')
     else:
          cr=False
          print('well done,just %d'%num)
          
     
                 
