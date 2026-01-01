import requests
from elasticsearch import Elasticsearch

# Kết nối ES
es = Elasticsearch(["http://localhost:9200"], basic_auth=("elastic", "changeme_UCzc1Twlw3qGIuCJ4Mai"))

# Tìm các alert mới nhất (status: active)
res = es.search(index="alerts-history", query={"term": {"status": "active"}})

for hit in res["hits"]["hits"]:
    msg = """🚨 Rule name:{rule_name} 
    Message: {log_message}""".format(
        rule_name=hit["_source"]["rule_name"], log_message=hit["_source"]["log_message"]
    )
    # Gửi tới Telegram
    requests.post(
        "https://api.telegram.org/bot8361033360:AAHI523u808WSqgC40lW5DtkwXrYyYewxBE/sendMessage",
        json={"chat_id": "-4887077657", "text": msg},
    )

    # Đánh dấu đã gửi để không gửi lại (Update status thành 'sent')
    es.update(index="alerts-history", id=hit["_id"], doc={"status": "sent"})

# Test gửi tin nhắn với Bot và Chat ID của bạn
# requests.post(
#     "https://api.telegram.org/bot8361033360:AAHI523u808WSqgC40lW5DtkwXrYyYewxBE/sendMessage",
#     json={"chat_id": "-4887077657", "text": "test"},
# )

