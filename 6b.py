n = input("Enter the string to be checked: ")
ch = di = sp = 0
for x in range(len(n)):
    if n[x].isalpha():
        ch+=1
    elif n[x].isdigit():
        di+=1
    else:
        sp+=1
print("Alphabets=",ch,"Digits=",di,"Special Characters=",sp)