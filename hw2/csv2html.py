from mycsv import *

# Get data
data = readcsv(getdata())

# Create top part of table
html = '<html>\n<body>\n<table>\n'

# Create header row
header = '<tr>'
for col_name in data[0]:
    header += f'<th>{col_name}</th>'
header += '</tr>\n'
html += header

# Create data rows
for row in data[1]:
    row_html = '<tr>'
    for value in row:
        row_html += f'<td>{value}</td>'
    row_html += '</tr>\n'
    html += row_html

# Create bottom part of table
html += '</table>\n</body>\n</html>'

# Print html format
print(html)
