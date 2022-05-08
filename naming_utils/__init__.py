from datetime import datetime
from random import randint

import os


def unique_name_with_ts(path=None, extension=None):
    """
    Create a unique name with timestamp.
    :param path: path to file
    :param extension: file extension
    :return: unique name
    """

    if path and type(path) is not str:
        raise TypeError('path must be a string')
    
    if extension and type(extension) is not str:
        raise TypeError('extension must be a string')

    while True:
        name = datetime.now().strftime('%Y%m%d_%H%M%S_%f') + str(randint(1, 1000))
        
        if extension:
            if '.' in extension:
                name += extension
            else:
                name += '.' + extension
        
        if path:
            name = os.path.join(path, name)

        if not os.path.exists(name):
            break

    return name


def unique_names_with_ts(count=1, path=None, extension=None):
    """
    Create list of unique names with timestamp.
    :param count: number of names to create
    :param path: path to file
    :param extension: file extension
    :return: unique names
    """

    if type(count) is not int:
        raise TypeError('count must be an integer')

    if count < 1:
        raise ValueError('count must be greater than 0')

    names = set()

    while True:
        names.add(unique_name_with_ts(path, extension))
        if len(names) == count:
            break
        
    return list(names)