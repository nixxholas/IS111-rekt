def create_email_dict(info_list):
    email_dict = {}
    for i in range(0, len(info_list), 2):
        email_dict[info_list[i]] = info_list[i + 1]
    return email_dict