# lexi-growth

## venv
```
python -m venv .venv
source .venv/bin/activate
```

## setup
```
pip install -r requirements.txt
```

## test
```
python -m pytest
```

## build known-list
konwn-list is a list of words that are known to be valid

#### known-list format
known-list file is a csv file with heeader as "word"

#### known-list config
set the known-list file path in .env file

#### quick build known-list
to be continued


## run
#### filter words
```
python -m lexi_growth --filter file_path=file_path index=1 max_words=20
```
file_path: required

index: optional, only used for epub file, values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

max_words: optional, values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

handles: optional, values: english_definition, chinese_translation

#### merge words to known-list
```
python -m lexi_growth --merge 
```