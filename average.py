print ("Welcome to our site!")
def Average(variables): 
    return sum(variables) / len(variables) 
variables = []
while True:
    num = int(input("Input a number or type 0 if done..........."))
    if num == 0:
        break
    else:
        variables.append(num)
average = Average(variables) 
print("Average of the variables =", round(average, 2)) 
print("Thanks for coming to the site!")