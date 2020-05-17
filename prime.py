n=int(input("Enter a number"))
if n<=1:
    print("Please enter the number greater than one")
else:
     for i in range(2,n):
           if(n%i)==0:
              print("Its not a prime no")
              break
     else:
        print("Its a prime number")
