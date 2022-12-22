class MongoDB:
    @staticmethod
    def create(cls, collection, object):
        collection.insert_one(object)
        return True

    @staticmethod
    def read(cls, collection, filter):
        return collection.find_one(filter)

    @staticmethod
    def update(cls, collection, filter, object):
        collection.update_one(filter, object)
        return True

    @staticmethod
    def delete(cls, collection, filter):
        collection.delete_one(filter)
        return True


def init_database():
    db = MongoDB()
    return db
