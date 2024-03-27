def find_factor(x):
    ans = []
    for i in range(x):
        
        if x%(i+1) == 0:
            ans.append(i+1)
            
        else:
            continue
    return ans

#-------------------------------
def factorization(x):
    a_list = []    

    result={}

    while True:
        a_list = find_factor(x)
        if len(a_list) == 2:

            if x not in result:
                result[x]=1
            else:
                result[x]+=1
            break

        else:
            if a_list[1] not in result:
                result[a_list[1]]=1
            else:
                result[a_list[1]]+=1

            x=int(x/a_list[1])

    return result    

#-------------------------------
def xyz(k_list):
    fac_list=[]

    result={}

    for x in k_list:
        fac_list.append(factorization(x))

    for a_dic in fac_list:
        for k in a_dic:
            if k not in result:
                result[k]=a_dic[k]
            else:
                if a_dic[k]>result[k]:
                    result[k]=a_dic[k]               

    min_mul=1

    for k in result:        
        min_mul*=pow(k, result[k])

    return min_mul

#-------------------------------
'''
if __name__ == '__main__':
    import math

    #k_list=[25, 45, 90]
    k_list = [int(num) for num in input("Enter numbers separated by spaces:").split()]
    min_mul=xyz(k_list)
    print (min_mul)
'''
if __name__ == '__main__':
    import math

    while True:
        try:
            k_list = [int(num) for num in input("Enter numbers separated by spaces ").split()]
            break
        except ValueError:
            print("Please enter valid integers separated by spaces.")

    min_mul = xyz(k_list)
    print( min_mul)
    