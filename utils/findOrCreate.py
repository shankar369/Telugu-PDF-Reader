from os.path import isdir
from os import makedirs


def find_or_create(paths: list):
    for each_path in paths:
        if not isdir(each_path):
            makedirs(each_path)
