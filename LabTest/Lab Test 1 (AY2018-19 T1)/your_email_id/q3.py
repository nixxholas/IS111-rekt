#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020@sis.smu.edu.sg
#
def mask_out(sentence, banned, substitutes):
    # write your answer between #start and #end
    c_arr = list(sentence)
    subs = list(substitutes)
    sub_it = 0

    for i in range(0, len(c_arr)):
        if c_arr[i] in banned:
            if len(subs) <= 1:
                c_arr[i] = subs[0]
            else:
                c_arr[i] = subs[sub_it]
                if sub_it + 1 < len(subs): sub_it += 1
                else: sub_it = 0

    return "".join(c_arr)


print('Test 1')
print('Expected:abcd#')
print('Actual  :' + mask_out('abcde', 'e', '#'))
print()

print('Test 2')
print('Expected:#$solute')
print('Actual  :' + mask_out('absolute', 'ab', '#$'))
print()

print('Test 3')
print('Expected:121hon')
print('Actual  :' + mask_out('python', 'pyt', '12'))
print()





