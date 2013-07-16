#!/usr/bin/env python
#coding: utf-8

from pymongo import MongoClient
from auswendig_verben.conf import (MONGO_IP, MONGO_PORT, MONGO_DB_NAME)


verb_store = None

class VerbStoreFactory:
    DEFAULT_VERBS_COLLECTION_NAME = 'verbs_collection'

    def __init__(self, host, port, db_name, verbs_collection_name=None):
        if verbs_collection_name is None:
            verbs_collection_name = self.DEFAULT_VERBS_COLLECTION_NAME
        self._client = MongoClient(host, port)
        self._db = self._client[db_name]
        self.verbs_collection = self._db[verbs_collection_name]


def init_verb_store(host, port, db_name):
    global verb_store
    verb_store = VerbStoreFactory(host, port, db_name)


if __name__ == '__main__':
    init_verb_store(MONGO_IP, MONGO_PORT, MONGO_DB_NAME)
    print verb_store.verbs_collection.find_one()

