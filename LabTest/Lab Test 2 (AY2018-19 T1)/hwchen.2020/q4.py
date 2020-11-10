#
# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020
#

# If needed, you can define your own additional functions here.
# Start of your additional functions.

# End of your additional functions.
def build_interchanges(mrt_map):
    # Sample.
    # (line1_index, line2_index, line1_stn_index, line2_stn_index, stn_name)
    intersections = set()
    # Loop every line once again
    for line in mrt_map:
        # Loop every station
        for i in range(len(line)):
            cur_stn = line[i]  # Set the current station just in case.

            # Loop every other line:
            for other_line in mrt_map:
                # Make sure its not the line we're checking on and ensure that the cur_stn also exist in this
                # other line.
                if other_line is not line and cur_stn in other_line:
                    # Since it is, its a cross section.
                    intersections.add((mrt_map.index(line), mrt_map.index(other_line), i, other_line.index(cur_stn),
                                       cur_stn))

    return list(intersections)


def get_distance_between_stations(mrt_map, s1, s2, interchanges):
    s1_line_num = -1
    s1_index = -1
    s2_line_num = -1
    s2_index = -1

    for line in mrt_map:
        # Basic flow
        if s1 in line and s2 in line:
            if line.index(s1) > line.index(s2):
                return line.index(s1) - line.index(s2)
            else:
                return line.index(s2) - line.index(s1)
        # Advanced flow, both stations are not on the station.
        else:
            if s1 in line:
                s1_index = line.index(s1)
                s1_line_num = mrt_map.index(line)
            if s2 in line:
                s2_index = line.index(s2)
                s2_line_num = mrt_map.index(line)


    return None


def find_lines_in_s1_but_not_s2(mrt_map, s1, s2):
    lines = []
    for line in mrt_map:
        if s1 in line and s2 not in line:
            lines.append(line)
    return lines


def find_stations_within_distance(mrt_map, orig, dist):
    stations = set()
    interchange_data = build_interchanges(mrt_map)

    for line in mrt_map:
        for station in line:
            if orig != station:
                dist = get_distance_between_stations(mrt_map, orig, station, interchange_data)

    # Loop the lines, get the interchange data first.
    # for line in mrt_map:
    #     # Ensure the origin is in the line.
    #     if orig in line:
    #         # Get the index of the orig if its in this line
    #         orig_i = line.index(orig)
    #
    #         # Loop the layers
    #         for i in range(dist):
    #             # Perform Naive Range Traversal First
    #             if orig_i - (i + 1) >= 0:
    #                 stations.add(line[orig_i - (i + 1)])
    #             if orig_i + (i + 1) < len(line):
    #                 stations.add(line[orig_i + (i + 1)])
    #
    # # Now we, need to ensure that we have inter-line checks as well.
    # if dist > 1:
    #     stations_to_track = list(stations)
    #     # Traverse every station.
    #     for station in stations_to_track:
    #         stn_dist = get_distance_between_stations(mrt_map, orig, station)
    #         cur_dist_left = dist - stn_dist
    #
    #         if cur_dist_left > 0:
    #             lines_to_search = find_lines_in_s1_but_not_s2(mrt_map, station, orig)
    #
    #             for line in lines_to_search:
    #                 stn_index = line.index(station)
    #
    #                 # Loop the layers
    #                 for i in range(cur_dist_left):
    #                     # Perform Naive Range Traversal First
    #                     if stn_index - (i + 1) >= 0:
    #                         stations.add(line[orig_i - (i + 1)])
    #                     if stn_index + (i + 1) < len(line):
    #                         stations.add(line[orig_i + (i + 1)])

    return stations
