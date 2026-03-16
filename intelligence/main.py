from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'])
res = es.search(query={'match_all':{}},index='intel-logs',size=100)
hits = res['hits']['hits']
for hit in hits:
    print(hit)