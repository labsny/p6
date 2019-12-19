lst=[]
ls=[]
n=eval(input("Enter the no of string: "))
c=0
print("Enter Strings: ")
for i in range(0,(n)):
    ele=input()
    lst.append(ele)
for i in lst:
    if (len(i)>=2 and i[0]==i[-1]):
        ls.append(i)
        c+=1
print("The strings satisfying the conditions are:",c)
print(ls)
