import pymongo


class StackPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['stackoverflow']
        self.collection = db['questions']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item

