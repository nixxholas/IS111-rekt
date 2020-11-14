## Q1
def reverse_segments(text):
    segments = []

    cur_text = ''
    for c in text:
        if c not in '|-=':
            cur_text += c
        else:
            segments.append(cur_text[::-1])
            segments.append(c)
            cur_text = ''

    if cur_text != '':
        segments.append(cur_text[::-1])

    return segments
        
# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    print(f"Test Case {tc_num} : reverse_segments ('a b c|def-123 aaa=|(abc)')")
    result = reverse_segments('a b c|def-123 aaa=|(abc)')
    print("Expected : ['c b a', '|', 'fed', '-', 'aaa 321', '=', '', '|', ')cba(']")
    print(f"Actual   : {result}")

    print()
    print("Expected return type  : <class 'list'>")
    print("Actual return type    : ", end="")
    if (isinstance(result, list)):
        print(type(result))
    else:
        print("N/A")
    
    print()

    tc_num += 1
    print('-' * 40)
    
    print(f"Test Case {tc_num} : reverse_segments ('111*si|-2 bal tset =kcul doog')")
    result = reverse_segments('111*si|-2 tset bal@=!kcul doog')
    print("Expected : ['is*111', '|', '', '-', '@lab test 2', '=', 'good luck!']")
    print(f"Actual   : {result}")

