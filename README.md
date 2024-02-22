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

#### merge words to known-list
to be continued

## run
```
python -m lexi_growth [file-path]
```