# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def get_relation_through_link(family_dict, link):
    # Modify the code below.
    relation_map = {}
    with open('relation_mapping.txt') as relations:
        for relation in relations:
            datum = relation.rstrip().split(':')
            relationship_chunk = tuple(datum[0][1:len(datum[0]) - 1].split(','))
            relation_map[relationship_chunk] = datum[1]

    link_text = []
    if len(link) > 1:
        for i in range(len(link) - 1):
            if (link[i], link[i + 1]) in family_dict.keys():
                link_text.append(family_dict[(link[i], link[i + 1])])

    # Build the link_text as a tuple
    while len(link_text) > 2:
        # Take out the first two.
        front_link = (link_text.pop(0), link_text.pop(0))
        # Obtain the new rs for the first two
        new_rs = relation_map[front_link]
        # Replace the first with new_rs
        link_text.insert(0, new_rs)

    rs_link = tuple(link_text)

    return relation_map[rs_link]
