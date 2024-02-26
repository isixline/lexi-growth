# lexi-growth

## venv
```
python -m venv myenv
source venv/bin/activate
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
python -m lexi_growth --filter file_path=file_path handles=english_definition,chinese_translation
```
file_path: required
handles: optional, default is all handles

#### merge words to known-list
```
python -m lexi_growth --merge 
```