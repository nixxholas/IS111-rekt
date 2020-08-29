# lab2_Q6
# ################################################################################
# The following code is given to you.

def compute_phone_bill(base, data_limit, amount_data=0.0, num_extra_sms=0, num_minutes_extra_calls=0):
    return base + max(0.0,
                      (amount_data - data_limit * 1024)) * 4.5 + num_extra_sms * 0.05 + num_minutes_extra_calls * 0.15


# ################################################################################
# You can verify your answers to Q6 by running the function calls below.

# 35.5
print(compute_phone_bill(35.5, 2, 800))
# 35.5
print(compute_phone_bill(35.5, 3))
# Error, data_limit not provided.
print(compute_phone_bill(22.5))
# 35.5
print(compute_phone_bill(35.5, data_limit=2, amount_data=800))
# 35.5
print(compute_phone_bill(base=35.5, data_limit=2, amount_data=800))
# 20.0
print(compute_phone_bill(data_limit=2, amount_data=800, base=20))
# 35.5
print(compute_phone_bill(35.5, amount_data=800, data_limit=2))
# Error, base not provided.
print(compute_phone_bill(amount_data=800, data_limit=2))
# 32.0
print(compute_phone_bill(32, 2, 800))
# 44.5
print(compute_phone_bill(35.5, 2, 2050))
# 39.0
print(compute_phone_bill(35.5, 2, 1900, 10, 20))
# 50.5
print(compute_phone_bill(35.5, 2, num_minutes_extra_calls=100))
# 55.5
print(compute_phone_bill(35.5, 2, num_minutes_extra_calls=100, num_extra_sms=100))
