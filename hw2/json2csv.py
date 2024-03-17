import json
from mycsv import *

# Get data
data = json.loads(getdata())

# Add header
headers = data['headers']
csv = ','.join(headers) + '\n'

# Add rows
data = data['data']
number_rows = len(data)
for i in range(number_rows):
    csv += ','.join(data[i].values()) + '\n'

# Remove last new line
csv = csv[:-1]

# Print CSV
print(csv)
