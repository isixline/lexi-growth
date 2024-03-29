import React, { useState } from 'react';
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
    console.log(list);
    setData(list);
  };

  const renderItem = (item) => (
    <List.Item>
      <Card title={item.word} extra={item.count}>
        <p>{item.definition}</p>
        <p>{item.translation}</p>
      </Card>
    </List.Item>
  );

  return (
    <div>
      <h1>Word List</h1>
      <Input.TextArea
        placeholder="Enter some text..."
        value={inputValue}
        onChange={handleInputChange}
      />
      <Button type="primary" onClick={handleButtonClick}>
        Submit
      </Button>
      <List
        itemLayout="horizontal"
        dataSource={data}
        renderItem={renderItem}
      />
    </div>
  );
};

export default WordList;