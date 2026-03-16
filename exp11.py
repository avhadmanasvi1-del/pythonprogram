print("1:ADDITION")
print("2:SUBSTRACTION")
print("3:MULTIPLICATION")
print("4:MODULUS")
print("5:DIVISION")
def add(num1,num2):
  sum=num1+num2
  print("ADDITION=",sum)
def sub(num1,num2):
  sub=num1-num2
  print("SUBSTRACTION=",sub)
def multiply(num1,num2):
  multiply=num1*num2
  print("MULTIPLICATION=",multiply)
def modulus(num1,num2):
  mod=num1%num2
  print("MODULUS=",mod)  
def division(num1,num2):
  if num2 == 0:
        print("error :cannot divide by zero")
  else:
        result = num1 / num2
        print("DIVISION =", result)
num1=int(input("Enter 1st value"))
num2=int(input('Enter 2nd value'))
choice=int(input('Enter choice'))
if choice == 1:
    add(num1, num2)
elif choice == 2:
    sub(num1, num2)
elif choice == 3:
    multiply(num1, num2)
elif choice == 4:
    modulus(num1, num2)
elif choice == 5:
    division(num1, num2)
else:
    print("Invalid choice")
