from .models import WordsModel


def create_db_data(words: dict, counter_all: int, obj: int) -> str:
    for word, count in words.items():
        WordsModel.objects.create(
            word=word, counter=count, term_frequency=count / counter_all, document=obj
        )
