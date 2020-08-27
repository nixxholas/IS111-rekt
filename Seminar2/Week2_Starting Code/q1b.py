# ################################################################################
# Implement the function below:
def compute_geometric_mean(x, y, z):
    """
    This function returns the geometric mean of the three numbers x, y and z.
    """
    # Write your code here:
    return (x * y * z) ** (1. / 3.)


# ################################################################################
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!

firstNo = int(input("Enter your first number: "))
secondNo = int(input("Enter your second number: "))
thirdNo = int(input("Enter your third number: "))

print("The geometric mean of", firstNo, ",", secondNo, "and", thirdNo, "is:",
      compute_geometric_mean(firstNo, secondNo, thirdNo))