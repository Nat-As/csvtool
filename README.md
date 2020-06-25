# csvtool
This tool converts csv rows to a key, value pair and queries a list of keys. I'm uploading it here so I don't have to type it again.
# How it works
This script uses a single row csv file (key) and a two row csv file (key-val) where column 0 is a list of keys and column 1 is a list of corresponding values. The keys from the keyfile are looked up in the key-val file and the corresponding values are printed next to the keys.
|KEY|
|---|
|001|
|004|
|058|
|999|
|002|

|Key|Val|
|---|---|
|001|0x01F|
|002|0x0C8|
|003|0x12C|
|004|0X190|
|...|...|
|999|0x3E7|
### Result:
|KEY|Val|
|---|---|
|001|0x01F|
|004|0X190|
|058|0x03A|
|999|0x3E7|
|002|0x0C8|
# Usage
```python3 sort.py```
