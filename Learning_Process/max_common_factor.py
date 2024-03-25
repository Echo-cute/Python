
#-----------------------------------
def find_factor(x):
    ans = []
    for i in range(x):
        
        if x%(i+1) == 0:
            ans.append(i+1)
            
        else:
            continue
    return ans
#------------------------------------
def common_factor(x, y):
    find_factor_x = find_factor(x)
    find_factor_y = find_factor(y)
    ans = []
    for i in find_factor_x:
        if i in find_factor_y:
            ans.append(i)    
    return ans
#-------------------------------------
def max_common_factor(x, y):
    spam = common_factor(x, y)
    spam.sort()
    return spam[-1]
#-------------------------------------

print('input number1')
num1 = int(input())
num2 = int(input())



#print(common_factor(num1, num2))
print(max_common_factor(num1, num2))




