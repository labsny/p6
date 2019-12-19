s1,s2=set(),set()
n1=eval(input("Enter the no of elements of set 1: "))
n2=eval(input("Enter the no of elements of set 2: "))

print("Enter the elements of set 1: ")
for i in range(0,n1):
	s1.add(int(input()))

print("Enter the elements of set 2: ")
for i in range(0,n2):
	s2.add(int(input()))

s1=sorted(list(s1))
s2=sorted(list(s2))

print("Cartesian Product: ")
print("{",end=" ")
for i in range(0,n1):
    for j in range(0,n2):
        print("{",s1[i],",",s2[j],"}",end=" ")
print("}")