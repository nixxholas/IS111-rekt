def add_new_email(email_dict, tuple):
    if tuple[0] in email_dict.keys():
        old_res = email_dict[tuple[0]] + ''
        email_dict[tuple[0]] = tuple[1]
        return old_res
    else:
        email_dict[tuple[0]] = tuple[1]
        return None
