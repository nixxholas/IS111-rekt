import math


# Taxi far = Meter Fare + Surcharges
# Meter Fare = Flag-down fare + fare based on distance

def get_meter_fare(dist, fd_fare=3.5, rate_within_9_8km=0.22, rate_beyond_9_8km=0.22):
    fare = fd_fare  # Flag-down by default

    if dist > 9800:
        fare += (math.ceil((dist - 9800) / 350) * rate_beyond_9_8km)  # Obtain the fare beyond 9.8km
        dist -= (dist - 9800)  # Deduct the distance traveled beyond 9.8km first
    if 9800 >= dist > 1000:
        fare += (math.ceil((dist - 1000) / 400) * rate_within_9_8km)  # Obtain the fare between 1 and 9.8km (
        # inclusive)

    return fare


def get_surcharges(has_loc_surcharge, peak, midnight, mtr_fare, loc_surcharge=3.0):
    surcharge = 0.0
    if has_loc_surcharge: surcharge += loc_surcharge
    if mtr_fare > 0 and midnight: surcharge += (mtr_fare * 0.5)
    elif mtr_fare > 0 and peak: surcharge += (mtr_fare * 0.25)
    return surcharge


flag_down_fare = float(input("What's the flag-down fare: $"))
rate_per_400_within_9_8km = float(input("What's the rate per 400 meters within 9.8km? $"))
rate_per_35_beyond_9_8km = float(input("What's the rate per 350 meters beyond 9.8km? $"))
distance = int(input("What's the distance travelled (in meters)? "))
is_peak = input("Is the ride during a peak period? [yes/no] ") == "yes"
is_midnight = False
if not is_peak: is_midnight = input("Is the ride between midnight and 6am? [yes/no] ") == "yes"
has_location_surcharge = input("Is there any location surcharge? [yes/no] ") == "yes"
location_surcharge = 3.0  # Default to 3 for now
if has_location_surcharge:
    location_surcharge = float(input("What's the amount of location surcharge? $"))

meter_fare = get_meter_fare(distance, flag_down_fare, rate_per_400_within_9_8km, rate_per_35_beyond_9_8km)
print("The total fare is $" + str(round(meter_fare + get_surcharges(has_location_surcharge, is_peak, is_midnight,
                                                                    meter_fare, location_surcharge), 2)))
