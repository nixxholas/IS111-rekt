def do_trick(a_list):
    a_list = a_list + a_list[1:3] + [a_list[3]]
    print(a_list)


my_list = ['a', 'b', 'c', 'd']
do_trick(my_list)
print(my_list)

def do_another_trick(a_list):
    a_list.append(a_list[1:3] + [a_list[3]])
    print(a_list)


my_list = ['a', 'b', 'c', 'd']
do_another_trick(my_list)
print(my_list)

my_str = '123'

for index in range(0, len(my_str) - 1):
    n = int(my_str[index] + my_str[index+1])
    print(n)
    m = int(my_str[index:index+2])
    print(m)