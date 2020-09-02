def get_avg_len(strings):
    # obtain the sum of all string chars and get the avg
    return sum(map(len, strings)) / len(strings) if len(strings) > 0 else 0


def get_longest_str(strings):
    return max(strings, key=len) if len(strings) > 0 else ''


def concatenate_emails(strings):
    email_str = ''
    for i in strings:
        curr_str = i.split('@')
        if len(curr_str) == 2 and not (' ' in curr_str[0] or ' ' in curr_str[1]): email_str += (i + ";")

    return email_str[:-1]


def check_hashtags(strings):
    if len(strings) <= 0: return False
    for i in strings:
        if i != '' and (i[0] != '#' or ' ' in i): return False
    return True


print(get_avg_len(["C", "Java", "Python", "PHP"]))
print(get_avg_len([]))

print(get_longest_str(["C", "Java", "Python", "PHP"]))
print(get_longest_str([]))
print(get_longest_str(["C", "Java", "HTML", "PHP"]))

my_list1 = ["tommy.goh@sis.smu.edu.sg", "alan_wong@gmail.com"]
print(concatenate_emails(my_list1))
my_list2 = []
print(concatenate_emails(my_list2))
my_list3 = ["IS111", "a @ b", "jerry.lee@sis.smu.edu.sg", "@@@", "alan_wong@gmail.com", "Python",
            "george_tan@yahoo.com"]
print(concatenate_emails(my_list3))

print(check_hashtags(["","#singapore", "#music", "#travel"]))
print(check_hashtags([]))
print(check_hashtags(["#singapore", "#music album", "#travel"]))
print(check_hashtags(["singapore", "#music", "#travel"]))
