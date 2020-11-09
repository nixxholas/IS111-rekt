#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.

# End of your additional functions.
def get_distance_between_stations(mrt_map, s1, s2):
    for line in mrt_map:
        if s1 in line and s2 in line:
            if line.index(s1) > line.index(s2):
                return line.index(s1) - line.index(s2)
            else:
                return line.index(s2) - line.index(s1)


def find_lines_in_s1_but_not_s2(mrt_map, s1, s2):
    lines = []
    for line in mrt_map:
        if s1 in line and s2 not in line:
            lines.append(line)
    return lines


def find_stations_within_distance(mrt_map, orig, dist):
    stations = set()

    # Loop the lines, get the interchange data first.
    for line in mrt_map:
        # Ensure the origin is in the line.
        if orig in line:
            # Get the index of the orig if its in this line
            orig_i = line.index(orig)

            # Loop the layers
            for i in range(dist):
                # Perform Naive Range Traversal First
                if orig_i - (i + 1) >= 0:
                    stations.add(line[orig_i - (i + 1)])
                if orig_i + (i + 1) < len(line):
                    stations.add(line[orig_i + (i + 1)])

    # Now we, need to ensure that we have inter-line checks as well.
    if dist > 1:
        stations_to_track = list(stations)
        # Traverse every station.
        for station in stations_to_track:
            stn_dist = get_distance_between_stations(mrt_map, orig, station)
            cur_dist_left = dist - stn_dist

            if cur_dist_left > 0:
                lines_to_search = find_lines_in_s1_but_not_s2(mrt_map, station, orig)

                for line in lines_to_search:
                    stn_index = line.index(station)

                    # Loop the layers
                    for i in range(cur_dist_left):
                        # Perform Naive Range Traversal First
                        if stn_index - (i + 1) >= 0:
                            stations.add(line[orig_i - (i + 1)])
                        if stn_index + (i + 1) < len(line):
                            stations.add(line[orig_i + (i + 1)])

    return stations
