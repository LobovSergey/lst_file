from datetime import datetime
import hashlib
from re import split
from collections import Counter
from core.settings import MOST_COMMON


def hash_str(path: str) -> str:
    bytes_str = path.encode()
    return hashlib.sha1(bytes_str).hexdigest()


def create_key(request):
    key = request
    name = request.FILES["file"].name + str(datetime.now())
    key = hash_str(name)
    return key


def prepare_data(collections: Counter):
    global count
    _dict = {key: val for key, val in dict(
        collections).items() if len(key) > 3}
    end_collection = Counter(_dict).most_common(MOST_COMMON)
    ended_dict = dict(end_collection)
    count = sum(Counter(_dict).values())
    return ended_dict, count


def collect_words(words: Counter, collections: Counter = None) -> list:
    string_collection = Counter(words)
    collections += string_collection
    return collections


def read_file(path):
    collections = Counter("")
    with open(path, "r", encoding="UTF-8") as f:
        for line in f:
            line = line.title()
            words = split(r"\W|'' ", line)
            collections = collect_words(words, collections)
    return prepare_data(collections)


def get_counter():
    return count
