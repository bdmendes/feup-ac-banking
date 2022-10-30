from .util import *


def preprocess_clients(clients):
    return extract_date(clients, "birth_number", True)
