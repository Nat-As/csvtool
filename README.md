# csvtool
This tool converts csv rows to a key, value pair and queries a list of keys. I'm uploading it here so I don't have to type it again.
# How it works
This script uses a single row csv file (key) and a two row csv file (key-val) where column 0 is a list of keys and column 1 is a list of corresponding values. The keys from the keyfile are looked up in the key-val file and the corresponding values are printed next to the keys.
# Usage
```python3 sort.py```
