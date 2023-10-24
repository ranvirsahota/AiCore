# Everything in bytes

Though everything is stored in bytes and then encoded into some format, but cannot always be opened

```py
with open("images/base64_table.png", 'r') as f:
    data = f.read()
print(data)
print(type(data))
```

The main.py file in this folder tried to open the img in 'utf-8' fromat but it did follow that encoding
and resulted in the following error:
```py
Traceback (most recent call last):
  File "/home/ranvir/AiCore/6_everything_stored_in_bytes/main.py", line 2, in <module>
    data = f.read()
           ^^^^^^^^
  File "<frozen codecs>", line 322, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
```

The way to get around this is by add in 'b' to 'r' making 'rb'
```py
with open("images/base64_table.png", 'rb') as f:
    data = f.read()
print(data)
print(type(data))
```

This works becuase it read the bytes
```
b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x8d\x00\x00\x01\xde\x08\x03\x00\x00\x00\xc9\x81\xc1\xbb\x00\x00\x00 cHRM\x00\x00z& .......
<class 'bytes'>
```

## Further explanations:
- https://stackoverflow.com/questions/9644110/difference-between-parsing-a-text-file-in-r-and-rb-mode