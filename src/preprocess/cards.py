from .util import *


def preprocess_cards(cards):
    return extract_date(cards, "issued")
