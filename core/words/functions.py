from .models import WordsModel
import hashlib


def create_secret_key(path: str) -> str:
    bytes_str = path.encode()
    return hashlib.sha1(bytes_str).hexdigest()


def create_db_data(words: dict, counter_all: int, path) -> str:
    key = create_secret_key(path)
    for word, count in words.items():
        WordsModel.objects.create(
            word=word, counter=count, term_frequency=count / counter_all, secret_key=key
        )
    return key
