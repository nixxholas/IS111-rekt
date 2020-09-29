import os
from PIL import Image

import util

def get_all_image_details_in_dir(img_dir):
    details = []
    file_names_list = os.listdir(img_dir)
    for file_name in file_names_list:
        # Only those files that are image files are considered.
        if(util.is_image_file(file_name)):
            file_full_path = os.path.join(img_dir, file_name)
            dimension = Image.open(file_full_path).size
            details.append((file_name, dimension))
    return details

def get_square_image_details_in_dir(img_dir):
    all_image_details = get_all_image_details_in_dir(img_dir)
    square_image_details = util.get_square_image_details(all_image_details)
    return square_image_details

def get_portrait_image_details_in_dir(img_dir):
    all_image_details = get_all_image_details_in_dir(img_dir)
    portrait_image_details = util.get_portrait_image_details(all_image_details)    
    return portrait_image_details

def get_landscape_image_details_in_dir(img_dir):
    all_image_details = get_all_image_details_in_dir(img_dir)
    landscape_image_details = util.get_landscape_image_details(all_image_details)    
    return landscape_image_details

def get_matching_image_details(img_dir, keyword):
    details = []
    file_names = util.get_matching_files(os.listdir(img_dir), keyword)
    for file_name in file_names:
        if(util.is_image_file(file_name)):
            file_full_path = os.path.join(img_dir, file_name)
            dimension = Image.open(file_full_path).size
            details.append((file_name, dimension))
    return details