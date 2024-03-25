from .functions import read_file
from words.functions import create_db_data


def word_analyzer(func):
    def wrapper(*args, **kwargs):
        path_file = func(*args, **kwargs).file.path
        words, counter = read_file(path_file)
        create_db_data(words=words, counter_all=counter, path=path_file)
        return func(*args, **kwargs)
    return wrapper
