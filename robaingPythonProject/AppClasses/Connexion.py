import pymongo, json


class Connexion:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["pingpongtournament"]


    def fermer_client(self):
        client.close()







