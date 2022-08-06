import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def pwr(x,y):
    return x**y

def log(x,y):
    return math.log(x,y)

def comb(x,y):
   numerator=math.factorial(x)
   denominator=math.factorial(x-y)
   denom2=math.factorial(y)
   comb = numerator // (denominator*denom2)
   return comb

def perm(x,y):
    numerator=math.factorial(x)
    denominator=math.factorial(x-y)
    perm = numerator//denominator
    return perm

def natln(x):
     return math.log(x)

  

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.x^n")
print("6.logarithm")
print("7. nCr")
print("8. nPr")
print("9.Natural logarithm")
print("10.e^x")

while True:
  
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

    
    if choice in ('1', '2', '3', '4','5','6','7','8'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1,"^", num2, "=",pwr(num1,num2))
        elif choice == '6':
            print(num1, "log" ,num2, "=", log(num1,num2))
        elif choice == '7':
            print(num1, "C" ,num2, "=", comb(num1,num2))
        elif choice == '8':
            print(num1, "P" ,num2, "=", perm(num1,num2))
        
  
            
    elif choice =='9':
     num = float(input("Enter the number: "))
     print("ln",num, "=", natln(num))
    elif choice =='10':  
     num = float(input("Enter the number: "))
     e=2.718281828459045
     print( "e","^", num , "=" ,e**num)
    else:
     print("Invalid Input")
    
        
    
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no": 
     break
    
