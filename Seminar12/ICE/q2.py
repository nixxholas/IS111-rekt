user_input = input('Enter a string > ')
inputs = {}
while len(user_input) > 0:
    if user_input[0].lower() in inputs:
        inputs[user_input[0].lower()].append(user_input)
    else:
        inputs[user_input[0].lower()] = [user_input]

    user_input = input('Enter a string > ')

print("You've entered")
for key in inputs:
    print('\t\t' + str(len(inputs[key])) + ' strings starting with ' + (("' " + key + " '") if not key.isalpha() else ("' " + key.upper() + " ' or '" + key + "'")))