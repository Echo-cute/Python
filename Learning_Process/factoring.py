'''
#range()=>得到一個範圍
for i in range(2, 99999999999999999999999999999999999999999999999999999999):
    print (i)

'''
'''
z=19876

print (int (z/100))
'''
'''
z=int(input("please enter number "))
ddd=True

for k in range(1,int (z/2)+1): #int() => 小數轉整數
    if z%k==0: # %=>求餘數
         print (k, int(z/k))
     
    
#print("Is Prime=" + str(ddd)) #str=> 轉字串
'''
import math

z = int(input("please enter number "))
ddd = True

for k in range(1, int(math.sqrt(z)) + 1):
    if z % k == 0:
        print(k, z // k)
