def get_file_extension(file_name):
    return file_name.split('.')[-1]

def is_image_file(file_name):
    return get_file_extension(file_name).lower() in {'png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif'}

def is_square(dimension):
    return True

def is_portrait(dimension):
    return True

def is_landscape(dimension):
    return True

def get_square_image_details(image_details):
    return image_details

def get_portrait_image_details(image_details):
    return []

def get_landscape_image_details(image_details):
    return []

def get_matching_files(file_list, keyword):
    return []




