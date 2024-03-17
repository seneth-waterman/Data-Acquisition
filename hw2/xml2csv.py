import untangle
from mycsv import *

xml = untangle.parse(getdata())

# Gets header
csv = f'{xml.file.headers.cdata}\n'

# Gets row 
number_rows = len(xml.file.data.record)
for i in range(number_rows):
    row = ''
    for elem in xml.file.data.record[i].children:
        row += f'{elem.cdata},'
    row = row[:-1] + '\n'
    csv += row

# Remove last new line
csv = csv[:-1]

# Print CSV
print(csv)
