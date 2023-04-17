def main():
    number= get_number()
    helloworld(number)


def get_number():
   while True:
    x= int(input("Enter the value of x"))
    if x > 0:
        break
 return x

 def helloworld(x):
     for_in range(x):
       print("Hello World")

main()
