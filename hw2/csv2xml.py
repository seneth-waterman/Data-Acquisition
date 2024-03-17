from mycsv import *


# Get data
data = getdata()
data = data.split('\n')

# Create top part of xml
xml = '<?xml version="1.0"?>\n<file>\n'

# Create header part of xml
header = f'  <headers>{data[0]}</headers>\n'
xml += header

# Create data part of xml
xml += '  <data>\n'
header = data[0].split(',')
for row in data[1:]:
    row = row.split(',')
    xml += '    <record>\n'
    xml += '      '
    for i in range(len(row)):
        xml +=f'''<{header[i].replace(' ', '_')}>{row[i]}</{header[i].replace(' ', '_')}>'''
    xml += '\n'
    xml += '    </record>\n'

# Create bottom part of xml
xml += '  </data>\n'
xml += '</file>'

# Print xml
print(xml)
