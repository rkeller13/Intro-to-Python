#obtains input from user
populationA = int(input("Enter population of Town A: "))
populationB = int(input("Enter population of Town B: "))
growthA = float(input("Enter growth rate of Town A: "))
growthB = float(input("Enter growth rate of Town B: "))

# This checks the input values, I am assuming that the populations
# and growth rates are considered concrete, true values for this problem
# not something that the user can make up
while populationA >= populationB or growthA <= growthB:
    print("You entered false values.  Please reenter correct values.")
    populationA = int(input("Enter population of Town A: "))
    populationB = int(input("Enter population of Town B: "))
    growthA = float(input("Enter growth rate of Town A: "))
    growthB = float(input("Enter growth rate of Town B: "))

# n = number of years  passed
n=0

#computes population growth for each city
while populationA < populationB:
    populationA += populationA*(growthA/100)*n
    populationB += populationB*(growthB/100)*n
    n += 1
    print(populationA)
    print(populationB)
    
print("The population of Town A will be greater than or equal to town B in " + str(n) + " years.")
print("The population of Town A after " + str(n) + " years is " + str(int(populationA)) + ".")
print("The population of Town B after " + str(n) + " years is " + str(int(populationB)) + ".")
   
