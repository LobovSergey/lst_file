from datetime import datetime
import hashlib
from re import split
from collections import Counter


def hash_str(path: str) -> str:
    bytes_str = path.encode()
    return hashlib.sha1(bytes_str).hexdigest()


def create_key(request):
    key = request
    name = request.FILES["file"].name + str(datetime.now())
    key = hash_str(name)
    return key


def prepare_data(collections):
    result = dict(collections.most_common(51))
    count = sum(collections.values()) - int(result[""])
    del result[""]
    return result, count


def collect_words(words: Counter, collections: Counter = None) -> list:
    string_collection = Counter(words)
    collections += string_collection
    return collections


def read_file(path):
    collections = Counter("")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.title()
            words = split(r"\W|'' ", line)
            collections = collect_words(words, collections)
    return prepare_data(collections)
