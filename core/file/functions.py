from re import split
from collections import Counter


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
            print(words)
            collections = collect_words(words, collections)
    return prepare_data(collections)
