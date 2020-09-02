def extract_email_id(email):
    return email.split('@')[0]


def extract_multiple_email_ids(emails):
    email_arr = emails.split(';')
    for i in email_arr:
        print(extract_email_id(i))


print(extract_email_id("jerry.lee@sis.smu.edu.sg"))
print(extract_email_id("alan_wong.com"))
print(extract_email_id(""))
print(extract_email_id("alan_wong@gmail.com"))
print("==================================================")
extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com")
extract_multiple_email_ids("")
extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg")