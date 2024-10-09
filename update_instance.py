#! python3

import requests
import ast
import json

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
