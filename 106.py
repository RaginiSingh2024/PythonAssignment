# Json Module
import json

with open('data.json', 'r') as f:
  data = json.load(f)

data['name'] = 'Updated Name'

with open('data.json', 'w') as f:
  json.dump(data, f)