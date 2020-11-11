#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.
def get_interchanges(mrt_map):
    stations = {}
    interchanges = {}
    for line in mrt_map:
        for stn in line:
            if stn not in stations:
                stations[stn] = mrt_map.index(line)
            else:
                interchanges[stn] = [stations[stn], mrt_map.index(line)]
                del stations[stn]

    return interchanges


def get_station_coordinates(mrt_map, stn):
    # Key = Line index, Value = Line's Station Index
    # Line 0
    # Line 1
    # Line 2
    coordinates = {}
    for line in mrt_map:
        if stn in line:
            coordinates[mrt_map.index(line)] = line.index(stn)

    return coordinates

# End of your additional functions.
def find_stations_within_distance(mrt_map, orig, dist, parent=None):
    stations = set()
    orig_coords = get_station_coordinates(mrt_map, orig)
    interchanges = get_interchanges(mrt_map)
    parent = orig if parent is None else parent

    # Iterate every coordinate existing in orig_coords
    for line_id in orig_coords.keys():
        # Get orig's index for this line first
        orig_index = mrt_map[line_id].index(orig)

        # Start travelling
        for station in mrt_map[line_id]:  # Loop every station first.
            # Ensure we're not double checking the same station.
            if station != orig and station != parent and station not in stations:
                # Get the index.
                stn_index = mrt_map[line_id].index(station)
                difference = stn_index - orig_index if orig_index < stn_index else orig_index - stn_index

                if difference <= dist:
                    stations.add(station)

                # If the station being checked is an interchange and if there's still more difference.
                if station in interchanges.keys() and dist > difference:
                    stations = stations | find_stations_within_distance(mrt_map, station, dist - difference, parent)

    return stations
