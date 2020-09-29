def get_file_extension(file_name):
    return file_name.split('.')[-1]

def is_image_file(file_name):
    return get_file_extension(file_name).lower() in {'png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif'}

def is_square(dimension):
    return dimension[0] == dimension[1]

def is_portrait(dimension):
    return dimension[1] > dimension[0]

def is_landscape(dimension):
    return dimension[0] > dimension[1]

def get_square_image_details(image_details):
    images = []

    for i in image_details:
        if is_square(i[1]): images.append(i)

    return images

def get_portrait_image_details(image_details):
    images = []

    for i in image_details:
        if is_portrait(i[1]): images.append(i)

    return images

def get_landscape_image_details(image_details):
    images = []

    for i in image_details:
        if is_landscape(i[1]): images.append(i)

    return images

def get_matching_files(file_list, keyword):
    files = []

    for f in file_list:
        if keyword in f: files.append(f)

    return files




