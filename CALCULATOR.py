# Calculator


#Addition of numbers
def add(fnumber, snumber):
   return fnumber + snumber

def subtract(fnumber, snumber):
   return fnumber - snumber

def multiply(fnumber, snumber):
   return fnumber * snumber

def divide(fnumber, snumber):
   return fnumber / snumber

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


operations = input("Enter Operation:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operations == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif operations == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif operations == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif operations == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
