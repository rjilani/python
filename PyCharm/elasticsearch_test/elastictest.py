__author__ = 'rjilani'

from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch()

es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

a = es.get(index="my-index", doc_type="test-type", id=42)['_source']

print a

