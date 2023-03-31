import pymongo

# connect my pipeline to the database using pymongo to connect to mongoDB


class StackPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['stackoverflow']
        self.collection = db['questions']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

