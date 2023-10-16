from pymongo import MongoClient

class ANIMAL_SHELTER:
    def __init__(self, username, password, host, port, db, collection):
        #print('mongodb://%s:%s@%s:%d' % (username, password, host, port))
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port))        
        self.db = self.client['%s' % (db)]       
        self.collection = self.db['%s' % (collection)]

    def create(self, data):
       try:
           result = self.collection.insert_one(data)
           return True if result.inserted_id else False
       except Exception as e:
           print("Error:", e)
           return False
       
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception as e:
            print("Error:", e)
            return []

    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, update_data)
            return result.modified_count
        except Exception as e:
            print("Error:", e)
            return 0

    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Error:", e)
            return 0
