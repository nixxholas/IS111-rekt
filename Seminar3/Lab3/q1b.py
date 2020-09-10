# Q1b
def compare_values_1(a, b):
    if (a != b):
        return True
    else:
        return False
    
def compare_values_2(a, b, c):
    if (a == b + c):
        print("a == b + c")
    if (b == a + c):
        print("b == a + c")
    if (c == a + b):
        print("c == a + b")

print(compare_values_1("1 + 2", "3"))
compare_values_2('1', '', '1')
