#Calculating number of digits and letters in a string
s = input("Input a string: ")
D=L=0
for c in s:
    if c.isdigit():
        D=D+1
    elif c.isalpha():
        L=L+1
    else:
        pass
print("Letters", L)
print("Digits", D)
