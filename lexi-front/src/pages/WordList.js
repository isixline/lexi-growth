import React, { useState } from 'react';
import './WordList.css';
import { Input, Button, List, Card, Select } from 'antd';
import lexiServerApi from '../services/lexiServer';

const WordList = () => {
  const [data, setData] = useState([]);
  const [inputValue, setInputValue] = useState('hello lexi-growth!');
  const [revertedWord, setRevertedWord] = useState('');
  const [loadingData, setLoadingData] = useState(false);
  const [resourceLocator, setResourceLocator] = useState('');
  const [sortType, setSortType] = useState('');

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleRevertChange = (e) => {
    setRevertedWord(e.target.value);
  }

  const handleResourceLocatorChange = (e) => {
    setResourceLocator(e.target.value);
  }

  const handleSortChange = (value) => {
    setSortType(value);
    sortData(data, value);
  };

  const sortData = (data, sortType) => {
    if (!sortType) {
      return;
    }
    data.sort((a, b) => {
      if (sortType === 'count') {
        return b.count - a.count;
      } else if (sortType === 'difficulty') {
        return a.difficulty - b.difficulty;
      }
      return 0;
    });
  }

  const handleButtonClick = async () => {
    setLoadingData(true);
    const list = await lexiServerApi.filter(inputValue);
    setData(list);
    sortData(list, sortType);
    setLoadingData(false);
  };

  const handleRevertClick = async () => {
    if (!revertedWord) {
      return;
    }

    await lexiServerApi.revert(revertedWord);

    setRevertedWord('');
  }

  const handleMergeClick = async (item) => {
    await lexiServerApi.merge(item.word);
    const updatedData = data.map((d) => {
      if (d.word === item.word) {
        return { ...d, known: true };
      }
      return d;
    });
    setData(updatedData);
  }

  const handleExtractClick = async () => {
    setInputValue('Extracting...');
    const text = await lexiServerApi.extractText(resourceLocator);
    setInputValue(text);
    setData([]);
  }

  const formatContent = (content) => {
    return content.split('\\n').map((line, index) => (
      <span key={index}>
        {line}
        <br />
      </span>
    ));
  }

  const renderItem = (item) => (
    <List.Item>
      <Card size="small"
        title={item.word}
        extra={<div><span>{item.count}</span><Button type="link" onClick={() => handleMergeClick(item)}> known! </Button></div>}
        style={{ width: "100%", display: item.known ? 'none' : 'block' }}
      >
        <p>
          {item.difficulty && `🌟 ${item.difficulty}`}
          <br />
          {formatContent(item.definition)}
        </p>
        { }
      </Card>
    </List.Item>
  );

  return (
    <div className='word-list-container'>
      <h1>LexiGrowth</h1>

      <div className='util-container'>
        <Input
          value={revertedWord}
          onChange={handleRevertChange}
        />
        <Button danger onClick={handleRevertClick}>
          Revert
        </Button>
        
      
        <Input
          value={resourceLocator}
          onChange={handleResourceLocatorChange}
        />
        <Button onClick={handleExtractClick}>
          Extract
        </Button>
      </div>

      <Input.TextArea
        placeholder="Enter some text..."
        value={inputValue}
        autoSize={{ minRows: 3, maxRows: 5 }}
        onChange={handleInputChange}
      />
      <Button type="primary" onClick={handleButtonClick}>
        Filter
      </Button>

      {
        loadingData 
          ? (<h3>Loading...</h3>)
          : (
            <>
            <h3>total:{data.length}</h3>

            <Select
              value={sortType}
              onChange={handleSortChange}
              style={{ width: 120 }}
            >
              <Select.Option value="count">Count ⬇️</Select.Option>
              <Select.Option value="difficulty">Difficulty ⬆️</Select.Option>
            </Select>

            <List
              itemLayout="horizontal"
              dataSource={data} 
              renderItem={renderItem}
            />
            </> 
          ) 
      }

    </div>
  );
};

export default WordList;