import React, { useState } from 'react';
import './WordList.css';
import { Input, Button, List, Card } from 'antd';
import lexiServerApi from '../services/lexiServer';

const WordList = () => {
  const [data, setData] = useState([]);
  const [inputValue, setInputValue] = useState('hello lexi-growth!');
  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleButtonClick = async () => {
    const list = await lexiServerApi.filter(inputValue);
    list.sort((a, b) => b.count - a.count);
    setData(list);
  };


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
          {formatContent(item.definition)}
        </p>
      {}
      </Card>
    </List.Item>
  );

  return (
    <div className='word-list-container'>
      <h1>Word List</h1>
      <Input.TextArea
        placeholder="Enter some text..."
        value={inputValue}
        autoSize={{ minRows: 3, maxRows: 5}}
        onChange={handleInputChange}
      />
      <Button type="primary" onClick={handleButtonClick}>
        Submit
      </Button>
      <h3>total:{data.length}</h3>
      <List
        itemLayout="horizontal"
        dataSource={data}
        renderItem={renderItem}
      />
    </div>
  );
};

export default WordList;