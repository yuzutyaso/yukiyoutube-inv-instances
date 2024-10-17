#! python3
# update_instance.py

import requests
import ast
import json

# TODO:並行処理等で効率化

def fetch(urlpath, apis):
    success_apis = []

    for api in apis:
        try:
            res = requests.get(f'{api}api/v1{urlpath}', timeout=(3.0, 1.5))
            if 'error' not in json.loads(res.text):
                success_apis.append(api)
        except:
            pass
    return success_apis

    
with open('./instances_list.txt') as f:
    apis_list = ast.literal_eval(f.read())

videos = fetch('/videos/shs0rAiwsGQ', apis_list)
search = fetch('/search?q=test&page=1&hl=ja', apis_list)
channel = fetch('/channles/@cosmobsp', apis_list)
comment = fetch('/comments/shs0rAiwsGQ', apis_list)


with open('./videos_apis', mode="w") as f:
    f.write(list(set(videos)))

with open('./search_apis', mode="w") as f:
    f.write(list(set(search)))

with open('./channel_apis', mode="w") as f:
    f.write(list(set(channel)))

with open('./comment_apis', mode="w") as f:
    f.write(list(set(comment)))
