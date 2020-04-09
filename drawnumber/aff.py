import pandas as pd
import json
from pandas import json_normalize

path = '../drawnumber.json'

with open(path, 'r') as file:
    d = json.load(file)
    print(d)


test = json_normalize(data = d,
                      record_path = 'fields')

test2 = json_normalize(d)

print(test2['fields.drawingcode'])
print(test2.info())

