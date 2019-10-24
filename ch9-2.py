soldier={'tag':'red','score':15}
print (soldier)
         
fruits={'watermelon':15,'banana':20,'pear':25}
noodle={'beef':10,'meat':80,'yang':60}
print('pear=',fruits['pear'])
print ('beef=',noodle['beef'])

fruits['orange']=18
print(fruits)
print('orange=',fruits['orange'])


print('old banana is ',fruits['banana'])
fruits['banana']=15
print('new banana is ',fruits['banana'])
del fruits['watermelon']
print('old dicis ',fruits)
fruits.clear()
print('new dict',fruits)

vag={}
print(vag)
print(type(vag))

vag=noodle.copy()
print('new vag is',vag)
print(id(noodle))
print(id(vag))
n=len(noodle)
print (n)
fruits={'watermelon':15,'banana':20,'pear':25}
##key=input('press the key')
##value=input('press the value')
##if key in fruits:
##     print('%s is in here its price is %d'%(key,fruits[key]))
##else:
##     fruits[key]=value
##     print('%s is not here then add it up'%key,fruits)
##for name ,price in fruits.items():
##     print('name is ',name)
##     print('price is ',price)
##for name in fruits.keys ():
##     print('just name is',name)

for name in sorted(fruits.keys ()):
     print ('sorted name is',name)
armys=[]
sold={'tag':'red','score':15,'speed':'slow'}
for sold_num in range(50):
     
     armys.append(sold)
for soldier in armys[:3]:
     print (soldier)
print ('the amount of army is',len(armys))





     

           

