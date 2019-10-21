print ("Welcome!!")
x = 4
y = 8

while True:

    progress = input("Do you want to proceed?...(yes or no).........").lower()

    if progress == "yes":

        answer = input("Do you want to write an equation in full?....(yes or no)").lower()

        if answer == "yes":

            equation = input("Write your equation in full ....ex.(x+y)...").lower()
            print (eval(equation))          

        if answer == "no":

            x = int (input("What is the x variable, which is the first in the operation?........"))
            print(x)

            y = int (input("What is the y variable, which is the second in the operation?......."))
            print(y)

            operation = input("What is your operation to perform?...(+ - * /)......")
            print (operation)

            if operation == "+":
                print (x+y)

            if operation == "*":
                print (x*y)

            if operation == "/":
                print (x/y)

            if operation == "-":
                print (x-y)

            print("Thank you for using the service!")

    else:

        print ("Thanks for using the service!!")
        break