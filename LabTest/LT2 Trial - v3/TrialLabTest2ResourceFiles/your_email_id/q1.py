## Q1
def max_age(student_dict,gender):

    return 0
        
# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    student_dict = {'John': ('M', 21), 'Kate': ('F', 19), 'Eric': ('M', 23)}
    
    print(f"Test Case {tc_num} : max_age ({student_dict}), 'M')")
    result = max_age(student_dict, 'M')
    print("Expected : ('Eric', 23)")
    print(f"Actual   : {result}")

    print()
    print("Expected return type  : <class 'tuple'>")
    print("Actual return type    : ", end="")
    if (isinstance(result, tuple)):
        print(type(result))
    else:
        print("N/A")

    print("Expected return type of the first element of the tuple : <class 'str'>")
    print("Actual return type of the first element of the tuple   : ", end="")
    if (isinstance(result, tuple)):
        print(type(result[0]))
    else:
        print("N/A")

    tc_num += 1
    print('-' * 40)
    
    student_dict = {'Kate': ('F', 22), 'John': ('M', 23), 'Susan': ('F', 18)}
    
    print(f"Test Case {tc_num} : max_age ({student_dict}, 'F')")
    result = max_age (student_dict,'F')
    print("Expected : ('Kate', 22)")
    print(f"Actual   : {result}")

    print()

    tc_num += 1
    print('-' * 40)
    
    student_dict = {'Kate': ('F', 24), 'Mary': ('F', 22), 'Susan': ('F', 19)}
    
    print(f"Test Case {tc_num} : max_age ({student_dict}, 'M')")
    result = max_age (student_dict,'M')
    print("Expected : None")
    print(f"Actual   : {result}")

    print()

    tc_num += 1
    print('-' * 40)
    
    student_dict = {}
    
    print(f"Test Case {tc_num} : max_age ({student_dict},'')")
    result = max_age (student_dict, '')
    print("Expected : None")
    print(f"Actual   : {result}")


