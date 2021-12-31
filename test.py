import main,sys,os
import random
a = 1
while a == 100 or a < 100:
    c = open('./c/'+str(random.randint(1,9999999999999))+'.txt','w+')
    c.write(str(random.randint(1,9999999999999)))
    c.close()
    a=a+1
path = main.init()
print(path)
main.move(path,'./a')