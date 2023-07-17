#!/usr/bin/env python3
import os
import requests

path = "/data/feedback"
dirs = os.listdir(path)
url = "http://34.173.189.203/feedback/"
dicts = []

for filename in dirs:
    if filename.endswith('.txt'):
        with open(os.path.join(path, filename)) as f:
            content = f.read()
            lines = content.split("\n")
            dict = {
                'title': lines[0],
                'name': lines[1],
                'date': lines[2],
                'feedback': lines[3]
            }
            
            dicts.append(dict)
print(dicts)
for item in dicts:
  response = requests.post(url, json=item)
  response.raise_for_status()