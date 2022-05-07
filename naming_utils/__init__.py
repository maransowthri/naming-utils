from datetime import datetime
from random import randint

import os


def unique_name_with_ts(path=None, extension=None):
    """
    Create a timestamp file name.
    :param path: path to file
    :param extension: file extension
    :return: file name
    """

    if path and type(path) is not str:
        raise TypeError('path must be a string')
    
    if extension and type(extension) is not str:
        raise TypeError('extension must be a string')

    while True:
        file_name = datetime.now().strftime('%Y%m%d_%H%M%S_%f') + str(randint(1, 1000))
        
        if extension:
            if '.' in extension:
                file_name += extension
            else:
                file_name += '.' + extension
        
        if path:
            file_name = os.path.join(path, file_name)

        if not os.path.exists(file_name):
            break

    return file_name


def unique_names_with_ts(count=1, path=None, extension=None):
    """
    Create list of timestamp file names.
    :param count: number of file names to create
    :param path: path to file
    :param extension: file extension
    :return: file name
    """

    if type(count) is not int:
        raise TypeError('count must be an integer')

    if count < 1:
        raise ValueError('count must be greater than 0')

    filenames = set()

    while True:
        filenames.add(unique_name_with_ts(path, extension))
        if len(filenames) == count:
            break
        
    return list(filenames)