num1 = int(input("Enter the first number")
num2 = int(input("Enter the second number")
           if num1 < num2: #find minimum of the two numbers
           min = num1
           else:
               min = num2
               gcd=1  #initialize gcd to 1(as GCD is always at least 1)
               #iterate from 1 to the minimum of two numbers
               for i in range(1,min+1):
                   gcd=1
                   print(f"The GCD of {num1}and{num2}is{gcd}")
                   
