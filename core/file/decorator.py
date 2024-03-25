from .functions import read_file
from words.functions import create_db_data


def word_analyzer(func):
    def wrapper(*args, **kwargs):
        global key
        path_file = func(*args, **kwargs).file.path
        words, counter = read_file(path_file)
        key = create_db_data(words=words, counter_all=counter, path=path_file)
        return func(*args, **kwargs)

    return wrapper


def get_key(func):
    def wrapper(*args, **kwargs):
        url = func(*args, **kwargs) + key
        return url

    return wrapper
