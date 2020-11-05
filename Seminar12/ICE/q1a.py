def retrieve_email(email_dict, name):
    if name in email_dict:
        return email_dict[name]
    else:
        return None


print(retrieve_email({'Jack':'jack@gmail.com', 'Peter':'peter@smu.edu.sg'}, 'Jack'))
print(retrieve_email({'Jack':'jack@gmail.com', 'Peter':'peter@smu.edu.sg'}, 'John'))
