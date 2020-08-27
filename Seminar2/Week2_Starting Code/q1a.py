# ################################################################################
# The following code is given to you.
def compute_average(a, b, c):
    """
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c) / 3


# ################################################################################
# Write your code below:

print("The average is:",
      compute_average(float(input("Enter the first number: ")), float(input("Enter the second number: ")),
                      float(input("Enter the third number: "))))
