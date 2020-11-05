def create_email_dict(arr):
    res = {}

    while len(arr) > 0:
        name = arr.pop(0)
        email = arr.pop(0)

        res[name] = email

    return res


print(create_email_dict(["Jack", "jack@gmail.com", "Mary", "mary.loh@smu.edu.sg", "John", "john.smith@microsoft.com"]))
