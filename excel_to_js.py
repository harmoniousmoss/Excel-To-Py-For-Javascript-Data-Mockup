import json
import pandas as pd

df = pd.read_csv('MOCK_DATA.csv')

data = []

for index, row in df.iterrows():
    obj = {
        'id': row['id'],
        'first_name': row['first_name'],
        'last_name': row['last_name'],
        'email': row['email'],
        'gender': row['gender'],
        'ip_address': row['ip_address'],
    }
    data.append(obj)


with open('data.js', 'w') as f:
    f.write('const data = ')
    json.dump(data, f)
    f.write(';')
