import os
import re


def collect_images_in(root):
    image_list = []
    for dir_name, dir_names, file_names in os.walk(root):
        for file_name in file_names:
            if __file_is_image(file_name):
                image_list.append(os.path.join(dir_name, file_name))
    return image_list


def __file_is_image(file_name):
    regex = re.compile('(.* ?).(jpe?g|JPE?G|png|PNG)')  # regex for filtering for specific image endings
    return re.match(regex, file_name)
