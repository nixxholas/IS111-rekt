#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020@sis.smu.edu.sg
#
import string


def print_dancing_string(sentence, start):
    # write your answer between #start and #end
    s_arr = list(sentence)
    top_arr, mid_arr, bot_arr = ["|"], ["|"], ["|"]  # Store them like that first.

    start_allowed = 'TMB'
    if start not in start_allowed:
        print('Invalid operation.')
        exit()

    for i in range(0, len(s_arr)):
        c = s_arr[i]

        # If the current element is the first and the start is at the top OR
        if (i == 0 and start == 'T') or (
                # if the current length of the top_arr is more than 1 and if the 2nd last element was |, it means that
                # we're currently at the 3rd element to print and the mid_arr's 2nd element is definitely an ascii_
                # letter and the last element of bot_arr is a whitespace OR
                len(top_arr) > 1 and top_arr[-2] == '|' and (mid_arr[-1] in string.ascii_letters) and
                bot_arr[-1] == ' ') or (
                # If the last mid_arr is a letter and if the 2nd last bot_arr is a letter
                mid_arr[-1] in string.ascii_letters and bot_arr[-2] in string.ascii_letters):
            # It means that we haven't populated top_arr yet, so let's do it
            top_arr.append(c)

            # At the very end I think we should fill the 'gaps'
            mid_arr.append(' ')
            bot_arr.append(' ')
        # If the current element is the first and the start is at the mid OR
        elif (i == 0 and start == 'M') or (
                # Scenario when top or bot starts first
                # If mid_arr has more than 1 element and if the 2nd last mid_arr element is the beginning and
                # the last mid_arr is a whitespace and if either the bot or top_arr's last element is a character,
                len(mid_arr) > 1 and mid_arr[-2] == '|' and mid_arr[-1] == ' ' and (
                top_arr[-1] or bot_arr[-1] in string.ascii_letters)) or (
                # If the last top element is a character and the last bot element is a whitespace
                (top_arr[-1] in string.ascii_letters and bot_arr[-1] == ' ') or (
                # or if the last bot element is a character and the last top element is a whitespace
                bot_arr[-1] in string.ascii_letters and top_arr[-1] == ' ')):
            mid_arr.append(c)

            # At the very end I think we should fill the 'gaps'
            top_arr.append(' ')
            bot_arr.append(' ')
        # If the current element is the first and the start is at the bot or
        # if the bot array is less than or equal to the others,
        elif (i == 0 and start == 'B') or (bot_arr[-1] == ' '):
            bot_arr.append(c)

            # At the very end I think we should fill the 'gaps'
            top_arr.append(' ')
            mid_arr.append(' ')

    top_arr.append('|')
    mid_arr.append('|')
    bot_arr.append('|')

    print("".join(top_arr))
    print("".join(mid_arr))
    print("".join(bot_arr))


print('Test 1')
print('Expected:')
print('| |')
print('|a|')
print('| |')
print('-' * 20)
print('Actual:')
print_dancing_string('a', 'M')
print()

print('Test 2')
print('Expected:')
print('| b|')
print('|a |')
print('|  |')
print('-' * 20)
print('Actual:')
print_dancing_string('ab', 'M')
print()

print('Test 3')
print('Expected:')
print('| b |')
print('|a c|')
print('|   |')
print('-' * 20)
print('Actual:')
print_dancing_string('abc', 'M')
print()

print('Test 4')
print('Expected:')
print('| b  |')
print('|a c |')
print('|   d|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcd', 'M')
print()

print('Test 5')
print('Expected:')
print('| b   f   |')
print('|a c e g i|')
print('|   d   h |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'M')
print()

print('Test 6')
print('Expected:')
print('|a   e   i|')
print('| b d f h |')
print('|  c   g  |')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'T')
print()

print('Test 7')
print('Expected:')
print('|  c   g  |')
print('| b d f h |')
print('|a   e   i|')
print('-' * 20)
print('Actual:')
print_dancing_string('abcdefghi', 'B')
print()

print('Test 8')
print('Expected:')
print('||')
print('||')
print('||')
print('-' * 20)
print('Actual:')
print_dancing_string('', 'T')
print()
