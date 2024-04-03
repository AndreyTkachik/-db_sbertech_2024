import json
import time
from types import NoneType
import redis

red = redis.Redis(host="127.0.0.1", port=6379, db=0)

with open('data.json') as file:
    json_data = file.read()

data = json.loads(json_data)

# STRING
start = time.time()
red.set('json_data', json.dumps(data))
end = time.time()
print("STRING:", end - start)

# HSET
start = time.time()
for i, item in enumerate(data):
    red.hset('temperature_data_hset', i, json.dumps(item))

end = time.time()
print("HSET:", end - start)

# ZSET
start = time.time()
for i, item in enumerate(data):
    score = item['AverageTemperature']
    if type(score) == NoneType:
        continue
    red.zadd('temperature_data_zset', {json.dumps(item): score})

end = time.time()
print("ZSET:", end - start)

# List
start = time.time()
for item in data:
    red.rpush('temperature_data_list', json.dumps(item))

end = time.time()
print("List:", end - start)
