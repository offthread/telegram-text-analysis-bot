from elasticsearch import Elasticsearch


class ElasticSearchFacade(object):
    def __init__(self):
        self.connector = Elasticsearch()

    def insert_update(self, update):
        doc = {
            'author': update._effective_message.from_user.username,
            'author_id': update._effective_message.from_user.id,
            'text': update._effective_message.text,
            'date': update._effective_message.date,
        }

        res = self.connector.index(
            index="messages", doc_type='message', body=doc)
