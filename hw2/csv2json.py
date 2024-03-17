from mycsv import *


# Get data
data = getdata()
data = data.split('\n')

json = '{\n'

# Create header portion
header = data[0].split(',')
header_json = ''
for name in header:
    header_json += f'''"{name}", '''
header_json = header_json[:-2]
json += f'''  "headers":[{header_json}],\n'''

# Create data portion
json += '''  "data":[\n'''
for row in data[1:]:
    row = row.split(',')
    content = ''
    for i in range(len(row)):
        content += f'''"{header[i]}":"{row[i]}", '''
    content = content[:-2]
    json += '    {\n'
    json += f'''      {content}\n'''
    json += '    },\n'

json = json[:-2] + '\n'
json += '  ]\n'
json += '}'

print(json)
