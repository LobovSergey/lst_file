from .functions import read_file
from words.functions import create_db_data


def word_analyzer(func):
    def wrapper(*args, **kwargs):
        req = func(*args, **kwargs)
        words, counter = read_file(req.file.path)
        create_db_data(words=words, counter_all=counter, obj=req)
        return func(*args, **kwargs)

    return wrapper
