import base64

with open("images/base64_table.png", 'rb') as f:
    data = f.read()

print('Raw data:\n',data)
print('Type is: ', type(data))

data = base64.b64encode(data)
print('Encoded:\n', data)

data = base64.b64decode(data)
print('base64 decoded\n',data)
print('Type is: ', type(data))

with open('images/base64_table_new.png', 'wb') as f:
    f.write(data)